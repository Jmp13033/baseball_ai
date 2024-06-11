from tools import search_tool
from crewai import Task
from agents import news_researcher, news_writer

# Research task
# Tasks require the agent, the tool, description and expected output
research_task = Task(
  description=(
    "research topic {topic}."
  ),
  expected_output='comprehensive lst about the topic',
  tools=[search_tool],
  agent=news_researcher,
)


# Writing task with language model configuration

write_task = Task(
  description=(
    "Compose a list {topic}."
  ),
  expected_output='list of this topic',
  tools=[search_tool],
  agent=news_writer,
  async_execution=False,
  output_file='output.csv'  
)


