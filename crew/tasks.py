from crewai import Task
from crew.agents import good_example_analyzer, feature_analyzer, ticket_parser, user_story_generator

# Analyze Good Example Task
analyze_good_example_task = Task(
    description="""
    Analyze the following well-written ticket, and extract:
    * The expected style (e.g., formal, clear, concise)
    * The structure (e.g., clear definition of role, goal, and benefit)
    * Important elements in the user story (e.g., specific format, clarity, completeness)
    
    Provide insights to the user story generator so that it can replicate the style and structure in future user stories.
    """,
    expected_output="Insights on style, structure, and key elements from the good example ticket.",
    agent=good_example_analyzer,
    async_execution=True
)

# Analyze Feature Task
analyze_feature_task = Task(
    description="""
    Analyze the feature description and extract the following:
    * Context: What broader system or environment does this feature exist in?
    * Problem Statement: What specific issue or need is the feature addressing?
    * Target group and stakeholders: Who are the users or stakeholders involved?
    * Goals/Benefit: What are the intended outcomes or benefits of this feature?
    """,
    expected_output="A structured summary of the feature’s key points, including context, problem statement, target audience, and goals.",
    agent=feature_analyzer,
    async_execution=True
)

# Parse Ticket Task
parse_ticket_task = Task(
    description=f"""
    Analyze the following ticket text and extract the following:
    * Ticket Name
    * Short Description
    * Dependencies (related tickets, features, epics, etc.)
    * Links (Confluence, Jira, or other relevant links)
    * Metadata (sprint information, epic links, affected versions)
    """,
    expected_output="A structured format containing the ticket name, short description, dependencies, links, and additional metadata.",
    agent=ticket_parser,
    async_execution=True
)

# Generate User Story Task
generate_user_story_task = Task(
    description=f"""
    Based on the insights from the good example ticket, feature text, and ticket information, generate:

    * A well-formed user story in the format: "As a <user role>, I want <goal/desire> so that <reason/benefit>."
    * A detailed description that incorporates the feature’s context, addressing any missing or unclear information.
    * Clear and specific acceptance criteria that cover functional, non-functional, and error-handling aspects.
    * Identify information that is missing or unclear, and explicitly prompt for clarification from stakeholders (e.g., "Ask the stakeholder which data should be archived").
    * Seamlessly integrate all relevant metadata (dependencies, links, epics, etc.) into the user story, description, and acceptance criteria without listing them as a separate section.
    """,
    expected_output="A well-structured user story with integrated metadata and prompts for clarification where needed.",
    agent=user_story_generator
)
