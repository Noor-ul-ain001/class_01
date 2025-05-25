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
    name = 'Translator Agent',
    instructions= 
    """You are a translator agent. Translate provided text to urdu, english .
    Do not add labels like 'Urdu:' and 'English:'. Just provide the translated sentences in separate lines. Make sure the Urdu sentence comes first and uses correct native Urdu grammar and order.
"""
)

response = Runner.run_sync(
    writer,
    input = 'generate random paragraph?',
    run_config = config
    )
print(response.final_output)