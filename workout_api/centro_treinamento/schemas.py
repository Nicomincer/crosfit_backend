
from typing import Annotated
from pydantic import Field
from workout_api.contrib.schemas import BaseSchema


class CentroTreinamento(BaseSchema):
    nome: Annotated[str, Field(description='nome do centro de treinamento', example='CT Royal', max_length=20)]
    endereco: Annotated[str, Field(description='endereco do centro de treinamento', example='Rua X', max_length=60)]
    proprietario: Annotated[str, Field(description='proprietario do centro de treinamento', example='Marcos', max_length=30)]