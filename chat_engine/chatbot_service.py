# chatbot_service3.py
import pandas as pd
import openai

class ChatbotService:
    def __init__(self, api_key, excel_file):
        self.api_key = api_key
        self.excel_file = excel_file
        openai.api_key = api_key
        
        # Load the Excel file into a pandas DataFrame
        self.excel_data = pd.read_excel(excel_file)
        
        # Convert the DataFrame to a text representation
        self.data_text = self.excel_data.to_string(index=False)
        
    def send_message(self, message):
        # Add the data to the API prompt
        prompt = message + '\n' + self.data_text
        
        # Call the OpenAI API to send a message
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=1000,
            n=1,
            stop=None,
            temperature=0.7
        )
        
        # Return the response from the OpenAI API
        return response.choices[0].text.strip()