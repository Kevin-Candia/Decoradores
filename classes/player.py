# Game
from random import randrange
from classes.classes import ClassEnum
from equipment.armor import Equipment, EquipmentBase


# class Player():
class Player(EquipmentBase):

    experience  : int       = 1,
    class_      : ClassEnum = ClassEnum.Rookie
    armor       : dict[str, Equipment] = {}
    army        : dict[str, Equipment] = {}
    accesory    : dict[str, Equipment] = {}


    # def __init__(
    #     self,
    #     experience  : int               = 1,
    #     clas        : ClassEnum         = ClassEnum.Rookie,
    #     armor       : dict[Equipment]   = {},
    #     army        : dict[Equipment]   = {},
    #     accesory    : dict[Equipment]   = {}
    # ) -> None:
    #     super().__init__()
    #     self.experience = experience
    #     self.clas       = clas
    #     self.armor      = armor
    #     self.army       = army
    #     self.accesory   = accesory

    # @property
    # def get_experience(self) -> str:
    #     return self.name

    # @get_experience.setter
    # def set_experience(self, experience) -> None:
    #     self.experience = experience

    # def change_class(self, level, clas: ClassEnum):
    #     if level > ClassEnum.Rookie.value:
    #         self.clas = ClassEnum.Warrior
    #     elif level > ClassEnum.Warrior.value:
    #         self.clas = clas


    # def attack(self, enemy):
    #     attack = probability_of_critical()(enemy)


    # def probability_of_hit(self, enemy) -> bool:
    #     miss = self.player.get_hit < randrange(0, enemy.get_evasion)
    #     if miss:
    #         print("MISS!!")
    #     return miss


    # def probability_of_critical(self, enemy):
    #     enemy_probability_reduction_damage  = randrange(20, 101)
    #     player_probability_damage           = randrange(50, 101)

    #     if player_probability_damage > enemy_probability_reduction_damage:
    #         print("CRITICAL!!!")
    #         return calculate_damage(enemy)

    #     attack = self.player.get_attack_psl - enemy.get_defense_psl

    #     if attack < 0:
    #         attack = 0


    #     def calculate_damage(self, enemy):
    #         damage          = randrange(1, self.player.get_psl_dmg)
    #         damage_reduce   = randrange(1, enemy.rdc_psl_dmg)
    #         base            = round(self.player.get_attack_psl * ((damage / 100) + 1))
    #         reduce          = round(enemy.get_defense_psl * ((damage_reduce / 100) + 1))
    #         attack = base - reduce
    #         if attack < 0:
    #             attack = 0
    #         return attack

    #     return self.player.get_attack_psl - enemy.get_defense_psl

    # def attack_pisitive(attack: int, defense: int):
    #     attack = attack - defense
    #     if attack < 0:
    #         attack = 0
    #     return attack

    def attack(self, type: bool):
        def calculate_damage_per_critical(enemy: Player):
            enemy_probability_reduction_damage  = randrange(20, 101)
            player_probability_damage           = randrange(self.player.pbt_psl_dmg, 101)

            if enemy_probability_reduction_damage > 100 or player_probability_damage > 100:
                enemy_probability_reduction_damage = 100
                player_probability_damage = 100

            attack = self.player.get_attack_psl - enemy.get_defense_psl

            if attack < 0:
                attack = 0

            if player_probability_damage > enemy_probability_reduction_damage:
                print("CRITICAL!!!")
                damage          = randrange(1, self.player.get_psl_dmg)
                damage_reduce   = randrange(1, enemy.rdc_psl_dmg)
                base            = round(self.player.get_attack_psl * ((damage / 100) + 1))
                reduce          = round(enemy.get_defense_psl * ((damage_reduce / 100) + 1))
                attack          = base - reduce
                if attack < 0:
                    attack = 0
            return attack
        return calculate_damage_per_critical


    def put_on_armor(self, armor: Equipment):
        if not self.armor.get(armor.type.name):
            self.armor.setdefault(armor.type.name, armor)
        else:
            print('*'*10, "Can't equip, exceeds limit", '*'*10 )


    def put_on_army(self, army: Equipment):
        if not self.armor.get(army.type.name):
            self.armor.setdefault(army.type.name, army)
        else:
            print('*'*10, "Can't equip, exceeds limit", '*'*10 )


    def put_on_accesory(self, accesory: Equipment):
        if not self.accesory.get(accesory.type.name):
            self.accesory.setdefault(accesory.type.name, accesory)
        else:
            print('*'*10, "Can't equip, exceeds limit", '*'*10 )