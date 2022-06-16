# Python
from stats.stats_base import Stats_Base


class Player_Stats(Stats_Base):

    evasion         : int   = 0    # Puntos de evasión
    hit             : int   = 0    # Puntos para golpear
    psl_dmg         : float = 0    # Porcentaje de daño físico
    mgc_dmg         : float = 0    # Porcentaje de daño mágico
    pbt_psl_dmg     : float = 0    # Probabilidad de dar un golpe crítico físico
    pbt_mgc_dmg     : float = 0    # Probabilidad de dar un golpe crítico mágico
    pbt_rdc_psl     : float = 0    # Probabilidad de reducir un golpe crítico físico recibido
    pbt_rdc_mgc     : float = 0    # Probabilidad de reducir un golpe crítico mágico recibido
    rdc_psl_dmg     : float = 0    # Porcentaje de reducción por golpe crítico físico recibido
    rdc_mgc_dmg     : float = 0    # Porcentaje de reducción por golpe crítico mágico recibido
    # ! Proximamente agregar perforación física y mágica