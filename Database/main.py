from typing import List
from fastapi import FastAPI, Depends, File, UploadFile,Form
from database import SessionLocal, engine
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import models,schemas,curd
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from datetime import datetime, timedelta


app=FastAPI()
origins=["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


#models.Base
models.Base.metadata.create_all(bind=engine)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@app.get("/")
def hello_world():
    return "Hello world"


#@app.post("/SignUp",response_model=schemas.User)
@app.post("/SignUp")
def create_user(user:schemas.UserCreate,db:Session = Depends(get_db)):
    
    db_user=curd.get_user_by_name(db,name=user.name)
   
    if db_user:
        #print("successSUCCESSsuccessSUCCESS")
        return {"Error":"1","Message":"User name has been registered"}
    else:
        #print("SUCCESSsuccessSUCCESSsuccess")
        curd.create_user(db=db,user=user)
        return {"Error":"0","Message":"registere success"}

@app.get("/findUserByName/{username}",response_model=schemas.User)
def findUserByName(username:str,db:Session=Depends(get_db)):
    db_user = curd.get_user_by_name(db,name=username)
    if db_user is None:
        return "not find"
    else:
        return db_user

@app.post("/SignIn")
def CheckSignIn(user:schemas.UserSignIn,db:Session = Depends(get_db)):
    db_user=curd.get_user_by_name(db,name=user.name)
    if db_user:
        if db_user.password == user.password:
            username = user.name
            data={"username":username,
            "token":username.upper(),
            "expires":(datetime.now()+timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S"),
            ##还原：date=datetime.strptime(date_str,"%Y-%m-%d %H:%M:%S")
            ##判断：(expires-date).days  ><== 0 ?
            "Error":"0",
            "Message":"Login success"}
            response = JSONResponse(content = data)
            return response
            ##Cookie set up
        else:
            return {"Error":"1","Message":"password is incorrect"}
    else:
        return {"Error":"1","Message":"User has not been registered"}

##@app.post("/ImageSubmit")
##def imgsubmit(title:str=Form(),tag:str=Form()):
##    print(title)
##    print(tag)
##    return "success"

@app.post("/ImageSubmit")
async def ImageSubmit(file: UploadFile = File(), title:str=Form(), tag:str=Form(), Username:str=Form(),db:Session=Depends(get_db)):
    print("success")
    db_user=curd.get_user_by_name(db,name=Username)
    userid=db_user.ID
    imgbytes=file.file.read()
    imgname = file.filename
    savedir="Image/"
    
    with open(savedir+imgname, "wb") as fout:
        fout.write(imgbytes)
    im=schemas.ImageCreate(title=title,imageData=savedir+imgname,owner_ID=userid)

    """TODO add tag for images"""
    
    db_user.img.append(curd.create_image(db=db,image=im))
    
    return "success"

@app.get("/Selectimages/{userid}")
def Selectimages(userid,db:Session=Depends(get_db)):
    images=curd.get_all_images_by_userID(db,userid)
    return images


if __name__ == '__main__':
    uvicorn.run(app,host="127.0.0.1",port=8000)



