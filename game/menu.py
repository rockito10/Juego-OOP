
class menuHandler(): #maneja los inputs del menú
    def __init__(self):
        # self.nombre = nombre
        pass
        
    
    def menu_input(self): #toma el input para el menú
        
        user_input_choice = input(''' --- <GAME NAME> --- 
1- Play game
2- Options
3- Exit game        
              ''')
        user_input_number = self.check_option_int_and_ret(user_input_choice)
        return(user_input_number) #ahora es seguro que es un int entre 1 y 3
    
    def check_option_int_and_ret(self, user_input_choice): #chequea que el input sea válido
        try:
            user_input_number = int(user_input_choice) #transforma en int el input del user
            self.check_option_between_possible_choices(user_input_number)
            return(user_input_number)
        except ValueError:
            print("Please input a number between 1 and 3")
            return(self.menu_input())
            
    def check_option_between_possible_choices(self, user_input_number): #chequea que el input sea de 1 a 3
        if (user_input_number in self.user_possible_choices()):
            pass
        else: raise ValueError

    def user_possible_choices(self):
        return [1, 2, 3]
    

class Menu():
    def __init__(self, game):
        self.main_menu_handler = menuHandler()
        self.game = game
        
    def run(self, test_controls: list): #con esto el menú anda
        print("Menu is running")
        
        
        #testing behavior
        
        if not test_controls:
            user_choice = self.main_menu_handler.menu_input() #registra una opción de las dadas
        
            self.select_choice(user_choice) #se ejecuta la opción
        
        else:
            # for control_num in test_controls:
                
            #     user_choice = test_controls[control_num] #paso cada control tipeado
                
            #     self.select_choice(user_choice) #se ejecuta la opción
            
            user_choice = test_controls[0] #tomo el primero nomás para entrar al juego
            test_controls.pop(0)
            self.select_choice(user_choice, test_controls)
        
        print("Menu finished running")
        
    def select_choice(self, option_number, test_controls: list = []):
        #se ejecuta la opción
        match option_number:
            case 1: #play
                self.game.begin_new_match(test_controls)
            case 2: #options
                self.game.user_options(self)
            case 3: #exit
                self.game.close()
        
    