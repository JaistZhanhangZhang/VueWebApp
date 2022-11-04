from sqlalchemy.orm import Session
import models
import schemas

def create_user(db:Session,user:schemas.UserCreate):
    
    db_user=models.UserDB(name=user.name,password=user.password,email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_name(db:Session,name:str):
    return db.query(models.UserDB).filter(models.UserDB.name == name).first()



def sort_user_by_name(db:Session,skip:int = 1, limit:int = 10):
##    return db.query(models.City).offset(skip).limit(limit).all()
##    return db.query(models.City).order_by(models.City.country_code).offset(skip).limit(limit).all()
    return db.query(UserDB).order_by(UserDB.name).offset(skip).limit(limit).all()


def create_image(db:Session,image:schemas.ImageCreate):
    db_img=models.ImageDB(title=image.title,
                          imageData=image.imageData,
                          owner_ID=image.owner_ID,     
                          #user=image.user,?
                          #tag=image.tag?
                          )
    db.add(db_img)
    db.commit()
    db.refresh(db_img)
    return db_img

def get_image_by_title(db:Session,title:str):
    ### 精确查找
    return db.query(models.ImageDB).filter(models.ImageDB.title==title).first()

def get_all_images_by_userID(db:Session,ID:int):
    user = db.query(models.UserDB).get(ID)
    return user.img

    
