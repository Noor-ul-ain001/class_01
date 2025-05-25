import os 
from dotenv import load_dotenv
from agents import Agent, AsyncOpenAI, OpenAIChatCompletionsModel, Runner, RunConfig


load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")
# print(gemini_api_key)

if not gemini_api_key:
    raise ValueError("gemini api key not found ")


external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)


model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

writer = Agent(
    name = 'Writer Agent',
    instructions= 
    """You are a writer agent. Generate poem,
    stories, essay, email etc."""
)

response = Runner.run_sync(
    writer,
    input = 'Write a 2 paragraph essay on Generative AI..',
    run_config = config
    )
print(response.final_output)