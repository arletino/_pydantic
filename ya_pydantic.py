
# Constraining types
from pydantic import ValidationError, BaseModel



from pydantic import condecimal, conint, constr # Deprecated in Pydantic v3.0 - use Annotated  with Field instead
from pydantic import conlist

class Drink(BaseModel):
    alcohol: condecimal(ge=0, lt=18)
    name: str


class Guest(BaseModel):
    age: conint(ge=18, lt=100)
    name: constr(min_length=2, max_length=20)


class Party(BaseModel):
    guests: conlist(item_type=Guest, 
                    min_items=1, max_items=50)
    drinks: conlist(item_type=Drink, 
                    min_items=1, max_items=50)


try:
    vodka = Drink(name='vodrka', alcohol=40)
    print(vodka)
except ValidationError as e:
    print(e)
try:
    water = Drink(name='water', alcohol=0)
    print(water)
except ValidationError as e:
    print(e)
try:
    Party(guests=[{'age':12, 'name': 'Billy'}], 
          drinks=[{'alcohol':40}])
except ValidationError as e:
    print(e)

from typing import Optional
from pydantic import BaseSettings


#Pydantic & Settings
class LoggingSettings(BaseSettings):
    host: Optional[str]
    port: Optional[str]

    class Config:
        env_prfix = 'LOGGING_'

