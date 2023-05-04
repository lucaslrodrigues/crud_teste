from pydantic import BaseModel
from typing import List, Optional

class User(BaseModel):
    id: int[Optional]
    name: str
    login: str
    password: str

class UserUpdate():
    id: int[Optional]
    name: str[Optional]
    login: str[Optional]
    password: str[Optional]

class Wallet():
    id: int
    balance: float
    idUser: int

class Product():
    id: int
    name: str
    price: float