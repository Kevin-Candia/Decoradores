from pydantic import BaseModel


class Elemental(BaseModel):
    water       : float
    thunder     : float
    fire        : float
    ground      : float
    nature      : float


class Advanced_Elemental(Elemental):
    ice         : float
    electricity : float
    wash        : float
    earhqueke   : float
    hurricane   : float


class Master_Elemental(Advanced_Elemental):
    poison      : float
    time        : float
    dark        : float
    light       : float
    ghost       : float


class God_Elemental(Master_Elemental):
    nuclear     : float
    space       : float
    shadow      : float
    celestial   : float
    spectrum    : float