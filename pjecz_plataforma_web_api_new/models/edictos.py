"""
Edictos, modelos
"""

from datetime import date

from sqlalchemy import Date, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..dependencies.database import Base
from ..dependencies.universal_mixin import UniversalMixin


class Edicto(Base, UniversalMixin):
    """Edicto"""

    # Nombre de la tabla
    __tablename__ = "edictos"

    # Clave primaria
    id: Mapped[int] = mapped_column(primary_key=True)

    # Claves foráneas
    autoridad_id: Mapped[int] = mapped_column(ForeignKey("autoridades.id"))
    autoridad: Mapped["Autoridad"] = relationship(back_populates="edictos")

    # Columnas
    fecha: Mapped[date] = mapped_column(Date(), index=True)
    descripcion: Mapped[str] = mapped_column(String(256))
    expediente: Mapped[str] = mapped_column(String(16))
    numero_publicacion: Mapped[str] = mapped_column(String(16))
    archivo: Mapped[str] = mapped_column(String(256), default="", server_default="")
    url: Mapped[str] = mapped_column(String(512), default="", server_default="")

    # Columnas nuevas
    acuse_num: Mapped[int] = mapped_column(default=0)
    edicto_id_original: Mapped[int] = mapped_column(default=0)

    @property
    def distrito_id(self):
        """Distrito ID"""
        return self.autoridad.distrito_id
