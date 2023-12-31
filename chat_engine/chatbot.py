from flask import Flask, request, jsonify
from dotenv import load_dotenv
from flask_cors import CORS
from chatbot_service import ChatbotService
import os
import update

app = Flask(__name__)
CORS(app)  # Add this line to enable CORS
update.start()
chatbot_service = ChatbotService(api_key=os.getenv("OPENIA_KEY"), excel_file='output.xlsx')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data['message']
    response = chatbot_service.send_message(user_message)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run()
