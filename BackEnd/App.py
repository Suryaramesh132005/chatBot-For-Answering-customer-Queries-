from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

# Simple rule-based knowledge base
knowledge_base = {
    "greetings": [
        "Hello! How can I assist you today?",
        "Hi there! What can I do for you?",
        "Welcome! How may I help you?"
    ],
    "goodbye": [
        "Goodbye! Have a great day!",
        "Thank you for chatting with us. Goodbye!",
        "See you later! Don't hesitate to reach out if you have more questions."
    ],
    "help": [
        "I can help with account issues, product information, order status, and general questions.",
        "I'm here to assist with your questions about our products and services.",
        "How can I help you today? I can provide information about orders, products, and more."
    ],
    "account": [
        "For account-related issues, please visit the 'My Account' section on our website or contact support@example.com.",
        "You can reset your password by clicking 'Forgot Password' on the login page.",
        "Account settings can be changed in the 'Profile' section of your account."
    ],
    "order": [
        "You can check your order status in the 'My Orders' section of your account.",
        "For order inquiries, please have your order number ready and contact support@example.com.",
        "Shipping times vary by location. You'll receive a tracking email once your order ships."
    ],
    "product": [
        "Our products come with a 30-day money-back guarantee.",
        "Product specifications can be found on each product's detail page.",
        "For product availability, please check the product page or contact our sales team."
    ],
    "payment": [
        "We accept Visa, MasterCard, American Express, and PayPal.",
        "Payment issues can often be resolved by trying a different payment method.",
        "For payment-related questions, please contact billing@example.com."
    ],
    "default": [
        "I'm not sure I understand. Could you rephrase that?",
        "I don't have information on that topic. Could you ask something else?",
        "I'm still learning. Could you try asking a different question?"
    ]
}

def get_bot_response(user_message):
    user_message = user_message.lower()
    if any(word in user_message for word in ["hello", "hi", "hey", "greetings"]):
        return random.choice(knowledge_base["greetings"])
    if any(word in user_message for word in ["bye", "goodbye", "see you", "later"]):
        return random.choice(knowledge_base["goodbye"])
    if any(word in user_message for word in ["help", "support", "assistance"]):
        return random.choice(knowledge_base["help"])
    if any(word in user_message for word in ["account", "login", "password", "sign in"]):
        return random.choice(knowledge_base["account"])
    if any(word in user_message for word in ["order", "track", "shipping", "delivery"]):
        return random.choice(knowledge_base["order"])
    if any(word in user_message for word in ["product", "item", "spec", "feature"]):
        return random.choice(knowledge_base["product"])
    if any(word in user_message for word in ["payment", "pay", "credit card", "bill"]):
        return random.choice(knowledge_base["payment"])
    return random.choice(knowledge_base["default"])

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message', '')
    bot_response = get_bot_response(user_message)
    return jsonify({'response': bot_response})

if __name__ == '__main__':
    app.run(debug=True)