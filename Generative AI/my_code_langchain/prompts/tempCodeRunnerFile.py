from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    input_variables=["paper_input", "style_input", "length_input"],
    validate_template= True, 
    # এখানে validate_template দিলে, user যদি input_variables এ কোন input দিতে ভুলে যায় বা typing mistack করে তবে সেটা error হিসবা দেখাবে
    # input_variables=[ "style_input", "length_input"], missing input
    # input_variables=["paperinput", "style_input", "length_input"], typing mistack
    