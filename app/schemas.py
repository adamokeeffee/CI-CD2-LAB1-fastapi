from typing import Annotated

from pydantic import BaseModel, ConfigDict, EmailStr, Field, StringConstraints

NameStr = Annotated[str,StringConstraints(min_length=2, max_length=50)]
StudentidStr = Annotated[str, StringConstraints(pattern=r"^S\d{7}$")]

class UserCreate(BaseModel):
    user_id: int = Field(gt=0)
    name: Annotated[str, StringConstraints(min_length=2, max_length=50)]
    email:EmailStr
    age: int = Field(gt=18, lt=120)
    student_id: Annotated[str, StringConstraints(pattern=r"^S\d{7}$")]

class UserRead(BaseModel):
    model_config =  ConfigDict(from_attributes=True)

    id: int
    name: NameStr
    email: EmailStr
    age: int
    student_id: StudentidStr    