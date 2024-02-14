from typing import Union

from app.schemas.customer_schemas import CustomerTransactionRequest
from app.schemas.customer_schemas import CustomerTransactionResponse
from fastapi import APIRouter


route = APIRouter("/clientes")


@route.get("/{id}/extrato")
def get_extract(id) -> ...:
    """Get customer's account extract"""

    ...


@route.post("/{id}/transacoes")
def send_transactions(id: int, request: CustomerTransactionRequest) -> Union[CustomerTransactionResponse, None]:
    """Amount transaction operation"""

    ...
