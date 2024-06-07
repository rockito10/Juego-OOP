from entities.GeneralEntities import Entity
from abc import abstractmethod

class DamagefulEntity(Entity):
    
    @abstractmethod
    def base_damage(self):
        pass

    @abstractmethod
    def base_hp(self):
        pass
    
    @abstractmethod
    def representation_for_room__(self, cuadricule): #Cómo se ve
        pass
    
    def locate_player_in_room_in_cuadricule_num(self, room, num): #finaliza el pase de manos
        room.player_damage(self)
        room.damage_player(self)


class SpikeBox(DamagefulEntity):
    
    def turn(self):
        pass

    def base_hp(self):
        return 25
    
    def base_damage(self):
        return 10

    def representation_for_room__(self, cuadricule): #Cómo se ve
        return "四"

    # def locate_player_in_room_in_cuadricule_num(self, room, num): #finaliza el pase de manos

    #     room.player_damage(self)
    #     room.damage_player(self)
        
        
class Crab(Entity):
    def base_damage(self):
        return 10

    def base_hp(self):
        return 30
    
    def turn(self): #emula el movimiento de la entidad
        if self.total_move > 3:
            self.move_right()
            self.total_move += 1
            
        self.move_left()
        self.total_move += 1
        
        if self.total_move > 6:
            self.total_move = 0
        

    def representation_for_room__(self, cuadricule): #Cómo se ve
        return "雨"