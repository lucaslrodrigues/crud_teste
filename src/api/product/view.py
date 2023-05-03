from src.service.pessoa_service import PessoaService
from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from typing import List

router = APIRouter()

