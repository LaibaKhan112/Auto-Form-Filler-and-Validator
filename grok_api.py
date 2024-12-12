import os
from dotenv import load_dotenv
import openai

# Load the .env file
load_dotenv()

class GrokAPI:
    def __init__(self):
        # Set up the OpenAI API key
        openai.api_key = os.getenv("XAI_API_KEY")
        openai.api_base = "https://api.x.ai/v1"  # Grok's API base URL

    def validate_and_fill_form(self, form_data):
        """
        Sends form data to Grok for validation and auto-fill.
        :param form_data: Dictionary containing form fields (name, email, etc.)
        :return: Validated and auto-filled form data or error message
        """
        try:
            user_message = f"Validate and complete this tax form: {form_data}"

            response = openai.ChatCompletion.create(
                model="grok-beta",
                messages=[
                    {"role": "system", "content": "If any fields are missing or incorrect, provide recommended values to auto-fill the form."},
                    {"role": "user", "content": user_message},
                ],
            )

            raw_response = response.choices[0].message["content"]

            try:
                import json
                parsed_response = json.loads(raw_response)
            except json.JSONDecodeError:
                parsed_response = {"message": raw_response}

            return parsed_response
        except Exception as e:
            return {"error": str(e)}
