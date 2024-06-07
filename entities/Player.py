# class SubclassResponsability(Exception): #creando exceptions
#     def __init__(self):
#         print(f"Should be replaced in the subclass")

from resources.NoObjects import NoRoom
from entities.GeneralEntities import Entity
from weapons.Weapons import WoodenMurasama
from resources.CardinalDirection import North, West, South, East
from sys import exit
import os
import time
def cls(): #borra la consola
        os.system('cls' if os.name=='nt' else 'clear')

CLR_RST = "\033[0m"

class Player(Entity):
    def __init__(self):
        super().__init__()
        self.current_floor = None
        self.current_room = NoRoom()
        self.current_cuadricule_number = 0
        self.current_room_number = None
        self.map = None
        self.weapon = WoodenMurasama()
        self.looking_at = North()
        self.screen_color = CLR_RST
        
        
    # def set_current_weapon(self, weapon):
    #     self.current_weapon = weapon
    
    def turn(self): #podría servir para aplicar efectos, como fuego, veneno
        pass
    
    def base_hp(self):
        return 100
        
    def set_map(self, map):
        self.map = map

    def enter_floor(self, floor):
        self.current_floor = floor #entra a la habitación que se le dice
        # print(self.current_floor)

    def enter_room_num(self, room, num: int):
        self.current_room.player_leave() #saca al jugador de la sala anterior
        self.current_room = room #entra a la habitación que se le dice
        # print(self.current_room)
        self.set_room_number_position(num) #actualiza su posición
        print(f"Player succesfully placed")
        
    def show_map(self): #mapa del piso
        self.current_floor.room_map()
        
    def representation_for_room__(self, cuadricule): #cómo se ve en el juego
        return "P"
    
    def representation_for_floor__(self, room): #cómo se ve en el juego
        # print("patata")
        return "P"
    
    def locate_player_in_room_in_cuadricule_num(self, room, num): #finaliza el pase de manos, pasando al jugador a la habitación que corresponda 
        pass
        
    def set_room_number_position(self, num): #setter de número de habitación del piso
        self.current_room_number = num
        
    def set_cuadricule_number_position(self, num): #setter de número de cuadrícula de habitación
        self.current_cuadricule_number = num

    def get_room_number_position(self): #getter número de habitación
        return self.current_room_number
    
    def set_screen(self, color):
        self.screen_color = color
        
    def reset_screen(self):
        self.screen_color = CLR_RST
    
    def show_screen(self): #muestra la pantalla (el mapa de la sala)
        self.current_room.map(self.screen_color)
        self.reset_screen()
        # if self.screen_color == "\033[91m":
        #     time.sleep(0.1)
        #     cls()
        #     self.reset_screen()
        #     self.show_screen()
        
        
        # print(self.weapon.base_damage())

    #movimientos del jugador

    def move_up(self):
        # self.current_room.move_player__to_next_room_up(self, self.current_floor)
        self.current_room.move_player__to_next_cuadricule_north()
        self.looking_at = North()
        self.show_screen()

    def move_left(self):
        # self.current_room.move_player__to_next_room_left(self, self.current_floor)
        self.current_room.move_player__to_next_cuadricule_west()
        self.looking_at = West()
        self.show_screen()
        # print(self.current_cuadricule_number)

    def move_down(self):
        # self.current_room.move_player__to_next_room_down(self, self.current_floor)
        self.current_room.move_player__to_next_cuadricule_south()
        self.looking_at = South()
        self.show_screen()

    def move_right(self):
        # self.current_room.move_player__to_next_room_right(self, self.current_floor)
        self.current_room.move_player__to_next_cuadricule_east()
        self.looking_at = East()
        self.show_screen()
        
    def move__to_next_room_north(self):
        self.current_floor.move_player__to_next_room_north(self)
        
    def move__to_next_room_west(self):
        self.current_floor.move_player__to_next_room_west(self)
        
    def move__to_next_room_south(self):
        self.current_floor.move_player__to_next_room_south(self)
        
    def move__to_next_room_east(self):
        self.current_floor.move_player__to_next_room_east(self)
        
    def move_to_next_floor(self):
        self.map.move_player__to_next_floor(self) #último pase de manos
        
    #================================================================ combat
    
    def take_damage(self, damage): #recibe daño
        current_hp = self.hp
        print(current_hp, damage)
        if damage < current_hp:
            self.hp -= damage
        else: #si no me queda vida, me muero aaaaaaaa
            raise Exception("Te cuesta")
    
    def damage_entity(self, entity):
        # print("te wa matar 2")
        self.weapon.damage_entity(entity)
        
    def take_damage_from(self, entity):
        # print(entity)
        red = "\033[91m"
        self.take_damage(entity.damage)
        print(self.hp)
        self.set_screen(red)