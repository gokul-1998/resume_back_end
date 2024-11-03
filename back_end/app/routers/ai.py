from fastapi import APIRouter

router = APIRouter(tags=['AI'], prefix="/api")


@router.get("/ai/rephrase/")
def rephrase():
    return {"message": "Hello World"}


import requests

API_URL = "https://api-inference.huggingface.co/models/meta-llama/Llama-3.2-1B"
headers = {"Authorization": "Bearer hf_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
output = query({
	"inputs": "Can you please let us know more details about your ",
})