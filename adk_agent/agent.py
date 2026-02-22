import yaml
from dotenv import load_dotenv

from google.adk.agents import LlmAgent

load_dotenv()

def load_agent_config(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

config = load_agent_config("./adk_agent/agent_config.yaml")

root_agent = LlmAgent(
    name=config["agent"]["name"],
    description=config["agent"]["description"],
    model=config["model"]["name"],
    instruction=config["instruction"],
)
