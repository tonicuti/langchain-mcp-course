from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_mcp_adapters.tools import load_mcp_tools
from langchain.agents import create_agent
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage

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
    args = ["C:/Itoni/mcp-course/langchain-mcp/src/langchain_mcp/server/math_server.py"],
)

async def main():
    async with stdio_client(stdio_server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            print("Session initialized.")
            
            tools = await load_mcp_tools(session)
            agent = create_agent(llm, tools)
            
            result = await agent.ainvoke({"messages": [HumanMessage(content="What's 2 + 2 * 3?")]})
            print("Agent result:", result["messages"][-1].content)

if __name__ == "__main__":
    asyncio.run(main())