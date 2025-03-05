# https://learnwithhasan.com/blog/create-ai-agents-with-python/
import pdb
from helper import HttpRequest, Endpoint
from requests_config import request_config
from actions import get_response_time, test
from prompts import system_prompt
from json_helpers import extract_json


request_config = request_config("models-gpt-4o-mini", "2024-08-01-preview")

url = "https://cld.akkodis.com/api/openai/deployments/{deployment-id}/chat/completions?api-version={api-version}"
param = {
        "deployment-id": "gpt-4o-mini",
        "api-version": "2024-08-01-preview",
    }

class_A = Endpoint(url, **param)
Endpoint_instance = HttpRequest(url, **param)

class_A.show()

#test_messages = [
#    {"role": "user", "content": "c'est quoi python"},
#    {"role": "user", "content": "c'est quoi rust"}
#]

available_actions = {
    "get_response_time": get_response_time,
    "test": test
}

user_prompt = "le temps de reponse de google.com" # "le temps de reponse de google.com in test context"
#user_prompt = "le temps de reponse de google.com test "
#user_prompt = "c'est quoi python"
messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": user_prompt},
]

# response = request_config.send_message(test_messages)
# print("AI Response:", response)

turn_count = 1
max_turns = 5

while turn_count < max_turns:
    print (f"Loop: {turn_count}")
    print("----------------------")
    turn_count += 1

    response = request_config.send_message(messages)

    print(response)

    json_function = extract_json(response)

    if json_function:
            function_name = json_function[0]['function_name']
            function_parms = json_function[0]['function_parms']
            if function_name not in available_actions:
                raise Exception(f"Unknown action: {function_name}: {function_parms}")
            print(f" -- running {function_name} {function_parms}")
            action_function = available_actions[function_name]
            #call the function
            result = action_function(**function_parms)
            function_result_message = f"Action_Response: {result}"
            messages.append({"role": "user", "content": function_result_message})
            print(function_result_message)
    else:
         break