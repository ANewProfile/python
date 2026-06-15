import requests

# Define the exposed local Docker engine endpoint
url = "http://localhost:12434/engines/v1/chat/completions"

# Get user prompt
prompt = input("Enter your prompt: ")

# Construct standard OpenAI-compatible payload structure
payload = {
    "model": "ai/mistral:latest",
    "messages": [
        {"role": "user", "content": prompt}
    ],
    "temperature": 0.7
}

try:
    # Send the POST request with the JSON payload
    response = requests.post(url, json=payload)

    # Verify HTTP status 200 (Raises an HTTPError if the response was an error status)
    response.raise_for_status()

    # Parse the JSON response body
    result = response.json()

    # Extract message from the nested structural response schema
    answer = result["choices"][0]["message"]["content"]
    print("Your prompt:\n", prompt)
    print("\n\n")
    print("LLM Response:\n", answer)
except requests.exceptions.RequestException as e:
    print(f"HTTP Request Failed: {e}")
