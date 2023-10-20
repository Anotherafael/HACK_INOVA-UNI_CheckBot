import openai
from fastapi import FastAPI
from dotenv import dotenv_values
from utils import Payload
import requests

app = FastAPI()

ENV = dotenv_values(".env")
openai.api_key = ENV['KEY']
# Perfil que o ChatGPT irá adotar para responder o usuário.
ai_profile_primary = ENV['PROFILE_PRIMARY']
ai_profile_secondary = ENV['PROFILE_SECONDARY']
openai.organization = ENV['ORGANIZATION']

user_input = "";
data = "";

def openai_chat(profile:str, user_prompt:str, data = ""):
    if profile == "primary":
        prompt = [
            {"role": "system", "content": ai_profile_primary},
            {"role": "user", "content": f"Dados de referência:\n {data}\n"},
            {"role": "user", "content": user_prompt},
        ]
    elif profile == "secondary":
        prompt = [
            {"role": "system", "content": ai_profile_secondary},
            {"role": "user", "content": user_prompt},
        ]
    try:
        response = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages = prompt,
            max_tokens = 500,
            n = 1,
            temperature = 0.8,
        )

        for choice in response.choices:
            if "text" in choice:
                return choice.text
        
        return response.choices[0].message.content
    except Exception as e:
        return "Ocorreu um problema na API do OpenAI. Alerte para a equipe de suporte."


@app.get("/")
async def read_root():
    # return {"message": "Welcome to the CheckBot API, which is based on ChatGPT 3.5."}
    return {"message": "Welcome to the CheckBot API, which is based on ChatGPT 3.5."}

@app.post("/userInput")
async def userInput(payload: Payload):
    if payload.user_input == "":
        return {"message": "Usuário não perguntou."}
    global user_input
    user_input = payload.user_input
    print('User enviou uma pergunta')
    
    keys = getKeysInUserInput()
    print(keys)
    request = requests.get("http://localhost:3000", json={"keys":keys})
    print('Webscrapp retornou.')
    print(request.text)

    response = getAiResponseToUser(request.text)
    return {"message": response}

def getAiResponseToUser(data):
    global user_input
    response = openai_chat(profile="primary", user_prompt=user_input, data=data)
    return response

def getKeysInUserInput():
    global user_input
    if user_input == "":
        return "Usuário não requisitou"
    else:
        response = openai_chat(profile="secondary", user_prompt=user_input)
        return response
    

