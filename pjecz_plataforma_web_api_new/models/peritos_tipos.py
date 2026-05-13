"""
Peritos Tipos, modelos
"""

from typing import List

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..dependencies.database import Base
from ..dependencies.universal_mixin import UniversalMixin


class PeritoTipo(Base, UniversalMixin):
    """PeritoTipo"""

    # Nombre de la tabla
    __tablename__ = "peritos_tipos"

    # Clave primaria
    id: Mapped[int] = mapped_column(primary_key=True)

    # Columnas
    nombre: Mapped[str] = mapped_column(String(256), unique=True)

    # Hijos
    peritos: Mapped[List["Perito"]] = relationship("Perito", back_populates="perito_tipo")

    def __repr__(self):
        """Representación"""
        return f"<PeritoTipo {self.nombre}>"
