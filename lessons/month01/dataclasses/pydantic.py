from pydantic import BaseModel

class User(BaseModel):
    pass

a = User
print(a)