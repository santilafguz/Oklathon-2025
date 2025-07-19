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

def vid_cap():
        cap = cv.VideoCapture(0)
    if not cap.isOpened():
        print("Cannot open camera")
        exit()
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
 
        # if frame is read correctly ret is True
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        # Our operations on the frame come here
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        # Display the resulting frame
        cv.imshow('frame', gray)
        if cv.waitKey(1) == ord('q'):
            break
 
    # When everything done, release the capture
    cap.release()
    cv.destroyAllWindows()


vid_cap()