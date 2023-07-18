import os
from langchain.agents import create_csv_agent

from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.agents.agent_types import AgentType

# Initialize OpenAI client
os.environ["OPENAI_API_KEY"] = <openai_api_key>

agent = create_csv_agent(
    OpenAI(temperature=0),
    "/Users/pranjalsmacbook/Downloads/gamestop_data_2021_12.csv",
    verbose=True,
    agent_type= AgentType.ZERO_SHOT_REACT_DESCRIPTION,
)

agent.run("which game features the character 'Goku'?")
