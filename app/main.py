import ingest
import search_agent 
import logs

import asyncio


REPO_OWNER = "dbt-labs"
REPO_NAME = "docs.getdbt.com"


def initialize_index():
    print(f"Starting AI FAQ Assistant for {REPO_OWNER}/{REPO_NAME}")
    print("Initializing data ingestion...")

    def filter(doc):
        pass

    index = ingest.index_data(REPO_OWNER, REPO_NAME, filter=None)
    print("Data indexing completed successfully!")
    return index


def initialize_agent(index):
    print("Initializing search agent...")
    agent = search_agent.init_agent(index, REPO_OWNER, REPO_NAME)
    print("Agent initialized successfully!")
    return agent


def main():
    index = initialize_index()
    agent = initialize_agent(index)
    print("\nReady to answer your questions!")
    print("Type 'stop' to exit the program.\n")

    while True:
        question = input("Your question: ")
        if question.strip().lower() == 'stop':
            print("Goodbye!")
            break

        print("Processing your question...")
        response = asyncio.run(agent.run(user_prompt=question))
        logs.log_interaction_to_file(agent, response.new_messages())

        print("\nResponse:\n", response.output)
        print("\n" + "="*50 + "\n")


if __name__ == "__main__":
    main()
