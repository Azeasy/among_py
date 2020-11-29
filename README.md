# Among PY
## Singleplayer:
Kill them all!

### ClassDiagram
class Player

    fields:
        username
        position
        speed
        bullets
        cooldown
        lives
    methods:
        move
        shot
        get_punch
        is_alive
class Bot(Player)

    fields:
        direction
        duration

class Map

    fields:
        background
        map_arr
        players
        data_path
        assets
        gameover
    methods:
        display_ground
        add_player
        get_asset
        display
