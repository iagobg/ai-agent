import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys
from functions.get_files_info import schema_get_files_info
from functions.get_file_content import schema_get_file_content
from functions.run_python import schema_run_python_file
from functions.write_file_content import schema_write_file
from functions.call_function import call_function

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)



if len(sys.argv) < 2:
    print("Error: No prompt given")
    sys.exit(1)
user_prompt = sys.argv[1]
messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
]

system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""

available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_run_python_file,
        schema_write_file
    ]
)

response = client.models.generate_content(
    model='gemini-2.0-flash-001',
    contents=messages,
    config=types.GenerateContentConfig(
        tools=[available_functions], system_instruction=system_prompt),
)

print(response.text)
if response.function_calls:
    for item in response.function_calls:
        try:
            function_call_result = call_function(item)
            if (
                hasattr(function_call_result, "parts") and
                len(function_call_result.parts) > 0 and
                hasattr(function_call_result.parts[0], "function_response") and
                hasattr(function_call_result.parts[0].function_response, "response")
            ):
                print(f"-> {function_call_result.parts[0].function_response.response}")
            else:
                raise ValueError("Missing expected response structure in function_call_result.")

        except Exception as e:
            raise RuntimeError(f"Function call failed: {e}")
# if response.function_calls:
#     print(f"TEST: {response.function_calls}")
#     for item in response.function_calls:    
#         print(item.args)
#         print(f"Calling function: {item.name}({item.args})")


if "--verbose" in sys.argv:
    print(f"User prompt: {user_prompt}")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")