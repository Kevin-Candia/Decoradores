# Pydantic
from pydantic import BaseModel, Field

# Game
from random import randrange
from classes.classes import ClassEnum
# from classes.player import Player


class Stats(BaseModel):

    # player = Player
    vit    = 0
    str    = 0
    will   = 0
    int    = 0
    agi    = 0


    def calculate_stats_player(self, clas : ClassEnum) -> None:
        # * Calculamos las stats por nivel y clase del jugador 
        for i in range(self.player.level):
            level_up(self)
            if i >= 5:
                self.player.change_class(i, ClassEnum.Warrior)
            elif i >= 15:
                self.player.change_class(i, clas)


        def level_up() -> None:
            if self.player.clas == ClassEnum.Warrior:
                stats((1, 3), (1, 3), (1, 3) ,(1, 3) ,(1, 3))
            elif self.player.clas == ClassEnum.Berserker:
                stats((2, 3), (2, 5), (1, 3) ,(0, 1) ,(1, 2))
            elif self.player.clas == ClassEnum.Killer:
                stats((1, 3), (1, 3), (2, 3) ,(0, 1) ,(3, 5))
            elif self.player.clas == ClassEnum.Paladin:
                stats((3, 5), (2, 3), (2, 3) ,(0, 2) ,(0, 2))
            elif self.player.clas == ClassEnum.Wizard:
                stats((2, 4), (0, 2), (2, 3) ,(3, 5) ,(0, 1))
            elif self.player.clas == ClassEnum.Necromancer:
                stats((1, 3), (0, 1), (3, 5) ,(2, 3) ,(3, 4))
            else:
                stats((0, 1), (0, 1), (0, 1) ,(0, 1) ,(0, 1))

        def stats(vit_tuple: tuple, str_tuple: tuple, will_tuple: tuple, int_tuple: tuple, agi_tuple: tuple) -> None:
            self.vit    = self.vit  + randrange(vit_tuple[0]    , vit_tuple[1])
            self.str    = self.str  + randrange(str_tuple[0]    , str_tuple[1])
            self.will   = self.will + randrange(will_tuple[0]   , will_tuple[1])
            self.int    = self.int  + randrange(int_tuple[0]    , int_tuple[1])
            self.agi    = self.agi  + randrange(agi_tuple[0]    , agi_tuple[1])