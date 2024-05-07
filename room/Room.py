
from room.RoomObjects import Air
from abc import ABC, abstractclassmethod
from entities.Player import Player
from entities.GeneralEntities import Box
from room.Cuadricule import Cuadricule
from resources.NoObjects import NoPlayer
from resources.CardinalDirection import CardinalDirection, South
# from resources.Exceptions import ImpossibleMovement
from room.RoomObjects import *

class Room(ABC): #habitación
    def __init__(self):
        self.player = NoPlayer()
        self.inside_cuadricules = self.default_cuadricules()

    @abstractclassmethod
    def default_cuadricules(self):
        pass

    @abstractclassmethod
    def player_enter_with_num_from_cardinal(self, player: Player): #el jugador entra a la sala y se registra
        pass
    
    def map_representation(self):
        return self.player.representation_for_floor__(self)

     #le paso la mano al jugador para que se mueva al otro piso

    @abstractclassmethod
    def move_player__to_next_room_north(self, player: Player): #subclass resp
        pass

    @abstractclassmethod
    def move_player__to_next_room_west(self, player: Player): #subclass resp
        pass

    @abstractclassmethod
    def move_player__to_next_room_south(self, player: Player): #subclass resp
        pass

    @abstractclassmethod
    def move_player__to_next_room_east(self, player: Player): #subclass resp
        pass
    
    def player_damage(self, entity):
        # print("te wa matar")
        self.player.damage_entity(entity)
        
    def damage_player(self, entity):
        # print("te wa matar")
        self.player.take_damage_from(entity)


class BaseRoom(Room, ABC): #habitación predeterminada
    
    @abstractclassmethod
    def default_cuadricules(self):
        # north_door = Cuadricule(Door(North()))
        # west_door = Cuadricule(Door(West()))
        # south_door = Cuadricule(Door(South()))
        # east_door = Cuadricule(Door(East()))
        
        # inside_cuadricules = [ #habitación por dentro
        #             Cuadricule(Wall()), Cuadricule(Wall()),  Cuadricule(Wall()),  Cuadricule(Wall()),  Cuadricule(Wall()),  Cuadricule(Wall()),  north_door     ,  Cuadricule(Wall()),  Cuadricule(Wall()), Cuadricule(Wall()), Cuadricule(Wall()), Cuadricule(Wall()),  Cuadricule(Wall()),   
        #             Cuadricule(Wall()), Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),  Cuadricule(Air()),  Cuadricule(Air()),  Cuadricule(Air()),   Cuadricule(Wall()), 
        #             Cuadricule(Wall()), Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),  Cuadricule(Air()),  Cuadricule(Air()),  Cuadricule(Air()),   Cuadricule(Wall()),  
        #             Cuadricule(Wall()), Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),  Cuadricule(Air()),  Cuadricule(Air()),  Cuadricule(Air()),   Cuadricule(Wall()), 
        #                      west_door, Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),  Cuadricule(Air()),  Cuadricule(Air()),  Cuadricule(Air()),   east_door         , 
        #             Cuadricule(Wall()), Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),  Cuadricule(Air()),  Cuadricule(Air()),  Cuadricule(Air()),   Cuadricule(Wall()),   
        #             Cuadricule(Wall()), Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),  Cuadricule(Air()),  Cuadricule(Air()),  Cuadricule(Air()),   Cuadricule(Wall()),   
        #             Cuadricule(Wall()), Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),  Cuadricule(Air()),  Cuadricule(Air()),  Cuadricule(Air()),   Cuadricule(Wall()),   
        #             Cuadricule(Wall()), Cuadricule(Wall()),  Cuadricule(Wall()),  Cuadricule(Wall()),  Cuadricule(Wall()),  Cuadricule(Wall()),  south_door       ,  Cuadricule(Wall()),  Cuadricule(Wall()), Cuadricule(Wall()), Cuadricule(Wall()), Cuadricule(Wall()),   Cuadricule(Wall()),   
        #            ]
        
        # return inside_cuadricules
        pass
    
    @abstractclassmethod
    def __repr__(self): #para cambiar cómo se ve en el mapa
        # return "■"
        pass
    
    # @abstractclassmethod
    # def map_representation(self): #para cambiar cómo se ve en el mapa
    #     self.player.representation_for_floor__(self)
    
    def map(self): #para el mapping de la sala
        current_cuadricule = 0
        cuadricule_lines = 9
        for cuadricule in range(cuadricule_lines):
            self.map_line(current_cuadricule)
            current_cuadricule += 13

    def map_line(self, current_cuadricule: int): #para cada línea del mapping
        final_line = ""
        cuadricule_lines = 13
        for cuadricule in range(cuadricule_lines):
            final_line += f" {self.inside_cuadricules[current_cuadricule].map_representation()}"
            current_cuadricule += 1
        print(final_line)
    
    
    def set_player(self, player: Player): #setea al jugador para poder preguntar su representación en el mapa
        self.player = player
        
    def place_player_on_door(self, cardinal_direction: CardinalDirection): #ubica al jugador en alguna de las puertas
        # print(cardinal_direction)
        cardinal_direction.place_player_in_room(self)
    
    def player_enter_with_num_from_cardinal(self, player: Player, num: int, cardinal_direction: CardinalDirection): #el jugador entra a la sala y se registra
        print(f"Player succesfully enter")
        player.enter_room_num(self, num)
        self.set_player(player)
        # print(player, "TENGO JUGADOR")
        self.place_player_on_door(cardinal_direction)
        
    def locate_player_in_cuadricule_num(self, num: int): #pone al jugador en la cuadrícula del número dado de la lista de cuadrículas
        self.player_leave_current_cuadricule()
        self.inside_cuadricules[num].add_to_content(self.player)
        self.player.set_cuadricule_number_position(num)
        
    def player_leave_current_cuadricule(self):
        self.inside_cuadricules[self.player.current_cuadricule_number].restart_content_to_first() #saco al jugador de la cuadrícula previa
        
    def player_leave(self): #el jugador se "va" de la sala y queda NoJugador
        self.set_player(NoPlayer())
        
    def is_not_out_of_bounds_north(self, desired_next_cuadricule_num: int): #para que no se pueda mover de límites el jugador
        return desired_next_cuadricule_num >= 0
    
    def west_limits(self): #los límites de la izquierda
        return [-1, 12, 25, 38, 51, 64, 77, 90, 103] 
    
    def is_not_out_of_bounds_west(self, desired_next_cuadricule_num: int): #para saber si está o no en un punto donde no se pueda mover a la izquierda (y similar con el resto)
        return desired_next_cuadricule_num not in self.west_limits() 
    
    def is_not_out_of_bounds_south(self, desired_next_cuadricule_num: int):
        return desired_next_cuadricule_num < 117 
    
    def east_limits(self): #los límites de la derecha
        return [13, 26, 39, 52, 65, 78, 91, 104, 117] 
    
    def is_not_out_of_bounds_east(self, desired_next_cuadricule_num: int):
        return desired_next_cuadricule_num not in self.east_limits() 
     
    def move_player__to_next_cuadricule_north(self):
        desired_next_cuadricule_num = self.player.current_cuadricule_number - 13
        
        if self.is_not_out_of_bounds_north(desired_next_cuadricule_num):
            desired_cuadricule = self.inside_cuadricules[desired_next_cuadricule_num]
            desired_cuadricule.move_to_self_num_in_room_(self, desired_next_cuadricule_num)
            
        else:
            print("Out of bounds!")
    
    def move_player__to_next_cuadricule_west(self):
        desired_next_cuadricule_num = self.player.current_cuadricule_number - 1
        
        if self.is_not_out_of_bounds_west(desired_next_cuadricule_num):
            desired_cuadricule = self.inside_cuadricules[desired_next_cuadricule_num]
            desired_cuadricule.move_to_self_num_in_room_(self, desired_next_cuadricule_num)
            
        else:
            print("Out of bounds!")
    
    def move_player__to_next_cuadricule_south(self):
        desired_next_cuadricule_num = self.player.current_cuadricule_number + 13
        
        if self.is_not_out_of_bounds_south(desired_next_cuadricule_num):
            desired_cuadricule = self.inside_cuadricules[desired_next_cuadricule_num]
            desired_cuadricule.move_to_self_num_in_room_(self, desired_next_cuadricule_num)
            
        else:
            print("Out of bounds!")
    
    def move_player__to_next_cuadricule_east(self):
        desired_next_cuadricule_num = self.player.current_cuadricule_number + 1
        
        if self.is_not_out_of_bounds_east(desired_next_cuadricule_num):
            desired_cuadricule = self.inside_cuadricules[desired_next_cuadricule_num]
            desired_cuadricule.move_to_self_num_in_room_(self, desired_next_cuadricule_num)
            
        else:
            print("Out of bounds!")

    def move_player__to_next_room_north(self): #para mover al jugador arriba
        self.player.move__to_next_room_north()

    def move_player__to_next_room_west(self):
        self.player.move__to_next_room_west()
        #self.player_leave()

    def move_player__to_next_room_south(self):
        self.player.move__to_next_room_south()

    def move_player__to_next_room_east(self):
        self.player.move__to_next_room_east()
        #self.player_leave()
        
    def move_player__to_next_floor(self):
        self.player.move_to_next_floor()
        
    # def map_representation(self): #para cambiar cómo se ve en el mapa
    #     return "■"
    
        
class BossRoom_1_South(BaseRoom): #habitación de jefes
    
    def default_cuadricules(self):
        # north_door = Cuadricule(Door(North()))
        # west_door = Cuadricule(Door(West()))
        south_door = Cuadricule(Door(South()))
        # east_door = Cuadricule(Door(East()))
        
        inside_cuadricules = [ #habitación por dentro
                    Cuadricule(Wall()), Cuadricule(Wall()),  Cuadricule(Wall()),  Cuadricule(Wall()),  Cuadricule(Wall()),  Cuadricule(Wall()),  Cuadricule(Wall())  ,Cuadricule(Wall()),  Cuadricule(Wall()), Cuadricule(Wall()), Cuadricule(Wall()), Cuadricule(Wall()),  Cuadricule(Wall()),   
                    Cuadricule(Wall()), Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Trapdoor()),Cuadricule(Air()), Cuadricule(Air()),  Cuadricule(Air()),  Cuadricule(Air()),  Cuadricule(Air()),   Cuadricule(Wall()), 
                    Cuadricule(Wall()), Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),  Cuadricule(Air()),  Cuadricule(Air()),  Cuadricule(Air()),   Cuadricule(Wall()),  
                    Cuadricule(Wall()), Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),  Cuadricule(Air()),  Cuadricule(Air()),  Cuadricule(Air()),   Cuadricule(Wall()), 
                    Cuadricule(Wall()), Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Box()),   Cuadricule(Air()),   Cuadricule(Air()),  Cuadricule(Air()),  Cuadricule(Air()),  Cuadricule(Air()),   Cuadricule(Wall()), 
                    Cuadricule(Wall()), Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),  Cuadricule(Air()),  Cuadricule(Air()),  Cuadricule(Air()),   Cuadricule(Wall()),   
                    Cuadricule(Wall()), Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),  Cuadricule(Air()),  Cuadricule(Air()),  Cuadricule(Air()),   Cuadricule(Wall()),   
                    Cuadricule(Wall()), Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),   Cuadricule(Air()),  Cuadricule(Air()),  Cuadricule(Air()),  Cuadricule(Air()),   Cuadricule(Wall()),   
                    Cuadricule(Wall()), Cuadricule(Wall()),  Cuadricule(Wall()),  Cuadricule(Wall()),  Cuadricule(Wall()),  Cuadricule(Wall()),  south_door       ,  Cuadricule(Wall()),  Cuadricule(Wall()), Cuadricule(Wall()), Cuadricule(Wall()), Cuadricule(Wall()),   Cuadricule(Wall()),   
                   ]
        
        return inside_cuadricules
    
    def __repr__(self): #para cambiar cómo se ve en el mapa
        return "火"
    


class WallRoom(Room): #habitación inexistente
    
    def default_cuadricules(self):
        inside_cuadricules = [ Cuadricule(Wall()),  Cuadricule(Wall()), Cuadricule(Wall()), Cuadricule(Wall()), Cuadricule(Wall()), Cuadricule(Wall()), Cuadricule(Wall()), Cuadricule(Wall()), Cuadricule(Wall()), Cuadricule(Wall()), Cuadricule(Wall()), Cuadricule(Wall()), Cuadricule(Wall()),   
                                    Cuadricule(Wall()),  Cuadricule(Wall()), Cuadricule(Wall()), Cuadricule(Wall()), Cuadricule(Wall()), Cuadricule(Wall()), Cuadricule(Wall()), Cuadricule(Wall()), Cuadricule(Wall()), Cuadricule(Wall()), Cuadricule(Wall()), Cuadricule(Wall()), Cuadricule(Wall()), 
                                    Cuadricule(Wall()),  Cuadricule(Wall()), Cuadricule(Wall()), Cuadricule(Wall()), Cuadricule(Wall()), Cuadricule(Wall()), Cuadricule(Wall()), Cuadricule(Wall()), Cuadricule(Wall()), Cuadricule(Wall()), Cuadricule(Wall()), Cuadricule(Wall()), Cuadricule(Wall()),  
                                    Cuadricule(Wall()),  Cuadricule(Wall()), Cuadricule(Wall()), Cuadricule(Wall()), Cuadricule(Wall()), Cuadricule(Wall()), Cuadricule(Wall()), Cuadricule(Wall()), Cuadricule(Wall()), Cuadricule(Wall()), Cuadricule(Wall()), Cuadricule(Wall()), Cuadricule(Wall()), 
                                    Cuadricule(Wall()),  Cuadricule(Wall()), Cuadricule(Wall()), Cuadricule(Wall()), Cuadricule(Wall()), Cuadricule(Wall()), Cuadricule(Wall()), Cuadricule(Wall()), Cuadricule(Wall()), Cuadricule(Wall()), Cuadricule(Wall()), Cuadricule(Wall()), Cuadricule(Wall()), 
                                    Cuadricule(Wall()),  Cuadricule(Wall()), Cuadricule(Wall()), Cuadricule(Wall()), Cuadricule(Wall()), Cuadricule(Wall()), Cuadricule(Wall()), Cuadricule(Wall()), Cuadricule(Wall()), Cuadricule(Wall()), Cuadricule(Wall()), Cuadricule(Wall()), Cuadricule(Wall()),   
                                    Cuadricule(Wall()),  Cuadricule(Wall()), Cuadricule(Wall()), Cuadricule(Wall()), Cuadricule(Wall()), Cuadricule(Wall()), Cuadricule(Wall()), Cuadricule(Wall()), Cuadricule(Wall()), Cuadricule(Wall()), Cuadricule(Wall()), Cuadricule(Wall()), Cuadricule(Wall()),   
                                    Cuadricule(Wall()),  Cuadricule(Wall()), Cuadricule(Wall()), Cuadricule(Wall()), Cuadricule(Wall()), Cuadricule(Wall()), Cuadricule(Wall()), Cuadricule(Wall()), Cuadricule(Wall()), Cuadricule(Wall()), Cuadricule(Wall()), Cuadricule(Wall()), Cuadricule(Wall()),   
                                    Cuadricule(Wall()),  Cuadricule(Wall()), Cuadricule(Wall()), Cuadricule(Wall()), Cuadricule(Wall()), Cuadricule(Wall()), Cuadricule(Wall()), Cuadricule(Wall()), Cuadricule(Wall()), Cuadricule(Wall()), Cuadricule(Wall()), Cuadricule(Wall()), Cuadricule(Wall()),]
        
        return inside_cuadricules
    
    def player_enter_with_num_from_cardinal(self, player: Player, num: int, cardinal_direction: CardinalDirection): #el jugador entra a la sala y se registra
        print("You can't enter a wall!")
    
    def __repr__(self): 
        return "▓"
    

    def move_player__to_next_room_north(self, player, current_floor): #para mover al jugador arriba, pero no lo hace porque no es una habitación (yo que sé, una pared)
        print("There's no room above!")

    def move_player__to_next_room_west(self, player, current_floor):
        print("There's no room to the left!")

    def move_player__to_next_room_south(self, player, current_floor):
        print("There's no room down!")

    def move_player__to_next_room_east(self, player, current_floor):
        print("There's no room to the right!")