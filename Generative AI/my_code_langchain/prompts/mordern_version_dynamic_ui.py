from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
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
template = PromptTemplate.from_template(
    template="""
You are an expert research paper analyst.

Summarize the research paper titled:

"{paper_input}"

Follow these specifications carefully:

1. Explanation Style:
   - Write the explanation in a {style_input} style.
   - Adapt the technical depth and terminology to the selected style.

2. Explanation Length:
   - Follow the requested length: {length_input}.

3. Mathematical Details:
   - Include important mathematical equations, formulas, or
     mathematical concepts from the paper when relevant.
   - Explain each equation clearly and intuitively.
   - If the selected style is Code-Oriented, provide short and
     simple code snippets where they help explain the concept.

4. Key Contributions:
   - Explain the main problem addressed by the paper.
   - Describe the proposed method or architecture.
   - Highlight the major contributions.
   - Explain the experimental setup and important findings.

5. Analogies:
   - Use simple, relatable analogies when they help clarify
     complex concepts.

6. Accuracy:
   - Do not invent information.
   - If a requested piece of information is not available
     from the paper, write:
     "Insufficient information available"

Make the explanation clear, accurate, well-structured, and
consistent with the selected style and length.
"""
)

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
        # prompt after filling the placeholders
        result = model.invoke(prompt)

    st.subheader("📄 Research Paper Summary")
    st.write(result.content)