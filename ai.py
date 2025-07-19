import os
import requests
from openai import OpenAI, APIError

try:
    from google.colab import userdata
    NRP_API_KEY = userdata.get('NRP_API_KEY')
except (ImportError, ModuleNotFoundError):
    NRP_API_KEY = os.environ.get("NRP_API_KEY")
    if not NRP_API_KEY:
        raise RuntimeError("API Key not found. Please set the NRP_API_KEY environment variable or run in Google Colab with secrets.")
except userdata.SecretNotFoundError:
    raise RuntimeError("API Key not found. Please add it to Colab Secrets as 'NRP_API_KEY'.")

BASE_URL = "https:llm.nrp-nautilus.io/v1"
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


Retrieve_models()


def connect_task():
   model = 'phi3' # <-- small model


def persona_task():
   model = 'gemma3' # <-- google reliable


def code_task():
   model = 'deepseek-r1' # <-- known for code


def JSON_mode():
   model = 'llama3' # <-- supports JSON with prompting


def mirror_project():
   model = 'llava-oneviosion' # <-- supports both text and images
