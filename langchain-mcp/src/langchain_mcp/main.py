from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_mcp_adapters.tools import load_mcp_tools
from langchain.agents import create_agent
from langchain_ollama import ChatOllama

from dotenv import load_dotenv
import asyncio
import os

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

load_dotenv()

llm = ChatOllama(
    model = "qwen3:1.7b",
    temperature = 0
)

stdio_server_params = StdioServerParameters(
    command = "python",
    args = ["C:/Itoni/mcp-course/langchain-mcp/src/langchain_mcp/server/weather_server.py"],
)

async def main():
    print("Starting MCP client...")

if __name__ == "__main__":
    asyncio.run(main())