from room.RegularRooms import *
from room.Room import WallRoom, BossRoom_1_South
from entities.Player import Player
from resources.CardinalDirection import North, West, South, East, CardinalDirection
from abc import ABC, abstractclassmethod


class Floor(ABC): #piso
    def __init__(self):
     self.rooms = self.default_rooms()

    @abstractclassmethod
    def default_rooms(self):
        # return [ WallRoom(), WallRoom(), WallRoom(), WallRoom(), WallRoom(),
        #             WallRoom(), WallRoom(), WallRoom(), WallRoom(), WallRoom(),
        #             WallRoom(), WallRoom(), WallRoom(), WallRoom(), WallRoom(), #concepto de piso
        #             WallRoom(), WallRoom(), WallRoom(), WallRoom(), WallRoom(),
        #             WallRoom(), WallRoom(), WallRoom(), WallRoom(), WallRoom(),
        #            ]
        pass
     
    @abstractclassmethod
    def cardinal_starting_direction(self):
        # return South()
        pass

    @abstractclassmethod
    def cuadricule_starting_point(self):
        # return 23
        pass
     
    def put_player(self, player: Player):
        print(f"Putting player in room 24")
        self.in_room_num_locate_player_from_cardinal(self.cuadricule_starting_point(), player, self.cardinal_starting_direction()) #entra el jugador a la habitación 24 (0 -> 24)
        player.enter_floor(self)
     
    def room_map(self): #mapea todas las líneas de las habitaciones
        current_room_pointer = 0
        for line in range(5):
            line_to_map = self.room_line_map(current_room_pointer)
            print(line_to_map)
            current_room_pointer = current_room_pointer + 5

    def room_line_map(self, current_room_pointer): #crea una línea de habitaciones para mostrar
        room_to_map = []
        room_lines = 5
        for room in range(room_lines):
            room_to_map += [self.rooms[current_room_pointer].map_representation()]
            # print(self.rooms[current_room_pointer].map_representation())
            current_room_pointer += 1
        return(room_to_map)
        
    # @abstractclassmethod
    # def put_player(self):
    #     #self.rooms[num].playerEnter(player) #entra el jugador a la habitación 24 (0 -> 24)
    #     pass

    def in_room_num_locate_player_from_cardinal(self, num: int, player: Player, cardinal: CardinalDirection): #actualiza la posición del jugador y lo posiciona en la habitación deseada
        print(cardinal.cardinal_cuadricule_number())
        self.rooms[num].player_enter_with_num_from_cardinal(player, num, cardinal)
        
    def is_not_out_of_bounds_north(self, desired_position):
        return desired_position >= 0
    
    def left_limits(self):
        return [-1, 4, 9, 14, 19]
    
    def is_not_out_of_bounds_west(self, desired_position): #me fijo que no se salga del rango
        return desired_position not in self.left_limits()

    def is_not_out_of_bounds_south(self, desired_position):
        return desired_position < 25
    
    def right_limits(self):
        return [5, 10, 15, 20, 25]
    
    def is_not_out_of_bounds_east(self, desired_position):
        return desired_position not in self.right_limits() 

    def move_player__to_next_room_north(self, player): #para mover al jugador arriba

        desired_position = player.get_room_number_position() - 5

        if self.is_not_out_of_bounds_north(desired_position):
            self.in_room_num_locate_player_from_cardinal(desired_position, player, South()) #lo ubica en el sur, porque viene del norte
        else:
            print("Out of bounds!")

    def move_player__to_next_room_west(self, player): #para mover al jugador a la izquierda (resta 1, y no puede estar en un borde izquierdo)

        desired_position = player.get_room_number_position() - 1

        if self.is_not_out_of_bounds_west(desired_position): #números fuera del borde
            
            self.in_room_num_locate_player_from_cardinal(desired_position, player, East()) #lo ubica en el este, porque viene del oeste
        else:
            print("Out of bounds!")
        
    def move_player__to_next_room_south(self, player): #para mover al jugador abajo

        desired_position = player.get_room_number_position() + 5

        if self.is_not_out_of_bounds_south(desired_position):
            self.in_room_num_locate_player_from_cardinal(desired_position, player, North()) #lo ubica en el norte, porque viene del sur
        else:
            print("Out of bounds!")
    
    def move_player__to_next_room_east(self, player): #para mover al jugador arriba

        desired_position = player.get_room_number_position() + 1

        if self.is_not_out_of_bounds_east(desired_position):
            self.in_room_num_locate_player_from_cardinal(desired_position, player, West()) #lo ubica en el oeste, porque viene del este
        else:
            print("Out of bounds!")
            
    

class DefaultFloor(Floor): #piso predeterminado
    # def __init__(self):
    #     self.rooms = [
    #                 BossRoom(), WallRoom(),     WallRoom(),    WallRoom(),    WallRoom(),
    #                 DefaultRoom(), WallRoom(),     WallRoom(),    WallRoom(),    WallRoom(),
    #                 DefaultRoom(), WallRoom(),     WallRoom(),    WallRoom(),    WallRoom(), #un piso
    #                 DefaultRoom(), DefaultRoom(),  DefaultRoom(), DefaultRoom(), WallRoom(),
    #                 WallRoom(),    WallRoom(),     WallRoom(),    DefaultRoom(), WallRoom(),
    #                ]
        
    def default_rooms(self):
        return [
                    BossRoom_1_South(), WallRoom(),     WallRoom(),    WallRoom(),    WallRoom(),
                    DefaultRoom(), WallRoom(),     WallRoom(),    WallRoom(),    WallRoom(),
                    DefaultRoom(), WallRoom(),     WallRoom(),    WallRoom(),    WallRoom(), #un piso
                    DefaultRoom(), DefaultRoom(),  DefaultRoom(), Room_1(), WallRoom(),
                    WallRoom(),    WallRoom(),     WallRoom(),    DefaultRoom(), WallRoom(),
                   ]
        
    def cardinal_starting_direction(self):
        return South()

    def cuadricule_starting_point(self):
        return 23
    
    
class Manual_Floor_1(Floor):
    
    def default_rooms(self):
        return [
                    DefaultRoom(), BossRoom_1_South(),     WallRoom(),    WallRoom(),    WallRoom(),
                    DefaultRoom(), WallRoom(),     WallRoom(),    DefaultRoom(), WallRoom(),
                    DefaultRoom(), DefaultRoom(),  WallRoom(),    DefaultRoom(), WallRoom(), #un piso
                    WallRoom(),    DefaultRoom(),  DefaultRoom(), Room_1(), DefaultRoom(),
                    WallRoom(),    WallRoom(),     WallRoom(),    DefaultRoom(), WallRoom(),
                   ]
        
    def cardinal_starting_direction(self):
        return South()

    def cuadricule_starting_point(self):
        return 23
    
    
        
        
# class EmptyFloor(Floor): #piso vacío (todas habitaciones regulares)
#     def __init__(self):
#         self.rooms = [
#                     DefaultRoom(), DefaultRoom(), DefaultRoom(), DefaultRoom(), DefaultRoom(),
#                     DefaultRoom(), DefaultRoom(), DefaultRoom(), DefaultRoom(), DefaultRoom(),
#                     DefaultRoom(), DefaultRoom(), DefaultRoom(), DefaultRoom(), DefaultRoom(), #un piso
#                     DefaultRoom(), DefaultRoom(), DefaultRoom(), DefaultRoom(), DefaultRoom(),
#                     DefaultRoom(), DefaultRoom(), DefaultRoom(), DefaultRoom(), DefaultRoom(),
#                    ]

#     def put_player(self, player: Player):
#         print(f"Putting player in room 25")
#         self.in_room_num_locate_player_from_cardinal(24, player, South()) #entra el jugador a la habitación 24 (0 -> 24)
#         player.enter_floor(self)