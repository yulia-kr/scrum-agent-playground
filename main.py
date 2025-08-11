from crewai import Crew
from crew.agents import feature_analyzer, ticket_parser, user_story_generator, good_example_analyzer
from crew.tasks import analyze_feature_task, parse_ticket_task, generate_user_story_task, analyze_good_example_task
from utils.pdf_utils import extract_text_from_pdf

def process_pdf_tasks(feature_pdf, ticket_pdf, good_example_pdf):
	# Extract text from the provided PDFs
	feature_text = extract_text_from_pdf(feature_pdf)
	ticket_text = extract_text_from_pdf(ticket_pdf)
	good_example_text = extract_text_from_pdf(good_example_pdf)
		
	# Ensure texts are valid
	if not feature_text or not ticket_text or not good_example_text:
		raise ValueError("PDF extraction failed: One or more PDFs returned empty text.")

	# Update task descriptions with extracted text
	analyze_feature_task.description = f"Analyze the following feature text:\n{feature_text}"
	parse_ticket_task.description = f"Analyze the following ticket text and extract dependencies, links, and metadata:\n{ticket_text}"
	analyze_good_example_task.description = f"Analyze the following good example ticket:\n{good_example_text}"

	# Instantiate the Crew with agents and tasks
	crew = Crew(
		agents=[feature_analyzer, ticket_parser, user_story_generator, good_example_analyzer],
		tasks=[analyze_feature_task, parse_ticket_task, analyze_good_example_task, generate_user_story_task]
	)

	# Execute the process
	result = crew.kickoff()


if __name__ == "__main__":
	# Example PDF file paths
	feature_pdf = ['PDF PATH']
	ticket_pdf = ['PDF PATH']
	good_example_pdf = ['PDF PATH']

	# Process the PDFs and save the result
	process_pdf_tasks(feature_pdf, ticket_pdf, good_example_pdf)
