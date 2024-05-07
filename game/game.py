import game.menu as main_menu #importo el menú principal
import game.options as game_options #importo las opciones
import game.match as game_match #importo las partidas 

class Game(): #el objeto que es todo el juego en sí
    def __init__(self):
        self.menu = main_menu.Menu(self) #le doy un menú principal test mode es para los tests 
        self.options = game_options.Options(self)
        self.record_mode = False
        # self.nombre = nombre
        
    def toggle_record_mode(self):
        self.record_mode = not (self.record_mode)
        
    def run(self, test_controls: list = []): #con esto el juego corre
        print("Game is running")
        self.menu.run(test_controls)
        
    def begin_new_match(self, test_controls: list = []): #se crea nueva partida
        self.current_match = game_match.Match(self)
        self.current_match.start(test_controls, self.record_mode)
        
    def user_options(self, menu): #mostrar opciones al jugador
        self.options.show_option_menu(menu)
        self.menu.run(test_controls = [])
        
    def close(self): #para cerrar el juego
        print("Game finished running")
        quit()