import os, requests, sys
from openai import OpenAI, APIError
import numpy as np
import cv2 as cv




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

def mirror_project():
   model = "llava-oneviosion" # <-- supports both text and images

print(cv.__version__)