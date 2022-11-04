from typing import List, Union
from pydantic import BaseModel

class TagBase(BaseModel):
    name:str
class TagCreate(TagBase):
    pass
class Tag(TagCreate):
    ID:int

#-------------------------------------#    


class ImageBase(BaseModel):
    title:str
    imageData:str
    owner_ID:int
    #tag: List[Tag] = []
class ImageCreate(ImageBase):
    pass

class Image(ImageCreate):
    ID:int
    class Config:
        orm_mode=True
#-------------------------------------#
class UserSignIn(BaseModel):
    name:str
    password:str
    class Config:
        orm_mode=True

class UserBase(BaseModel):
    name:str
    email:str

class UserCreate(UserBase):
    """#the password won't be in other Pydantic models, for example,
    it won't be sent from the API when reading a user."""
    password:str

class User(UserCreate):
    ID:int
    #img:List[Image] = [] # ?
    class Config:
        orm_mode=True
