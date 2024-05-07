from abc import ABC, abstractclassmethod
from room.RoomObjects import RoomObject

class Entity(RoomObject, ABC): 
    #hereda de RoomObject cómo funcionar en caso que lo pisen y cómo se ve
    def __init__(self): #necesita la cuadrícula para hacerse daño y destruirse
        self.hp = self.base_hp()
        self.current_cuadricule = None
        self.damage = self.base_damage()
        
    def set_cuadricule(self, cuadricule): #pone la cuadrícula
        self.current_cuadricule = cuadricule
        
    @abstractclassmethod
    def base_hp(self):
        pass
    
    def base_damage(self):
        return 0
    
    def take_damage(self, damage): #recibe daño
        current_hp = self.hp
        # print(current_hp, damage)
        if damage < current_hp:
            self.hp -= damage
        else: #si no me queda vida, me muero aaaaaaaa
            self.current_cuadricule.destroy_content()

class Box(Entity):
    def base_hp(self):
        return 100
    
    def representation_for_room__(self, cuadricule): #Cómo se ve
        return "囗"
    
    def locate_player_in_room_in_cuadricule_num(self, room, num): #finaliza el pase de manos
        # print("WAITTTTTTTTTTT")
        room.player_damage(self)
        
class SpikeBox(Entity):
    
    def base_damage(self):
        return 10
    
    def base_hp(self):
        return 25
    
    def representation_for_room__(self, cuadricule): #Cómo se ve
        return "四"
    
    def locate_player_in_room_in_cuadricule_num(self, room, num): #finaliza el pase de manos
        
        room.player_damage(self)
        room.damage_player(self)