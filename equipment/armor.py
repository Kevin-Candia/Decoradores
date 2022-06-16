import enum
from base import Base_Game
from stats.player_stats import Player_Stats


class EquipmentColor(enum.Enum):
    White   = 1
    Green   = 2
    Blue    = 3
    Orange  = 4
    Golden  = 5
    Divine  = 6


class EquipmentType(enum.Enum):
    Head        = "Head"
    Body        = "Body"
    Leg         = "Leg"
    Glove       = "Glove"
    Boot        = "Boot"
    Army        = "Army"
    Shield      = "Shield"
    SecondArmy  = "SecondArmy"
    Accessory   = "Accessory"
    Layer       = "Layer"


class Skill_Armor(Base_Game):
    description : str = ''


class EquipmentBase(Base_Game, Player_Stats):
    pass


class Equipment(EquipmentBase):

    type        : EquipmentType             # Tipo de arma ej: Casco, armadura, Polainas, Arma, escudo
    color       : EquipmentColor = EquipmentColor.White   # Color que tiene el arma ej: Blanco, Verde, Azul, Naranja, Dorado, Purpura, Rojo,  
    durability  : float = 100
    fortify     : int   = 0
    comment     : str   = ''
    stones      : list  = []