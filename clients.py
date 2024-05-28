import json
import requests
from datetime import datetime

class ollama_client():
    def __init__(self, api_url, model):
        self.model = model
        self.url = api_url
    def first_request(self, prompt):
         return self.send_request(prompt)

    def send_request(self,  prompt):
        headers = { 'Content-Type': 'application/json' }
        payload = { "model": self.model, "prompt": prompt}
        response = requests.post(api_url, data=json.dumps(payload), headers=headers)
        
        if response.status_code == 200:
            json_objects = response.text.strip().split('\n')
            deserialized_data = []
            for json_str in json_objects:
                deserialized_data.append(json.loads(json_str))
            response = ""
            # Output the deserialized data
            for item in deserialized_data:
                response += item['response']
            return response

api_url = "http://localhost:11434/api/generate"

Agent1 = ollama_client(api_url, "Agent1:latest")
Agent2 = ollama_client(api_url, "Agent2:latest")

ESC = chr(27) 
BLUE = ESC + "[1m" 
NORMAL = ESC + "[0m" 


Agent1Response = "Showtime"
Agent2Response = "Showtime"

while True:
    Agent1Response = Agent1.send_request(Agent2Response)
    print(BLUE + "Agent1:" + NORMAL)
    print(Agent1Response)
    Agent2Response = Agent2.send_request(Agent1Response)
    print(BLUE + "Agent2:" + NORMAL)
    print(Agent2Response)
