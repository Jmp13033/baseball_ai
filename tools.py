from dotenv import load_dotenv, find_dotenv
from crewai_tools import SerperDevTool
print(load_dotenv(find_dotenv()))
search_tool = SerperDevTool()


