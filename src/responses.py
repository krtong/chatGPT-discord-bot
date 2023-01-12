import os
import json
import openai
from asgiref.sync import sync_to_async
from dotenv import load_dotenv

# load environment variables from .env file
load_dotenv()

# read the OpenAI API key from the environment variables
openai_key = os.environ.get('OPENAI_KEY')

async def handle_response(message) -> str:
    openai.api_key = openai_key
    response = await sync_to_async(openai.Completion.create)(
        model="text-davinci-003",
        prompt=message,
        temperature=0.7,
        max_tokens=2048,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.0,
    )

    responseMessage = response.choices[0].text

    return responseMessage
