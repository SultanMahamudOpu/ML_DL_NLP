from langchain_groq import ChatGroq
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Literal, Optional

load_dotenv()

model = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0
)

# define the schema
class ResumeAnalysis(TypedDict):
    candidate_name : Annotated[ str, 'Extract the name of the Candiate from the resume']
    key_skills : Annotated[list[str], 'Extract all important technical and soft skills from the resume']
    # literal use করি যখন আমার কাছে অনেক গুলা catagory থাকে কিন্তু আমার অল্প কিছু catagory তে ওই সব গুলা নিতে হবে তখন
    # যেমন বয়স দেয়া আছে 1,2,3,4,5,10,15,16,20,15,16,30,50,70
    # আমি চাইলে বয়সকে child, young, old এ ভাগ করে নিতে পারি, এটাই literal এর কাজ
    experience_level : Annotated[Literal['entry-level', 'mid-level', 'senior-level'], "Classify the Candidate's Experiences level"]
    strengths : Annotated[Optional[list[str]], "List the candidate's major strengths"]
    weaknesses : Annotated[Optional[list[str]], "List the candidate's possible weaknesses or ares for improvement"]
# create structured output
structured_model = model.with_structured_output(ResumeAnalysis)

# invoke the model

result = structured_model.invoke(
        """My name is  Sultan Mahamud Opu. I am a Computer Science graduate with two years
    of experience working as a Machine Learning Engineer.

    I have experience with Python, PyTorch, TensorFlow, Scikit-learn,
    FastAPI, Docker, Kubernetes, MLflow, and AWS. I have built machine
    learning pipelines, deployed deep learning models, and developed
    REST APIs for AI applications.

    I also have experience working with LangChain and Retrieval-Augmented
    Generation (RAG) systems.

    My main strength is my ability to build complete machine learning
    systems from data preprocessing to deployment. However, I have limited
    experience managing large engineering teams and need to improve my
    system design skills.

    Education:
    BSc in Computer Science and Engineering.
    """
)

print(result)
# print(result['candidate_name'])