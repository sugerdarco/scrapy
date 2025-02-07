import os
from google import genai
from google.genai import types
from dotenv import load_dotenv
load_dotenv()
def format_data(data, fields=None):
    client = genai.Client(api_key=os.getenv('GEMINI_API'))
    
    if fields is None:
        fields = ["id"]
    system_message = f"""You are an intelligent text extraction and conversion assistant. 
                        Your task is to extract structured information from the given text and convert it into a pure JSON format. 
                        The JSON should contain only the structured data extracted from the text, with no additional commentary, explanations, or extraneous information.
                        If any field is missing in the provided text, exclude it from the output instead of providing null values.
                        Return the output in valid JSON format with no words before or after the JSON.
                        """
    user_message = f"""Extract the following information from the provided text:
                        Page content: {data}
                        Information to extract: {fields}
                        """
    
    response = client.models.generate_content(
        model='gemini-1.5-flash',
        contents=user_message,
        config=types.GenerateContentConfig(
            system_instruction=system_message,
            response_mime_type= 'application/json'
        )
    )
    
    return response
