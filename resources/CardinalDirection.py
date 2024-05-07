from abc import ABC, abstractclassmethod

class CardinalDirection(ABC):
    def __init__(self):
        pass
    
    @abstractclassmethod
    def place_player_in_room(self, room): #reenvía a la habitación a colocar al jugador en el número de cuadrícula que diga la dirección cardinal
        pass
    
    @abstractclassmethod
    def cardinal_cuadricule_number(self): #el número de cuadrícula
        pass
    
    @abstractclassmethod
    def move_player__to_next_room_from_room(self, room):
        pass
    
class North(CardinalDirection):
    def __init__(self):
        pass

    def place_player_in_room(self, room):
        room.locate_player_in_cuadricule_num(self.cardinal_cuadricule_number()) #4 es la puerta del norte 0 1 2 3 4 5   6  7 8 9 10 11 12
        
    def cardinal_cuadricule_number(self):
        return 19

    def move_player__to_next_room_from_room(self, room):
        room.move_player__to_next_room_north()


class West(CardinalDirection):
    def __init__(self):
        pass
    
    def place_player_in_room(self, room):
        room.locate_player_in_cuadricule_num(self.cardinal_cuadricule_number()) 

    def cardinal_cuadricule_number(self):
        return 53
    
    def move_player__to_next_room_from_room(self, room):
        room.move_player__to_next_room_west()
    
class South(CardinalDirection):
    def __init__(self):
        pass
    
    def place_player_in_room(self, room):
        room.locate_player_in_cuadricule_num(self.cardinal_cuadricule_number()) 

    def cardinal_cuadricule_number(self):
        return 97
    
    def move_player__to_next_room_from_room(self, room):
        room.move_player__to_next_room_south()
    
class East(CardinalDirection):
    def __init__(self):
        pass
    
    def place_player_in_room(self, room):
        room.locate_player_in_cuadricule_num(self.cardinal_cuadricule_number()) 

    def cardinal_cuadricule_number(self):
        return 63
    
    def move_player__to_next_room_from_room(self, room):
        room.move_player__to_next_room_east()