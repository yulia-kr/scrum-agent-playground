from crewai import Agent
from langchain_openai import AzureChatOpenAI
from config import AZURE_OPENAI_LLM_DEPLOYMENT_NAME, AZURE_OPENAI_LLM_MODEL_NAME

# Initialize LLM
llm = AzureChatOpenAI(
    azure_deployment=AZURE_OPENAI_LLM_DEPLOYMENT_NAME, 
    model=AZURE_OPENAI_LLM_MODEL_NAME,
    temperature=0.8
)

# Good Example Analyzer
good_example_analyzer = Agent(
    role="Good Example Analyzer",
    goal="Analyze the good example ticket to extract the style, structure, and key elements expected for a well-formed user story.",
    llm=llm,
    backstory="You are an experienced product owner and Agile coach. Your job is to understand how a well-written user story is structured and provide insights on style, structure, and tone to the user story generator."
)

# Feature Analyzer
feature_analyzer = Agent(
    role="Feature Analyzer",
    goal="Analyze the feature description and extract key information including context, problem statement, target audience, and goals.",
    llm=llm,
    backstory="You are an experienced business analyst with deep expertise in software requirements. Your role is to extract critical information from technical documentation and feature descriptions, identifying the key objectives, problems being solved, and the relevant stakeholders."
)

# Ticket Parser
ticket_parser = Agent(
    role="Ticket Parser",
    goal="Extract the ticket name, short description, and additional metadata such as dependencies, links, epics, and sprints from the user story ticket.",
    llm=llm,
    backstory="You are detail-oriented and skilled at parsing technical documents. Your goal is to capture all critical information from the ticket, including dependencies, links, and other metadata required to complete the story."
)

# User Story Generator
user_story_generator = Agent(
    role="User Story Generator",
    goal="Generate a well-structured user story, including detailed descriptions and acceptance criteria, based on the provided feature summary and ticket information. Ensure missing information is identified and clearly prompt for clarification.",
    llm=llm,
    backstory="You are an expert in Agile development with a deep understanding of best practices for writing user stories. Your role is to ensure user stories are complete, concise, and include well-defined acceptance criteria, highlighting any gaps or ambiguities that need further clarification from stakeholders."
)
