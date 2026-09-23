from pydantic import BaseModel

class User(BaseModel):
    name : str
    age : int
    
user_data = {
    "name" : "Sultan Mahamud",
    # "age" : 32
    # "age" : "32" # তবে এটাকে সে নিজেই int এ convert করে দিবে
    "age" : "thirty two" # এখন এটা error দিবে, কিন্তু typeddict এ এটা error দিত না
}

user1 = User(**user_data)

# print(user_data)
print(user1)