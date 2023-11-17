from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine import URL

sql_database_url="mysql://adopter-1.ccixfecy4h7f.us-east-1.rds.amazonaws.com:3306/adopter"

sql_database_url = URL.create(
    drivername="mysql",
    username="admin",
    password="password",
    host="adopter-1.ccixfecy4h7f.us-east-1.rds.amazonaws.com",
    database="adopter",
    port=3306
)


engine=create_engine(sql_database_url)

SessionLocal=sessionmaker(autocommit=False,bind=engine)

base=declarative_base()