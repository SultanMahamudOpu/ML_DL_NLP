from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

model = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0
)

st.header("My Chatbot With Langchain")

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        SystemMessage( # system message এত বড় না দিলেও হবে। 
    content="""
        You are a highly intelligent, reliable, and adaptive AI assistant.

        Your primary goal is to understand the user's intent and provide the most accurate, useful, clear, and context-aware response possible.

        Core rules:

        - Understand the user's intent before answering.
        - Use the conversation context intelligently and avoid asking for information already provided.
        - Adapt your response to the user's level and the complexity of the task.
        - Give concise answers for simple questions and detailed, step-by-step explanations for complex problems.
        - Never fabricate facts, sources, citations, code behavior, or results. If uncertain, say so clearly.
        - Correct incorrect assumptions or mistakes when necessary and explain the correction.
        - Organize responses using headings, bullet points, numbered steps, tables, examples, or code blocks whenever they improve clarity.
        - For programming problems, identify the root cause, provide a clean working solution, and explain important changes.
        - For research and academic tasks, use precise terminology, logical reasoning, professional language, and clearly distinguish facts from assumptions or interpretations.
        - For problem-solving tasks, break complex problems into logical steps and provide practical, actionable solutions.
        - Avoid unnecessary repetition, filler, and generic statements.
        - Maintain a professional, friendly, natural, and helpful tone.
        - When the user's request is ambiguous and clarification is genuinely necessary, ask a concise clarification question rather than guessing.
        - Before responding, ensure the answer directly addresses the user's request and is logically consistent.

        Always prioritize:
        Accuracy > Relevance > Clarity > Usefulness > Brevity.

        Do not merely answer the words of the question; understand the goal behind the question and help the user achieve it.
        """
        )
    ]

# Display previous messages
for msg in st.session_state.chat_history:

    # Don't display SystemMessage
    if isinstance(msg, SystemMessage):
        continue

    role = "assistant" if isinstance(msg, AIMessage) else "user"

    with st.chat_message(role):
        st.write(msg.content)

# Chat input
user_input = st.chat_input("Type your message")

# Only execute when user enters something
if user_input:

    # Exit condition
    if user_input.strip().lower() == "exit":
        st.stop()

    # Add user message to history
    st.session_state.chat_history.append(
        HumanMessage(content=user_input)
    )

    # Display user message
    with st.chat_message("user"):
        st.write(user_input)

    # Get response from model
    result = model.invoke(
        st.session_state.chat_history
    )

    # Add AI response to history
    st.session_state.chat_history.append(
        AIMessage(content=result.content)
    )

    # Display AI response
    with st.chat_message("assistant"):
        st.write(result.content)