import os
import requests
from openai import OpenAI, APIError
import sys


try:
    from google.colab import userdata
    NRP_API_KEY = userdata.get('NRP_API_KEY')
except (ImportError, ModuleNotFoundError):
    NRP_API_KEY = os.environ.get("NRP_API_KEY")
    if not NRP_API_KEY:
        raise RuntimeError("API Key not found. Please set the NRP_API_KEY environment variable or run in Google Colab with secrets.")
except userdata.SecretNotFoundError:
    raise RuntimeError("API Key not found. Please add it to Colab Secrets as 'NRP_API_KEY'.")

BASE_URL = "https://llm.nrp-nautilus.io/v1"
client = OpenAI(
    api_key=NRP_API_KEY,
    base_url=BASE_URL
)

def Retrieve_models():
  ml = []
  models = client.models.list()
  for model in models.data:
    ml.append(f"{model.id}")

  sort_models = sorted(ml)

  for x in sort_models:
    print(x)


#connection
def connect_task():
    completion = client.chat.completions.create(
    model="phi3",
    messages=[
        {"role": "warm individual", "content": "respond to input"},
        {
            "role": "user",
            "content": input("talk to me: "),
        },
    ],
)

    print(completion.choices[0].message.content)


#switch personalities
def persona_task():
    rp = input("a or b, pick your poison: ").lower()
    if rp != "a" and rp != "b":
      sys.exit("please choose persona 'a' or 'b'")
    elif rp == "a":
    
      a_completion = client.chat.completions.create(
      model= "llama3", ##**dont use google It doesn't use the same format**
      messages=[
          {"role": "system", "content": "respond to input as a cowboy"},
          {
              "role": "user",
              "content": input("talk to me: "),
          },
      ],
  )
      print(a_completion.choices[0].message.content)

    elif rp == "b":

      b_completion = client.chat.completions.create(
      model= "llama3", ##**dont use google It doesn't use the same format**
      messages=[
          {"role": "system", "content": "you only speak in spanish, you don't understand English, act confused."},
          {
              "role": "user",
              "content": input("talk to me: "),
          },
      ],
  )

      print(b_completion.choices[0].message.content)


#code explainer au natural
def code_task_org():
    query = input("tell me, young padawan: ")
    completion = client.chat.completions.create(
    model = "deepseek-r1", # <-- known for code
    messages=[
        {"role": "Coding expert", 
         "content": "you simply explain what code given aims to do at the most beginner level succinctly."},
        {
            "role": "user",
            "content": f"what does this mean: {query}, Restrict your answer to a maximum of a paragraph.",
        },
    ],
)

    print(completion.choices[0].message.content)


#code explainer taken from spoiler
def code_task_cheat():
    print("\n--- Task 4: The Code Explainer ---")
try:
    code_snippet = "short_names = [name for name in names if len(name) < 5]"
    code_explanation = client.chat.completions.create(
        model='deepseek-r1',
        messages=[
            {"role": "system", "content": "You are an expert Python programmer who excels at explaining complex code to beginners in simple terms."},
            {"role": "user", "content": f"Please explain what this line of Python code does: ```{code_snippet}```"}
        ]
    )
    print(code_explanation.choices[0].message.content)
except APIError as e:
    print(f"An API error occurred: {e}")

def JSON_model():
   model = "llama3" # <-- supports JSON with prompting



code_task_org()
code_task_cheat()