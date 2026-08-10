from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base


class CategoryModel(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(50), unique=True, nullable=False)

    dishes = relationship("DishModel", back_populates="category")