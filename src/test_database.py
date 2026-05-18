from sqlalchemy import create_engine

engine = create_engine(
    'postgresql://admin:admin123@localhost:5432/retail_analysis'
)

connection = engine.connect()

print("Database connected successfully!")