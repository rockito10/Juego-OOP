
import os

def cls(): #borra la consola
    os.system('cls' if os.name=='nt' else 'clear')

class Options(): #el objeto que es las opciones
    def __init__(self, game):
        self.game = game
    
    def show_option_menu(self, menu): #opciones para el jugador
        user_input_choice = input(''' --- <OPTIONS> --- 
1- <Record>
2- <>
3- <Go to menu>
              ''')
        self.select_choice(user_input_choice, menu)   
    
    # def check_option_int_and_ret(self, user_input_choice): #chequea que el input sea válido
    #     try:
    #         user_input_number = int(user_input_choice) #transforma en int el input del user
    #         self.check_option_between_possible_choices(user_input_number)
    #         return(user_input_number)
    #     except ValueError:
    #         print("Please input a number between 1 and 3")
    #         return(self.menu_input())
        
            
    # def check_option_between_possible_choices(self, user_input_number): #chequea que el input sea de 1 a 3
    #     if (user_input_number in self.user_possible_choices()):
    #         pass
    #     else: raise ValueError

    # def user_possible_choices(self):
    #     return [1, 2, 3]
    
    def set_record_mode(self):
        self.game.toggle_record_mode()
    
    def select_choice(self, user_input_choice, menu):
        #se ejecuta la opción
        cls()
        match user_input_choice:
            case "1": #test record mode
                self.set_record_mode()
                self.show_option_menu(menu)
            case "2": #options
                # self.game.user_options()
                self.show_option_menu(menu)
            case "3": #return
                pass
            case _:
                print("Please input a number between 1 and 3")
                self.show_option_menu(menu)