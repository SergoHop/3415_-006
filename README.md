# Корова006

## Правила игры

### Карты

* Колода состоит из 104 карт. Каждая пронумерована от 1 до 104. На каждой карте, кроме числа, нанесено количество штрафных очков. Всего в колоде:
  * 76 карт с 1-м штрафным очком;
  * 9 карт 2-мя штрафными очками;
  * 10 карт с 3-мя штрафными очками;
  * 8 карт с 5-ю штрафными очками;
  * 1 карта с 7-ю штрафными очками.
* Для лучшего восприятия карты так же отличаются по цвету в зависимости от количества штрафных очков на них:
  * Фиолетовая (число 55) - 7 очков.
  * Оранжевые (кратные 11, исключая 55) - 5 очков;
  * Жёлтые (кратные 10) - 3 очка;
  * Голубые (кратные 5) - 2 очка;
  * Зелёные (все остальные) - 1 очко;

### Комплектность

* Карты 5 цветов (зелёный, голубой, жёлтый, оранжевый, фиолетовый) с номерами от 1 до 104 и количеством штрафных очков на каждой.

### Раздача

* 2-10 игроков.
* Каждому игроку раздаётся 10 карт в закрытую.
* Из колоды берётся 4 карты, которые кладутся в 4 ряда по одной.
* После каждого раунда игрокам снова раздаётся по 10 карт.

### Условие поражения

* Получение 66 и более штрафных очков

### Правила игры

* Игроки ходят одновременно.
* Во время хода игроки
  * Выбирают из руки 1 карту и кладут её на стол в закрытую.
  * Каждый игрок одновременно с остальными переворачивает свою карту.
  * Далее игроки размещают свои карты в ряды
    * Порядок размещения карт определяется её номером - первой размещается карта с наименьшим значением.
    * Далее размещается карта следующая по возрастанию и так далее.
* Карты размещаются в рядах, согласно следующим правилам
  * Каждая следующая карта в ряду должна иметь большее число, чем предыдущая.
  * Разница между числами должна быть минимальна.
  * Если размещаемая карта оказывается шестой в ряду, она начнёт новый ряд. А прошлые пять карт нужно забрать в штрафную стопку.
  * Если карта игрока не подходит ни в один ряд, он выбирает один ряд со стола и забирает его себе.
  * Не подошедшая карта кладется в начало убранного ряда.
* Когда игроки сыграют все свои 10 карт, каждый подсчитывает число своих штрафных баллов и записывает его.
* Далее все карты замешиваются повторно и начинается новый раунд.

## Пример текстового интерфейса игры

Играют игрок 1 и игрок 2.


Играют Sergo и Bot.

```
Row1: 5
Row2: 6
Row3: 80
Row4: 24
Bot: 10, 11, 103, 44, 14, 62, 72, 73, 75, 1
Sergo: 53, 13, 15, 18, 55, 77, 100, 20, 22, 9
Bot: введите, какую карту игрем из руки: 11
Sergo: введите, какую карту играем из руки: 120
Sergo: такой карты нет в руке
Sergo: введите, какую карту играем из руки: 100
Top: открытие карт
----
Row1: 5
Row2: 6, 11
Row3: 80, 100
Row4: 24
Bot: 10, 103, 44, 14, 62, 72, 73, 75, 1
Sergo: 53, 13, 15, 18, 55, 77, 20, 22, 9
Bot: введите, какую карту игрем из руки: 1
Sergo: введите, какую карту играем из руки: 13
Top: открытие карт
Bot: ваша карта не походит ни к одному ряду. Введите ряд, который хотите забрать: 4
----
Row1: 5
Row2: 6, 11, 13
Row3: 80, 100
Row4: 1
Bot: 10, 103, 44, 14, 62, 72, 73, 75
Sergo: 53, 15, 18, 55, 77, 20, 22, 9
....
----
Row1: 5, 10
Row2: 6, 11, 13, 15, 18
Row3: 80, 100, 103
Row4: 1
Bot: 44, 14, 62, 72, 73, 75
Sergo: 53, 55, 77, 20, 22, 9
Bot: введите, какую карту игрем из руки: 14
Sergo: введите, какую карту играем из руки: 20
Top: открытие карт
Sergo: ваша карта последняя во втором ряду. Ряд помещен в вашу штрафную колоду.
----
Row1: 5, 10, 14
Row2: 20
Row3: 80, 100, 103
Row4: 1
Bot: 44, 62, 72, 73, 75
Sergo: 53, 55, 77, 22, 9
....
----
Bot: 67 штрафных очков
Sergo: 58 штрафных очков
Bot Lose!
```
----

## Формат save-файла

```json
{
  "row1": "5",
  "row2": "6",
  "row3": "80",
  "row4": "24",
  "current_player_index": 0,
  "players": [
    {
      "name": "Sergo",
      "hand": "53, 13, 15, 18, 55, 77, 100, 20, 22, 9",
      "is_human": true
      "score1":0
    },
    {
      "name": "Bot",
      "hand": "10, 11, 103, 44, 14, 62, 72, 73, 75, 1",
      "is_human": false
      "score2":0
    }
  ]
}
