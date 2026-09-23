from langchain_groq import ChatGroq
from pydantic import BaseModel , EmailStr, Field
from typing import Optional 
from dotenv import load_dotenv

load_dotenv()

class JobApplication(BaseModel):
    name : str = "Unknown"
    experience : Optional[int] = None
    email : EmailStr
    expected_salary : int = Field( gt =0  , description="Expected Annual Salary of the candidate" )

# create the model
model = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0
)

# create a sturctured model
structured_mode = model.with_structured_output(JobApplication)

# invoke the model

result = structured_mode.invoke(
    """My name is Sultan Mahamud Opu. I have 3 years of experience
    as a Machine Learning Engineer.

    My email is arif@gmail.com.
    I am expecting an annual salary of 50000 dollars.
    """
)

print(result)
print(result.name)