from tools import search_tool
from crewai import Task
from agents import news_researcher, news_writer

# Research task
# Tasks require the agent, the tool, description and expected output
research_task = Task(
  description=(
    "Identify most likely players to get a hit tonight {topic}."
    "Focus on the statistics of each player and probabilities of that person getting a hit against the starting pitchers."
    "Your final report should give players names and probability they will get a hit."
  ),
  expected_output='A comprehensive list of players names and probabilities of hits tonight.',
  tools=[search_tool],
  agent=news_researcher,
)


# Writing task with language model configuration

write_task = Task(
  description=(
    "Compose a list {topic}."
    "focus on the players names and stats as to why they are likely to get a hit tonight"
    "This article should be easy to understand, engaging, and positive."
  ),
  expected_output='statistics on each player',
  tools=[search_tool],
  agent=news_writer,
  async_execution=False,
  output_file='AI-article.md'  
)
