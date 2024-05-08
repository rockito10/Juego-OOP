
from structure.Map import DefaultMap
from entities.Player import Player
import os
import time
from pynput import keyboard


def cls(): #borra la consola
        os.system('cls' if os.name=='nt' else 'clear')

class MatchHandler():
    def __init__(self, game):
        self.game = game
        
    def begin_auto_input_taker(self, match):
        with keyboard.Listener(on_press=match.select_response_with) as listener:
            listener.join()
    
    def player_input(self): #controles del usuario y toma su input
        playerResponse = input(''' 
<CONTROLS>            
-W -> Go up
-A -> Go left
-S -> Go down
-D -> Go right
-M -> Map

-O -> Options
-E -> Exit the game   
              ''')
        return playerResponse

class Match(): #el objeto que es las partidas en sí
    def __init__(self, game):
        self.game = game
        self.handler = MatchHandler(game)
        self.generated_map = DefaultMap() #le seteo el mapa predeterminado, habría que hacerlo random más adelante
        self.player = Player()
        self.record_mode = False
        self.record_list = []
        
    def set_record_mode(self, record_mode): # para grabar las keys apretadas y tenerlas al final de la ejecución
        self.record_mode = record_mode
        
    def start(self, test_controls: list, record_mode): # ubico al jugador
        self.set_record_mode(record_mode)
        self.generated_map.locate_player_on_first_floor(self.player)
        self.player.show_screen()
        
        #testing
        if len(test_controls) == 0:
            self.handler.begin_auto_input_taker(self) #no test
            
        else:
            self.take_input_and_respond(test_controls) #test
        
        
    def test(self, test_controls):
        player_response = test_controls[0] #para el testing, remuevo cada elemento para pasar al siguiente (siempre debe terminar con e, sino peta)
        test_controls.pop(0)
        # print(player_response)
        self.select_response_with(player_response, test_controls)

    def take_input_and_respond(self, test_controls: list = []):
        
        print(''' 
<CONTROLS>            
-W -> Go up
-A -> Go left
-S -> Go down
-D -> Go right
-M -> Map

-O -> Options
-E -> Exit the game   
              ''')
        
        if not test_controls: #si no es un test se ejecuta
            # player_response = self.handler.playerInput()
            # self.select_response_with(player_response)
            pass
        
        else: #test
            # time.sleep(0.01)
            self.test(test_controls)
            
    def unused_key_warning(self):
        print("Please input only W A S D or M O E")

    def select_response_with(self, player_response, test_controls: list = [] ): #elige entre la opción elegida y las otras
        cls() #borra la consola para que quede más limpio
        
        if self.record_mode == True:
            self.record_list += [player_response]
        
        if not test_controls:
            #por si es un test o no
            try:
                final_response = player_response.char
            except AttributeError:
                try:
                    final_response = player_response.lower()
                except AttributeError:
                    return
                    
        else: #para testeo (básicamente si es str tengo que hacerle lower, y si es input del cmd es .char, no sé por qué pero bueno)
            final_response = player_response.lower()
            # print(final_response)
        
        try:
          match final_response:
            case "w": #mover arriba
                self.player.move_up()
                # self.player.show_screen()
            case "a": #mover izquierda
                self.player.move_left()
                # self.player.show_screen()
            case "s": #mover abajo
                self.player.move_down()
                # self.player.show_screen()
            case "d": #mover derecha
                self.player.move_right()
                # self.player.show_screen()
            case "m": #mapa
                self.player.show_map()
            case "o": #options
                self.game.user_options()
            case "e": #exit
                print(self.record_list)
                self.game.close()
            case _:
                self.unused_key_warning()
        except KeyboardInterrupt:
            # print("so")
            self.unused_key_warning()
            
        self.take_input_and_respond(test_controls)

    
        
        
                
    
