from datetime import datetime
from http.client import FORBIDDEN
from random import choice, randrange
from classes.classes import ClassEnum

from classes.player import Player
from equipment.armor import EquipmentColor, EquipmentType, Equipment


def execution_time(func):
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        print(f"Tiempo jugado: {(final_time - initial_time).total_seconds()}")
    return wrapper


def status__(vit: int, str: int, will: int, int: int, agi: int) -> tuple:
    def repeater(vit_: int, str_: int, will_: int, int_: int, agi_: int) -> tuple:
        return round(vit / vit_), round(str / str_), round(will / will_), round(int / int_), round(agi / agi_)
    return repeater


def start_player_game(status_player: list, status_enemy: list):
    return ["Player", "Enemy", status_player[9], status_player, status_enemy]


def next_player_game(status_player: list, status_enemy: list):
    return ["Enemy", "Player", status_enemy[9], status_enemy, status_player]


def game(func):
    def attack(player: dict[str, dict[str, int]], player_enemy: dict[str, dict[str, int]]) -> int:
        print("*" * 20, "STATUS PLAYER", "*" * 20)
        status_player = calculate_status_player(player)

        print("*" * 20, "STATUS ENEMY", "*" * 20)
        status_enemy = calculate_status_player(player_enemy)

        turns           = 0
        player_start    = ["Player", "Enemy"]
        start           = choice(player_start)
        print("***START ATTACK:", start)

        func(player, player_enemy)

        start_player    = start_player_game(status_player, status_enemy)
        next_player     = next_player_game(status_player, status_enemy)

        if start == "Enemy":
            start_player    = next_player_game(status_player, status_enemy)
            next_player     = start_player_game(status_player, status_enemy)

        life_player = start_player[2]
        life_enemy  = next_player[2]

        while True:
            print("-" * 50)
            print(f"{start_player[0]} LIFE", life_player)
            print(f"{next_player[0]} LIFE", life_enemy)

            life_enemy, critical_player = turn(start_player[0], start_player[1], life_enemy, start_player[3], start_player[4])

            if critical_player:
                print(f"CRITICAL {start_player[0]}!!")

            if life_enemy <= 0:
                turns += 1
                print(f"---{start_player[1]} is dead---")
                break

            life_player, critical_enemy = turn(next_player[0], next_player[1], life_player, next_player[3], next_player[4])
            if critical_enemy:
                print(f"CRITICAL {next_player[0]}!!")

            if life_player <= 0:
                turns += 1
                print(f"---{next_player[1]} is dead---")
                break

            turns += 1
        print("*" * 20, "END BATTLE", "*" * 20)
        print("CANTIDAD DE TURNOS:", turns)
        if life_player <= 0:
            print(f"***{next_player[0]} WIN***")
        elif life_enemy <= 0:
            print(f"***{start_player[0]} WIN***")
        return 0
    return attack


def turn(start_player: str, next_player: str, life: int, status_player: list, status_enemy: list):
    critical = False

    if probability_of_hit(status_player[13])(status_enemy[11]):
        return life, critical

    if status_player[14] >= randrange(1, 100):
        damage = randrange(1, status_player[12])
        base = round(status_player[7] * ((damage / 100) + 1))
        critical = True
    else:
        base = status_player[7]

    golpe =  base - status_enemy[5]

    if golpe < 0:
        golpe = 0

    print(start_player, " -> ", next_player, ": ", golpe)

    life -= golpe

    return life, critical


def probability_of_hit(hit) -> bool:
    def attack(rival_eva: int) -> bool:
        miss = hit < randrange(0, rival_eva)
        if miss:
            print("MISS!!")
        return miss
    return attack


def bonus_status(bonus: int, dict_players: dict[str, dict[str, int]]) -> int:
    return sum([[*v.values()][bonus] for v in dict_players.values() if type(v) is dict ])


def calculate_status_player(dict_players: dict[str, dict[str, int]]):
    bonus = []
    for i in range(0, 15):
        bonus.append(bonus_status(i, dict_players))

    final_status: tuple = status__(bonus[0], bonus[1], bonus[2], bonus[3], bonus[4])(4, 3, 2, 3, 4)

    list_bonus = [0, 2, 1, 3, 0, 2, 4]
    add_bonus = [10, 11, 20, 13, 13, 14, 1]

    for i in range(0, 7):
        bonus[i + 5] = round(bonus[i + 5] + final_status[list_bonus[i]] * add_bonus[i])

    print("VIT:", bonus[0])
    print("STR:", bonus[1])
    print("WILL:", bonus[2])
    print("INT:", bonus[3])
    print("AGI:", bonus[4])
    print("DEFENSE BASE", bonus[5])
    print("DEFENSE_MAGIC:", bonus[6])
    print("ATTACK:", bonus[7])
    print("ATTACK_MAGIC:", bonus[8])
    print("HP:", bonus[9])
    print("MP:", bonus[10])
    print("EVA:", bonus[11])
    print("DAÑO:", bonus[12])
    print("GOLPE:", bonus[13])
    print("PROB:", bonus[14])
    print(bonus)
    return bonus

@execution_time
@game
def start_game(player: dict[str, dict[str, int]], enemy: dict[str, dict[str, int]]):
    print("*" * 20, "START BATTLE", "*" * 20)


def run():
    player = {
        "level"         : 1,
        "casco"         : {
            "vit"           : 10,
            "str"           : 20,
            "will"          : 0,
            "int"           : 0,
            "agi"           : 10,
            "defense"       : 230,
            "defense_magic" : 120,
            "attack"        : 0,
            "attack_magic"  : 0,
            "hp"            : 144,
            "mp"            : 0,
            "eva"           : 130,
            "daño"          : 4,
            "golpe"         : 6,
            "probabilidad"  : 1,
        },
        "peto"          : {
            "vit"           : 20,
            "str"           : 12,
            "will"          : 5,
            "int"           : 0,
            "agi"           : 2,
            "defense"       : 250,
            "defense_magic" : 200,
            "attack"        : 0,
            "attack_magic"  : 0,
            "hp"            : 250,
            "mp"            : 0,
            "eva"           : 20,
            "daño"          : 2,
            "golpe"         : 1,
            "probabilidad"  : 4,
        }, 
        "polainas"      : {
            "vit"           : 15, 
            "str"           : 0, 
            "will"          : 0, 
            "int"           : 0, 
            "agi"           : 5,
            "defense"       : 100,
            "defense_magic" : 120,
            "attack"        : 0,      
            "attack_magic"  : 0,
            "hp"            : 180,
            "mp"            : 0,
            "eva"           : 10,
            "daño"          : 2,
            "golpe"         : 3,
            "probabilidad"  : 1,
        }, 
        "botas"         : {
            "vit"           : 10, 
            "str"           : 0, 
            "will"          : 5, 
            "int"           : 10, 
            "agi"           : 30,
            "defense"       : 40,
            "defense_magic" : 10,
            "attack"        : 0,      
            "attack_magic"  : 0,
            "hp"            : 400,
            "mp"            : 0,
            "eva"           : 10,
            "daño"          : 1,
            "golpe"         : 3,
            "probabilidad"  : 5,
        }, 
        "guantes"       : {
            "vit"           : 10, 
            "str"           : 2, 
            "will"          : 5, 
            "int"           : 0, 
            "agi"           : 3,
            "defense"       : 50,
            "defense_magic" : 20,
            "attack"        : 0,      
            "attack_magic"  : 0,
            "hp"            : 249,
            "mp"            : 0,
            "eva"           : 10,
            "daño"          : 5,
            "golpe"         : 1,
            "probabilidad"  : 0,
        },
        "arma"          : {
            "vit"           : 50, 
            "str"           : 40, 
            "will"          : 20, 
            "int"           : 0, 
            "agi"           : 10,
            "defense"       : 0,
            "defense_magic" : 0,
            "attack"        : 1000,      
            "attack_magic"  : 500,
            "hp"            : 144,
            "mp"            : 0,
            "eva"           : 10,
            "daño"          : 1,
            "golpe"         : 8,
            "probabilidad"  : 4,
        },
        "escudo"        : {
            "vit"           : 100, 
            "str"           : 100, 
            "will"          : 40, 
            "int"           : 0, 
            "agi"           : 10,
            "defense"       : 600,
            "defense_magic" : 450,
            "attack"        : 0,      
            "attack_magic"  : 0,
            "hp"            : 500,
            "mp"            : 230,
            "eva"           : 0,
            "daño"          : 1,
            "golpe"         : 1,
            "probabilidad"  : 1,
        }
    }

    enemy = {
        "level"         : 1,
        "casco"         : {
            "vit"           : 10, 
            "str"           : 20, 
            "will"          : 0, 
            "int"           : 0, 
            "agi"           : 10,
            "defense"       : 230,
            "defense_magic" : 120,
            "attack"        : 0,      
            "attack_magic"  : 0,
            "hp"            : 190,
            "mp"            : 0,
            "eva"           : 1,
            "daño"          : 53,
            "golpe"         : 20,
            "probabilidad"  : 1,
        }, 
        "peto"          : {
            "vit"           : 20, 
            "str"           : 12, 
            "will"          : 5, 
            "int"           : 0, 
            "agi"           : 2,
            "defense"       : 250,
            "defense_magic" : 200,
            "attack"        : 0,
            "attack_magic"  : 0,
            "hp"            : 240,
            "mp"            : 0,
            "eva"           : 2,
            "daño"          : 53,
            "golpe"         : 20,
            "probabilidad"  : 1,
        }, 
        "polainas"      : {
            "vit"           : 15, 
            "str"           : 0, 
            "will"          : 0, 
            "int"           : 0, 
            "agi"           : 5,
            "defense"       : 100,
            "defense_magic" : 120,
            "attack"        : 0,      
            "attack_magic"  : 0,
            "hp"            : 190,
            "mp"            : 0,
            "eva"           : 1,
            "daño"          : 53,
            "golpe"         : 20,
            "probabilidad"  : 1,
        }, 
        "botas"         : {
            "vit"           : 10, 
            "str"           : 0, 
            "will"          : 5, 
            "int"           : 10, 
            "agi"           : 30,
            "defense"       : 40,
            "defense_magic" : 10,
            "attack"        : 0,      
            "attack_magic"  : 0,
            "hp"            : 80,
            "mp"            : 0,
            "eva"           : 1,
            "daño"          : 53,
            "golpe"         : 20,
            "probabilidad"  : 1,
        }, 
        "guantes"       : {
            "vit"           : 10, 
            "str"           : 2, 
            "will"          : 5, 
            "int"           : 0, 
            "agi"           : 3,
            "defense"       : 50,
            "defense_magic" : 20,
            "attack"        : 0,      
            "attack_magic"  : 0,
            "hp"            : 130,
            "mp"            : 0,
            "eva"           : 1,
            "daño"          : 53,
            "golpe"         : 20,
            "probabilidad"  : 1,
        },
        "arma"          : {
            "vit"           : 50, 
            "str"           : 40, 
            "will"          : 20, 
            "int"           : 0, 
            "agi"           : 10,
            "defense"       : 0,
            "defense_magic" : 0,
            "attack"        : 700,      
            "attack_magic"  : 500,
            "hp"            : 450,
            "mp"            : 0,
            "eva"           : 1,
            "daño"          : 53,
            "golpe"         : 20,
            "probabilidad"  : 1,
        },
        "escudo"        : {
            "vit"           : 100, 
            "str"           : 100, 
            "will"          : 40, 
            "int"           : 0, 
            "agi"           : 10,
            "defense"       : 600,
            "defense_magic" : 450,
            "attack"        : 0,      
            "attack_magic"  : 0,
            "hp"            : 590,
            "mp"            : 0,
            "eva"           : 0,
            "daño"          : 53,
            "golpe"         : 20,
            "probabilidad"  : 4,
        }
    }

    # start_game(player, enemy)

    # print(f'CLASE:', ClassEnum.Killer.value)
    # print(f'CLASE:', ClassEnum.Killer.name)
    # clas = Class.Warrior
    # print(clas)
    # if Class.Warrior == Class.Warrior:
    #     print('SON IGUALEs')
        
    
    # Names = Enum("Names", [("Waiz",8), ("Tom",5), ("Sara",7), ("Lee",6)])

    # print(Names.Sara.value)
    # print(Names.Waiz.value)
    
    
    
    # evasion         : int      # Puntos de evasión
    # hit             : int      # Puntos para golpear
    # psl_dmg         : float    # Porcentaje de daño físico
    # mgc_dmg         : float    # Porcentaje de daño mágico
    # pbt_psl_dmg     : float    # Probabilidad de dar un golpe crítico físico
    # pbt_mgc_dmg     : float    # Probabilidad de dar un golpe crítico mágico
    # pbt_rdc_psl     : float    # Probabilidad de reducir un golpe crítico físico recibido
    # pbt_rdc_mgc     : float    # Probabilidad de reducir un golpe crítico mágico recibido
    # rdc_psl_dmg     : float    # Porcentaje de reducción por golpe crítico físico recibido
    # rdc_mgc_dmg     : float    # Porcentaje de reducción por golpe crítico mágico recibido
    head = Equipment(
        type            = EquipmentType.Head,
        name            = "Dark Helmet",
        color           = EquipmentColor.White,
        level           = 1,
        vit             = 10,
        str             = 20,
        will            = 0,
        int             = 0,
        agi             = 10,
        defense         = 230,
        defense_magic   = 120,
        attack          = 0,
        attack_magic    = 0,
        hp              = 144,
        mp              = 0,
        evasion         = 10,
        hit             = 6,
        psl_dmg         = 4,
        mgc_dmg         = 1,
        pbt_psl_dmg     = 1,
        pbt_mgc_dmg     = 1,
        pbt_rdc_psl     = 1,
        pbt_rdc_mgc     = 1,
        rdc_psl_dmg     = 1,
        rdc_mgc_dmg     = 1,
        durability      = 100,
        fortify         = 0,
        comment         = 'Armor of darkness',
        stones          = []
    )

    body = Equipment(
        type            = EquipmentType.Body,
        name            = "Dark Body",
        color           = EquipmentColor.White,
        level           = 1,
        vit             = 20,
        str             = 12,
        will            = 5,
        int             = 0,
        agi             = 2,
        defense         = 250,
        defense_magic   = 200,
        attack          = 0,
        attack_magic    = 0,
        hp              = 250,
        mp              = 0,
        evasion         = 10,
        hit             = 6,
        psl_dmg         = 4,
        mgc_dmg         = 1,
        pbt_psl_dmg     = 1,
        pbt_mgc_dmg     = 1,
        pbt_rdc_psl     = 1,
        pbt_rdc_mgc     = 1,
        rdc_psl_dmg     = 1,
        rdc_mgc_dmg     = 1,
        durability      = 100,
        fortify         = 0,
        comment         = "Armor of darkness",
        stones          = []
    )

    glove = Equipment(
        type            = EquipmentType.Glove,
        name            = "Dark Glove",
        color           = EquipmentColor.White,
        level           = 1,
        vit             = 5,
        str             = 4,
        will            = 5,
        int             = 0,
        agi             = 2,
        defense         = 120,
        defense_magic   = 90,
        attack          = 0,
        attack_magic    = 0,
        hp              = 40,
        mp              = 0,
        evasion         = 8,
        hit             = 6,
        psl_dmg         = 4,
        mgc_dmg         = 1,
        pbt_psl_dmg     = 1,
        pbt_mgc_dmg     = 1,
        pbt_rdc_psl     = 1,
        pbt_rdc_mgc     = 1,
        rdc_psl_dmg     = 1,
        rdc_mgc_dmg     = 1,
        durability      = 100,
        fortify         = 0,
        comment         = "Armor of darkness",
        stones          = []
    )

    player = Player(
        level   = 4,
        name    = "Slasher"
    )

    player.put_on_armor(body)
    player.put_on_armor(head)
    player.put_on_armor(glove)

    print(f"Jugador ARMOR: { player.armor.values() }")
    print(f"Jugador LEVEL: { player.level }")
    print(f"Jugador NAME : { player.name }")


if __name__ == '__main__':
    run()