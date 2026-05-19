from sqlalchemy import Column, String, Date, Float, Integer

from ..src.base import Base

class Sales(Base):
    __tablename__ = 'sales'
    
    order_id = Column(String, primary_key=True, nullable=False)
    order_data = Column(Date)
    ship_date = Column(Date)
    ship_mode = Column(String)
    customer_id = Column(String)
    customer_name = Column(String)
    segment = Column(String)
    country = Column(String)
    city = Column(String)
    state = Column(String)
    #postal_code = Column(String)
    region = Column(String)
    product_id = Column(String)
    category = Column(String)
    sub_category = Column(String)
    product_name = Column(String)
    sales = Column(Float)
    quantity = Column(Integer)
    discount = Column(Float)
    profit = Column(float)