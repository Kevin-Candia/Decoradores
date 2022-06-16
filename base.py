from pydantic import BaseModel


class Base_Game(BaseModel):

    level   : int = 1,
    name    : str = 'Default Name'