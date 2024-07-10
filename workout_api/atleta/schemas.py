from typing import Annotated
from pydantic import Field, PositiveFloat
from workout_api.contrib.schemas import BaseSchema

class Atleta(BaseSchema):
    nome: Annotated[str, Field(description='nome do atleta', example='joao', max_length=50)]
    cpf: Annotated[str, Field(description='cpf do atleta', example='12345678900', max_length=11)]
    idade: Annotated[int, Field(description='idade do atleta', example=21)]
    peso: Annotated[PositiveFloat, Field(description='peso do atleta', example=75.5)]
    altura: Annotated[PositiveFloat, Field(description='altura do atleta', example=1.68)]
    sexo: Annotated[str, Field(description='sexo do atleta', example='H', max_length=1)]
    
