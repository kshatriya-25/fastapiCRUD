# OM VIGHNHARTAYE NAMO NAMAH :
from bson import ObjectId
#imports and other stuff
from fastapi import FastAPI , HTTPException
from pydantic import BaseModel, Field,  StringConstraints
import motor.motor_asyncio
from typing_extensions import Annotated
from fastapi.middleware.cors import CORSMiddleware


#initalisation
app = FastAPI()
#for form purpose but can be stricter on production or critical methods
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins; specify a list of origins if needed
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017")

db = client.task_database


#Creating a User Object
class User:
    name: str
    password: str
    email: str
    phoneNo: int

    def __init__(self , name , password , email , phoneNo):
        self.name = name
        self.password = password
        self.email = email
        self.phoneNo = phoneNo

#creating request validation models
class UserRequest(BaseModel):
    name: Annotated[
        str,
        StringConstraints(
            strip_whitespace=True,
            pattern = r'^[A-Za-z]+$',
            min_length=3,
            max_length=20
        )
    ]
    email : str = Field(min_length=3)
    phoneNo : int
    password : str = Field(min_length=3)

    model_config = {
        "json_schema_extra":{
            "example":{
                "name": "Ankit",
                "email": "ankit@saliabs.com",
                "phoneNo": 9363491264,
                "password": "password"
            }
        }
    }


#performing Crud on this object

#Create
@app.post("/users" , status_code=201)
async def createUser(user : UserRequest):
    user_data = user.model_dump()
    # print("user Data: " +str(user_data) )
    result = await db.users.insert_one(user_data)
    return {
        "msg" : "User created Successfully",
        "id" : str(result.inserted_id)
    }

#Read, No check required due to no data passed
@app.get("/users/{user_id}")
async def get_User(user_id: str):
    user = await db.users.find_one({"_id": ObjectId(user_id)})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    # Serialization for avoiding internal server error
    user["_id"] = str(user["_id"])
    return user

#Update
@app.put("/users/{user_id}")
async def update_userData(user_id : str , user : UserRequest):
    result = await db.users.update_one({"_id" : ObjectId(user_id)} , {"$set" : user.model_dump() })
    if result.matched_count == 0:
        raise HTTPException(status_code=404 , detail="User not found")
    return {"msg" : "User updated Successfully!"}
'''
    ⚠️ in the update method i have to pass the full object here as i have created a full field mandatory validation but 
    this can be done optionally with craeting another optioanl field that gives flexiblity to update only that field 
'''

@app.delete("/users/{user_id}")
async def deleteUser(user_id : str):
    result = await db.users.delete_one({"_id" : ObjectId(user_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404 , detail="User not found")
    return {
        "msg" : "user deleted successfully"
    }


print("HAR HAR MAHADEV")