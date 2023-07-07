"""
Materias-Tipos de Juicios v3, rutas (paths)
"""
from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi_pagination.ext.sqlalchemy import paginate

from lib.authentications import Usuario, get_current_user
from lib.database import DatabaseSession
from lib.exceptions import MyAnyError
from lib.fastapi_pagination_custom_list import CustomList, custom_list_success_false
from lib.fastapi_pagination_datatable import DataTablePage, datatable_page_success_false

from .crud import get_materias_tipos_juicios, get_materia_tipo_juicio
from .schemas import MateriaTipoJuicioOut, OneMateriaTipoJuicioOut

materias_tipos_juicios = APIRouter(prefix="/v3/materias_tipos_juicios", tags=["materias - tipos de juicios"])


@materias_tipos_juicios.get("", response_model=CustomList[MateriaTipoJuicioOut])
async def listado_materias_tipos_juicios(
    db: DatabaseSession,
    current_user: Annotated[Usuario, Depends(get_current_user)],
    materia_id: int = None,
    materia_clave: str = None,
):
    """Listado de materias-tipos de juicios"""
    try:
        resultados = get_materias_tipos_juicios(
            db=db,
            materia_id=materia_id,
            materia_clave=materia_clave,
        )
    except MyAnyError as error:
        return custom_list_success_false(error)
    return paginate(resultados)


@materias_tipos_juicios.get("/{materia_tipo_juicio_id}", response_model=OneMateriaTipoJuicioOut)
async def detalle_materia_tipo_juicio(
    db: DatabaseSession,
    current_user: Annotated[Usuario, Depends(get_current_user)],
    materia_tipo_juicio_id: int,
):
    """Detalle de una materia-tipo de juicio a partir de su id"""
    try:
        materia_tipo_juicio = get_materia_tipo_juicio(db, materia_tipo_juicio_id)
    except MyAnyError as error:
        return OneMateriaTipoJuicioOut(success=False, message=str(error))
    return OneMateriaTipoJuicioOut.from_orm(materia_tipo_juicio)
