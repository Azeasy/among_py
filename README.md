# Among PY
## Singleplayer:
Игрок должен за ограниченное время сделать все задания.
Несколько карт (уровней)
Мини-задания = мини-игры или тестовые вопросы.
На карте есть боты, которые мешают игроку.

## Multiplayer:
Ход игры:
Всего 4-10 игроков
Среди них 1-2 Импостера

Игроки решают задачи по питону, для победы нужно решить всё. Задача - найти импостера.

Импостеры убивают игроков. Задача - убить всех.

### ClassDiagram
class Player
    class fields:
        screen
        image_size

    obj fields:
        image = pygame.image
        nickname = str, max=15
        tasks = []MiniGame
        position = int x, int y

    def display: displays an image at the screen

class Bot(Player)

class Map

class MiniGame
