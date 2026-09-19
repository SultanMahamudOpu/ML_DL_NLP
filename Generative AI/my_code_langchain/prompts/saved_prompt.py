from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    input_variables=["paper_input", "style_input", "length_input"],
    validate_template= True, 
    # এখানে validate_template দিলে, user যদি input_variables এ কোন input দিতে ভুলে যায় বা typing mistack করে তবে সেটা error হিসবা দেখাবে
    # input_variables=[ "style_input", "length_input"], missing input
    # input_variables=["paperinput", "style_input", "length_input"], typing mistack
    
    
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


template.save('template.json')