from typing import Union

from fastapi import APIRouter
from schemas.customer import CustomerTransactionRequest
from schemas.customer import CustomerTransactionResponse


route = APIRouter("/clientes")


@route.get("/{id}/extrato")
def get_extract(id) -> ...:
    """Get customer's account extract"""

    ...


@route.post("/{id}/transacoes")
def send_transactions(id: int, request: CustomerTransactionRequest) -> Union[CustomerTransactionResponse, None]:
    """Amount transaction operation"""

    ...
