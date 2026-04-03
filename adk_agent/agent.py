import yaml
from dotenv import load_dotenv

from google.adk.agents import LlmAgent
from google.adk.tools.mcp_tool import McpToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams
from mcp import StdioServerParameters


load_dotenv()


def load_agent_config(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

config = load_agent_config("./adk_agent/agent_config.yaml")

server = StdioServerParameters(
    command="python",
    args=["-u", "./mcp_server/server.py"],
)

mcp_toolset = McpToolset(
    connection_params=StdioConnectionParams(
        server_params=server
    )
)

root_agent = LlmAgent(
    name=config["agent"]["name"],
    description=config["agent"]["description"],
    model=config["model"]["name"],
    instruction=config["instruction"],
    tools=[mcp_toolset],
)
