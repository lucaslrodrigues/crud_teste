from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    login = Column(String)
    senha = Column(String)
    type = Column(String)

    wallet = relationship("wallet", back_populates="user")

class Product(Base):
    __tablename__ = "product"
    id = Column (Integer, primary_key=True)
    name = Column (String)
    price = Column (float)

class Wallet(Base):
    __tablename__ = "wallet"
    id = Column (Integer, primary_key=True)
    balance = Column (float)
    owner = relationship("user", back_populates="wallet")

class Sale(Base):
    __tablename__ = "sale"
    id = Column (Integer, primary_key=True)
    idUser = Column (Integer, primary_key=True)
    idProduct = Column (Integer, primary_key=True)
    datePurchase = Column (DateTime(timezone=True), default=func.now())