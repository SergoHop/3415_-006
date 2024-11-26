import inspect
import json
from pathlib import Path

from deck import Deck
from game_state import GameState
from hand import Hand
from player import Player
from table import Table
from player_interaction import PlayerInteraction
import player_interactions as all_player_types
import enum



class GamePhase(enum.StrEnum):
    CHOOSE_CARD = "Choose card"
    DEAL_CARDS = "Deal cards"
    CHOOSE_ROW = "Choose row"
    DISPLAY_TABLE = "Display table state"
    NEXT_PLAYER = "Switch current player"
    PLACE_CARD = "Place card"
    DECLARE_WINNER = "Declare a winner"
    GAME_END = "Game ended"


class GameServer:
    INITIAL_HAND_SIZE = 10
    chosen_cards = {}
    def __init__(self, player_types, game_state):
        self.game_state: GameState = game_state
        self.player_types: dict = player_types  
        self.stroke_number = 0


    @classmethod
    def load_game(cls, filename: str | Path):
        with open(filename, 'r') as fin:
            data = json.load(fin)
            game_state = GameState.load(data)
            print(game_state.save())
            player_types = {}
            for player, player_data in zip(game_state.players, data['players']):
                kind = player_data['kind']
                kind = getattr(all_player_types, kind)
                player_types[player] = kind
            return GameServer(player_types=player_types, game_state=game_state)


    def save(self, filename: str | Path):
        data = self.save_to_dict()
        with open(filename, 'w') as fout:
            json.dump(data, fout, indent=4)


    def save_to_dict(self):
        data = self.game_state.save()
        for player_index, player in enumerate(self.player_types.keys()):
            player_interaction = self.player_types[player]
            data["players"][player_index]["kind"] = player_interaction.__name__
        return data


    @classmethod
    def get_players(cls):
        player_count = cls.request_player_count()

        player_types = {}
        names_count = {}  
        for _ in range(player_count):
            name, kind = cls.request_player()

            if name in names_count:
                names_count[name] += 1
                new_name = name+str(names_count[name])
                print(f"Имя {name} было изменено на {new_name}")
            else:
                names_count[name] = 1
                new_name = name
            player = Player(new_name, Hand())
            player_types[player] = kind
        return player_types


    @classmethod
    def new_game(cls, player_types: dict):
        deck = Deck(cards=None)
        table = Table()
        for row in table: 
            row.add_card(deck.draw_card())
        game_state = GameState(list(player_types.keys()), deck, table)

        res = cls(player_types, game_state)
        res.deal_cards_phase()
        return res


    def run(self):
        phases = {
            GamePhase.DEAL_CARDS: self.deal_cards_phase,
            GamePhase.DISPLAY_TABLE: self.display_table_state,
            GamePhase.CHOOSE_CARD: self.choose_card_phase,
            GamePhase.NEXT_PLAYER: self.next_player_phase,
            GamePhase.PLACE_CARD: self.place_card_phase,
            GamePhase.DECLARE_WINNER: self.declare_winner_phase,
        }
        current_phase = GamePhase.DISPLAY_TABLE
        while current_phase != GamePhase.GAME_END:
            current_phase = phases[current_phase]()


    def inform_all(self, method: str, *args, **kwargs):
        for p in self.player_types.values():
            getattr(p, method)(*args, **kwargs)


    @staticmethod
    def request_player_count() -> int:
        #
        while True:
            try:
                player_count = int(input("Сколько игроков? "))
                if not 2 <= player_count <= 10:
                    raise ValueError("Число игроков должно быть от 2 до 10.")
                return player_count
            except ValueError as e:
                print(f"Ошибка: {e}")


    @staticmethod
    #
    def request_player() -> tuple[str, type[PlayerInteraction]]:
        player_type_dict = {
        name: cls for name, cls in inspect.getmembers(all_player_types)
        if inspect.isclass(cls) and issubclass(cls, PlayerInteraction)}
        player_types_as_str = ', '.join(player_type_dict.keys())

        while True:
            name = input("Введите имя игрока: ")
            if name.isalpha():
                break
            print("Имя должно состоять из одного слова и только из буквенных символов")

        while True:
            kind = input(f"Выберите тип игрока ({player_types_as_str}): ")
            if kind in player_type_dict:
                return name, player_type_dict[kind]
            print(f"Неверный тип игрока. Допустимые типы: {player_types_as_str}")


    def deal_cards_phase(self):
        for p in self.game_state.players: 
            for _ in range(self.INITIAL_HAND_SIZE):
                p.hand.add_card(self.game_state.deck.draw_card())
        print("Карты разданы игрокам.")
        return GamePhase.DISPLAY_TABLE


    def display_table_state(self):
        self.stroke_number += 1
        if self.stroke_number <= self.INITIAL_HAND_SIZE:
            print(f"\nХОД {self.stroke_number}\nСостояние стола:\n"f"{self.game_state.table} \n\nИгроки выбирают карту")
            return GamePhase.CHOOSE_CARD
        else:
            return GamePhase.DECLARE_WINNER


    def choose_card_phase(self) -> GamePhase: 

        current_player = self.game_state.current_player()
        print(f"Ход игрока: {current_player.name}({current_player.score})")  

        card = self.player_types[current_player].choose_card(current_player.hand, self.game_state.table)
        self.inform_all("inform_card_chosen", current_player)
        if card:
            
            self.chosen_cards[current_player] = card

        if len(self.chosen_cards) == len(self.player_types):
            return GamePhase.PLACE_CARD
        else:
            return GamePhase.NEXT_PLAYER


    def next_player_phase(self) -> GamePhase:
        if self.stroke_number <= self.INITIAL_HAND_SIZE:
            self.game_state.next_player()
            return GamePhase.CHOOSE_CARD
        else:
            return GamePhase.DECLARE_WINNER


    def place_card_phase(self):
        print("\n--- Раскрытие выбранных карт ---")
        for player, card in self.chosen_cards.items():
            print(f"{player.name}({player.score}): {card}")
        print("\n----------------------------------\n")

        for player, card in sorted(self.chosen_cards.items(), key=lambda x: x[1].num):
            print(f'{player.name}({player.score}): добавление карты {card}')
            try:
                try_play = self.game_state.play_card(card, player)
                if try_play:
                    print(f'Карта игрока {player.name}({player.score}) добавлена в один из рядов\n')
                else:
                    print(f"Карту игрока {player.name}({player.score}) невозможно добавить на стол\n")
                    print("\n----------------------------------\n")
                    row_index = self.player_types[player].choose_row(self.game_state.table, player)         
                    self.inform_all("inform_row_chosen", player, row_index)
                    points = self.game_state.table.rows[row_index].truncate()                               
                    player.score += points
                    print(f"{player.name}({player.score}): забирает ряд {row_index + 1} и получает {points} штрафных очков\n"
                          f"Карта {card} становится 1-й в ряду {row_index + 1}\n")
                    self.game_state.table.rows[row_index].add_card(card)
                    self.inform_all("inform_card_played", card)
                    print("\n----------------------------------\n")
            except ValueError as e:
                print(str(e))
        

        self.display_table_state()
        self.chosen_cards = {}
        return GamePhase.NEXT_PLAYER


    def declare_winner_phase(self) -> GamePhase:
        #
        print(self.game_state.table)
        print("\nИгра закончена!\nРезультаты игры:")

        players = self.game_state.players
        winning_score = min(player.score for player in players)
        winners = [player for player in players if player.score == winning_score]

        print(f"{'Победитель:' if len(winners) == 1 else 'Победители:'}")
        for player in winners:
            print(f"- {player.name}: {player.score}")

        losers = [player for player in players if player not in winners]
        print(f"{'Проигравший:' if len(losers) == 1 else 'Проигравшие:'}")
        for player in losers:
            print(f"- {player.name}: {player.score}")

        return GamePhase.GAME_END



def __main__():
    load_from_file = False
    if load_from_file:
        server = GameServer.load_game("korova.json")
    else:
        server = GameServer.new_game(GameServer.get_players())
    server.run()


if __name__ == "__main__":
    __main__()