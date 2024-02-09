import os
import openai
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

openai.api_key = os.getenv('OPENAI_API_KEY')


def get_completion_from_messages (prompt, model="gpt-3.5-turbo", temperature=0.1):

    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature
    )

    return response.choices[0].message["content"]


messages = [
    {
        'role':'system',
        'content':'you are an assistant that speaks '
    },
    {
        'role':'user',
        'content':'tell me a joke'
    },
    {
        'role':'assistant',
        'content':'Why did the chicken cross the road?'
    },
    {
        'role':'user',
        'content':"I don't know"
    },
]


# def collect_messages(_):
#     prompt = inp.value_input
#     inp.value = ""
#     context.append({'role':'user', 'content':f"{prompt}"})
#     response = get_completion_from_messages(context)
#     context.append({'role':'assistant', 'content':f"{response}"})
#     panels.append(pn.Row('User: ', pn.pane.Markdown(prompt, width=600)))
#     panels.append(pn.Row('Assistant: ', pn.pane.Markdown(response, width=600)))

    return pn.Column(*panels)