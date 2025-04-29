from pydantic import BaseModel


class TodoCreate(BaseModel):
    title: str
    description: str = ""


class TodoOutput(BaseModel):
    id:int
    title: str
    description: str = ""

    class Config:
        orm_mode = True  
