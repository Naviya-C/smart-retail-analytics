from sqlalchemy import create_engine
from config import USER_D, PASSWORD_D

engine = create_engine(
    f'postgresql://{USER_D}:{PASSWORD_D}@localhost:5432/retail_analysis'
)

connection = engine.connect()

print("Database connected successfully!")