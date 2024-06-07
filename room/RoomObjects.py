#Objetos dentro de la habitación (en el sentido literal)
from abc import abstractmethod
from resources import CardinalDirection

class RoomObject():
    
    def turn(self):
        pass
    
    def set_cuadricule(self, cuadricule): #la mayoría no debería usarlo, esto es para las entidades
        pass

    @abstractmethod
    def representation_for_room__(self, cuadricule): #Cómo se ve
        pass
    
    @abstractmethod
    def locate_player_in_room_in_cuadricule_num(self, room, num): #finaliza el pase de manos
        pass


class Door(RoomObject):
    
    def __init__(self, cardinalDirection: CardinalDirection): #seteo a qué habitación mira
        self.cardinalDirection = cardinalDirection

    def representation_for_room__(self, cuadricule): #Cómo se ve
        return "▯"
    
    def locate_player_in_room_in_cuadricule_num(self, room, num): #finaliza el pase de manos, pasando al jugador a la habitación que corresponda 
        # print(self.cardinalDirection)
        self.cardinalDirection.move_player__to_next_room_from_room(room)
    
class Air(RoomObject): #nada

    def representation_for_room__(self, cuadricule): #Cómo se ve
        return "▢"
    
    def locate_player_in_room_in_cuadricule_num(self, room, num): #finaliza el pase de manos
        room.locate_player_in_cuadricule_num(num)
    
    
class Wall(RoomObject): #objeto al que no se puede entrar bajo ningún concepto

    def representation_for_room__(self, cuadricule): #Cómo se ve
        return "▓"
    
    def locate_player_in_room_in_cuadricule_num(self, room, num): #finaliza el pase de manos
        print("Cant enter a wall!") 
        
        
class Trapdoor(RoomObject):

    def representation_for_room__(self, cuadricule): #Cómo se ve
        return "毎"
    
    def locate_player_in_room_in_cuadricule_num(self, room, num): #finaliza el pase de manos, pasando al jugador a la habitación que corresponda 
        room.move_player__to_next_floor()