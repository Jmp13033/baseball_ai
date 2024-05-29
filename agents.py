from crewai import Agent
from langchain_google_genai import  ChatGoogleGenerativeAI
from tools import search_tool
#

## we need model as well as api key to get this to work
llm = ChatGoogleGenerativeAI(model="gemini-pro",
                             google_api_key=""
                             )


news_researcher=Agent(
    role="BaseBall Analyst",
    goal=' provide statistics about players {topic}',
    verbose=True,
    memory=True,
    backstory=(
        "Driven by uncovering statistical analysis."
        "innovation, eager to explore and share knowledge that could change"
        "the world."

    ),
    tools=[search_tool],
    llm=llm,
    allow_delegation=True
)

## creating a write agent with custom tools responsible in writing news blog

news_writer = Agent(
  role='Writer',
  goal='write a comprehensive list about {topic}',
  verbose=True,
  memory=True,
  backstory=(
    "With a flair for simplifying complex topics, you craft"
    "engaging narratives that captivate and educate, bringing new"
    "discoveries to light in an accessible manner."
  ),
  tools=[search_tool],
  llm=llm,
  allow_delegation=False
)





