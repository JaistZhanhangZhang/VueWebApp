from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = "sqlite:///./UserInformation.db"

#Mysql postgresql
#SQLALCHEMY_DATABASE_URL = "postgresql://username:password@host:port/database_name"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,encoding="utf-8",echo=True,
    connect_args={"check_same_thread":False} #only need for Sqlite
    )

SessionLocal = sessionmaker(bind=engine,
                            autoflush=False,
                            autocommit=False,
                            expire_on_commit=True)

#创建数据表
Base = declarative_base(bind=engine,name="Base")
