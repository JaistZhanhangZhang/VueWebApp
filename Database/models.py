from sqlalchemy import Column, String, Integer, BigInteger,DateTime,func,ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class UserDB(Base):
    __tablename__="user"
    ID = Column(Integer,primary_key=True,index=True,autoincrement=True)
    name = Column(String(64),unique=True,nullable=False,comment="user_name")
    email = Column(String(128),nullable=False,comment="Emali")
    password = Column(String(64),nullable=False,comment="password")
    #create_at = Column(DateTime,server_default=func.now(),comment="created time")
    img=relationship("ImageDB",back_populates="user")#类名 back反向查询 表名
    #__mapper_args__={"order_by":name} 方法废弃

class ImageDB(Base):
    __tablename__="image"
    ID = Column(Integer,primary_key=True,index=True,autoincrement=True)
    create_at = Column(DateTime,server_default=func.now(),comment="created time")
    
    owner_ID=Column(Integer,ForeignKey("user.ID"),comment="related_user_ID")
    user=relationship("UserDB",back_populates="img")#类名 back反向查询 变量名
    title=Column(String(128),nullable=False,comment="image title")
    imageData=Column(String(256),nullable=False,comment="Image")

    ##  tag_name= 多对多怎么写
##    tag_name=Column(String(64),ForeignKey("tag.name"),comment="related_tag_name" )
##    tag=relationship("Tag",back_populates="image")
    #__mapper_args__={"order_by":user_ID} 方法废弃


class TagDB(Base):
    __tablename__="tag"
    ID = Column(Integer,primary_key=True,index=True,autoincrement=True)
    name = Column(String(64),unique=True,nullable=False,comment="tag_name")
    #img=relationship("ImageDB",back_populates="tag")
