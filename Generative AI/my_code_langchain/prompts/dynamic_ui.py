from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate, load_prompt
from dotenv import load_dotenv
import streamlit as st

# Load environment variables
load_dotenv()

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Research Tool",
    page_icon="📚",
    layout="centered"
)

# -----------------------------
# Initialize LLM
# -----------------------------
model = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0
)

# -----------------------------
# UI
# -----------------------------
st.title("📚 Research Paper Summarizer")
st.write(
    "Select a research paper and choose how you want the explanation "
    "to be presented."
)

paper_input = st.selectbox(
    "Select Research Paper",
    [
        "Attention Is All You Need",
        "BERT: Pre-training of Deep Bidirectional Transformers "
        "for Language Understanding",
        "GPT-3: Language Models are Few-Shot Learners",
        "Diffusion Models Beat GANs on Image Synthesis"
    ]
)

style_input = st.selectbox(
    "Select Explanation Style",
    [
        "Beginner-Friendly",
        "Technical",
        "Code-Oriented",
        "Mathematical"
    ]
)

length_input = st.selectbox(
    "Select Explanation Length",
    [
        "Short (1-2 paragraphs)",
        "Medium (3-5 paragraphs)",
        "Long (detailed explanation)"
    ]
)

# -----------------------------
# Prompt Template
# -----------------------------
template = load_prompt('template.json')
# -----------------------------
# Summarization
# -----------------------------
if st.button("🔍 Summarize Paper", use_container_width=True):

    with st.spinner("Analyzing the research paper..."):

        prompt = template.invoke(
            {
                "paper_input": paper_input,
                "style_input": style_input,
                "length_input": length_input
            }
        )

        result = model.invoke(prompt)

    st.subheader("📄 Research Paper Summary")
    st.write(result.content)