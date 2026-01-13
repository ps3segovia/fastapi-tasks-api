from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Используем SQLite — файл базы будет в корне проекта
SQLALCHEMY_DATABASE_URL = "sqlite:///./tasks.db"

# Создаём "движок" — он управляет соединением с БД
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, 
    connect_args={"check_same_thread": False}  # только для SQLite!
)

# Фабрика сессий — через неё будем общаться с БД
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Базовый класс для моделей
Base = declarative_base()