import pandas as pd
import openai

class ChatbotService:
    def __init__(self, api_key, excel_file):
        self.api_key = api_key
        self.excel_file = excel_file
        openai.api_key = api_key
        
        # Load the Excel file into a pandas DataFrame
        self.excel_data = pd.read_excel(excel_file)

        # Fill empty cells in populated rows
        self.excel_data.fillna("", inplace=True)
        
        # Convert the DataFrame to a text representation
        self.data_text = self.excel_data.to_string(index=False)
        
    def send_message(self, message):
        # Add the data to the API prompt
        prompt = self.data_text + '\n' + message
        
        # Call the OpenAI API to send a message
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0613",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1000,
            n=1,
            stop=None,
            temperature=0.5
        )
        
        # Return the response from the OpenAI API
        return response['choices'][0]['message']['content']
