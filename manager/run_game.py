from screens.menu_screen import MenuScreen
from screens.character_select import character_select
from screens.map_select import map_select_screen
from screens.battle_screen import BattleScreen

def run_game():
    game_state = {
        "player1": None,
        "player2": None,
        "selected_map": None
    }

    while True:
        menu_screen = MenuScreen()
        menu_screen.run()

        character_select(game_state)
        print("chegou no mapa")
        map_select_screen(game_state)
        print("saiu do mapa")

        batle_screen = BattleScreen(game_state)
        batle_screen.run()