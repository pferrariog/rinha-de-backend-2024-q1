from datetime import datetime

from pydantic import BaseModel
from pydantic import validator


class CustomerTransactionRequest(BaseModel):
    """Transaction request schema"""

    valor: int
    tipo: str
    descricao: str
    realizada: datetime = datetime.now()

    @validator("tipo")
    def _type_validator(cls, type) -> str:
        """Validate type input value"""
        if type not in ["c", "d"]:
            raise ValueError("Tipo de transação deve ser 'c' para crédito ou 'd' para débito")
        return type


class CustomerTransactionResponse(BaseModel):
    """Transaction response schema"""

    limite: int
    saldo: int


class CustomerFinalTransactionResponse(BaseModel):
    """Transaction response with datetime"""

    realizada: datetime


class CustomerBalanceInformation(BaseModel):
    """Information about customer's account"""

    total: int
    data_extrato: datetime
    limite: int


class CustomerExtractResponse(BaseModel):
    """Customer's extract full information"""

    saldo: CustomerBalanceInformation
    ultimas_transacoes: list[CustomerTransactionRequest]
