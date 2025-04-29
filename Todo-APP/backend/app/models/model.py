from pydantic import BaseModel, EmailStr

#todo model

class TodoCreate(BaseModel):
    title: str
    description: str = ""


class TodoOutput(BaseModel):
    id:int
    title: str
    description: str = ""

    class Config:
        orm_mode = True  


#user model

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    username: str
    email: EmailStr

    class Config:
        orm_mode = True

#token
class Token(BaseModel):
    access_token: str
    token_type: str