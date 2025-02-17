from langchain.schema import HumanMessage, SystemMessage

#----------------------------------------------------------------------------------------
# EXTRACTION

# prompt used to extract questions
extraction_system_prompt="You are an AI trained to extract information from documentation to create an engaging quiz. You will be passed a page extracted from the documentation. Your task is to write a numbered list of questions that can be answered based solely on the given text. Start with broader, general questions about the overall content, and then branch out into more specific questions about the details. This should create a 'tree of thoughts' structure, where each general question has related detailed questions under it."


def create_extraction_conversation_messages(text):
    """
    Takes a piece of text and returns a list of messages designed to extract questions from the text.
    
    Args:
        text (str): The input text for which questions are to be extracted.
    
    Returns:
        list: A list of messages that set up the context for extracting questions.
    """
    # Create a system message setting the context for the extraction task
    context_message = SystemMessage(content=extraction_system_prompt)
    
    # Create a human message containing the input text
    input_text_message = HumanMessage(content=text)
    
    # Return the list of messages to be used in the extraction conversation
    return [context_message, input_text_message]


#----------------------------------------------------------------------------------------
# ANSWERING

# prompt used to answer a question
answering_system_prompt="You are an AI expert in answering questions. You will be passed a page extracted from a documentation and a question. The questions will be organized in a 'tree of thoughts' manner, with general questions followed by more detailed ones. Your task is to generate a comprehensive and informative answer to the question based solely on the given text. If the question is a detailed one, make sure to provide the specific information asked for, but also consider the broader context of the related general question."



def create_answering_conversation_messages(question, text):
    """
    Takes a question and a text and returns a list of messages designed to answer the question based on the text.
    
    Args:
        question (str): The question to be answered.
        text (str): The text containing information for answering the question.
    
    Returns:
        list: A list of messages that set up the context for answering the question.
    """
    # Create a system message setting the context for the answering task
    context_message = SystemMessage(content=answering_system_prompt)
    
    # Create a human message containing the input text
    input_text_message = HumanMessage(content=text)
    
    # Create a human message containing the question to be answered
    input_question_message = HumanMessage(content=question)
    
    # Return the list of messages to be used in the answering conversation
    return [context_message, input_text_message, input_question_message]
