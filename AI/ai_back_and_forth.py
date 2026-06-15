import requests
from time import sleep

# Define the exposed local Docker engine endpoint
url = "http://localhost:12434/engines/v1/chat/completions"

# Get user prompt
prompt = input("Enter to start: ")


mistral_prompt = "You are arguing with me in a sales negotiation. You are selling me a car. Introduce this scenario, then kick off the negotiations with car details and a starting price. When introducing this scenario, be clear that YOU are selling the car and that I am buying the car."
qwen_prompt = None

for _ in range(3):
    payload_mistral = {
        "model": "ai/mistral:latest",
        "messages": [
            {"role": "user", "content": mistral_prompt}
        ],
        "temperature": 0.7
    }


    try:
        # Send the POST request with the JSON payload
        mistral_response = requests.post(url, json=payload_mistral)

        # Verify HTTP status 200 (Raises an HTTPError if the response was an error status)
        mistral_response.raise_for_status()

        # Parse the JSON response body
        mistral_result = mistral_response.json()

        # Extract message from the nested structural response schema
        mistral_answer = mistral_result["choices"][0]["message"]["content"]
        qwen_prompt = mistral_answer
        print("\n\nMistral:\n", mistral_answer)
    except requests.exceptions.RequestException as e:
        print(f"HTTP Request Failed: {e}")



    payload_qwen = {
        "model": "ai/smollm2:latest",
        "messages": [
            {"role": "user", "content": qwen_prompt}
        ],
        "temperature": 0.7
    }

    try:
        # Send the POST request with the JSON payload
        qwen_response = requests.post(url, json=payload_qwen)

        # Verify HTTP status 200 (Raises an HTTPError if the response was an error status)
        qwen_response.raise_for_status()

        # Parse the JSON response body
        qwen_result = qwen_response.json()

        # Extract message from the nested structural response schema
        qwen_answer = qwen_result["choices"][0]["message"]["content"]
        mistral_prompt = qwen_answer
        print("\n\nSmolLM:\n", qwen_answer)
    except requests.exceptions.RequestException as e:
        print(f"HTTP Request Failed: {e}")

