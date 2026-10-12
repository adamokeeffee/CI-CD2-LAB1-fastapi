from typing import Annotated

from pydantic import BaseModel, ConfigDict, EmailStr, Field, StringConstraints

NameStr = Annotated[str,StringConstraints(min_length=2, max_length=50)]
StudentidStr = Annotated[str, StringConstraints(pattern=r"^S\d{7}$")]

class UserCreate(BaseModel):
    name: NameStr
    email:EmailStr
    age:int = Field(gt=18, lt=120)
    student_id: StudentidStr

class UserRead(BaseModel):
    model_config =  ConfigDict(from_attributes=True)

    id: int
    name: NameStr
    email: EmailStr
    age: int
    student_id: StudentidStr    