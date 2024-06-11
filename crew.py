from crewai import Crew,Process
from tasks import research_task,write_task
from agents import news_researcher,news_writer


## agents, task, process 
crew=Crew(
    agents=[news_researcher,news_writer],
    tasks=[research_task,write_task],
    process=Process.sequential,
)

## starting the task execution process wiht enhanced feedback

result=crew.kickoff(inputs={'topic':'Baseball players'})
print(result)