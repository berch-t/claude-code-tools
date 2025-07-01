# Ollama API Documentation

## Overview
Ollama provides a REST API for running and managing large language models locally. The API is compatible with OpenAI's format and offers both streaming and non-streaming responses.

## Base URL
- Default: `http://localhost:11434`
- Chat API endpoint: `/api/chat`
- Generate API endpoint: `/api/generate`
- OpenAI-compatible endpoint: `/v1/chat/completions`

## Chat Completion API

### Request Format (/api/chat)
```json
{
  "model": "model_name",
  "messages": [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello!"}
  ],
  "stream": false,
  "options": {
    "temperature": 0.7,
    "top_p": 0.9
  }
}
```

### Response Format
```json
{
  "model": "model_name",
  "created_at": "2023-08-04T08:52:19.385406455-07:00",
  "message": {
    "role": "assistant",
    "content": "Hello! How can I help you today?"
  },
  "done": true,
  "total_duration": 5191566416,
  "load_duration": 2154458,
  "prompt_eval_count": 26,
  "prompt_eval_duration": 383809000,
  "eval_count": 298,
  "eval_duration": 4799921000
}
```

## Python Integration Examples

### Using Python Requests
```python
import requests
import json

url = "http://localhost:11434/api/chat"
headers = {"Content-Type": "application/json"}

data = {
    "model": "qwq:latest",
    "messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello!"}
    ],
    "stream": False
}

response = requests.post(url, headers=headers, data=json.dumps(data))
if response.status_code == 200:
    result = response.json()
    print(result['message']['content'])
```

### Using Ollama Python Library
```python
import ollama

response = ollama.chat(
    model='qwq:latest',
    messages=[
        {'role': 'user', 'content': 'Why is the sky blue?'}
    ]
)
print(response['message']['content'])
```

### Using OpenAI-Compatible API
```python
from openai import OpenAI

client = OpenAI(
    base_url='http://localhost:11434/v1',
    api_key='ollama',  # required, but unused
)

response = client.chat.completions.create(
    model="qwq:latest",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello!"}
    ]
)
print(response.choices[0].message.content)
```

## Streaming Responses
Set `stream=True` in the request to get streaming responses:

```python
import ollama

response = ollama.chat(
    model='qwq:latest',
    messages=[{'role': 'user', 'content': 'Tell me a story'}],
    stream=True
)

for chunk in response:
    print(chunk['message']['content'], end='', flush=True)
```

## Model Management
- List models: `GET /api/tags`
- Pull model: `POST /api/pull`
- Push model: `POST /api/push`
- Delete model: `DELETE /api/delete`

## Error Handling
- 404: Model not found
- 400: Bad request format
- 500: Internal server error

## Notes
- Ensure Ollama is running locally before making API calls
- Models must be pulled/downloaded before use
- Default port is 11434
- API supports multimodal models for image inputs