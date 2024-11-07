import os
import asyncio
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from src.workflows.car_assistant_workflow import CarAssistantWorkflow

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("FLASK_SECRET_KEY", "default_secret_key")

# Initialize workflow
workflow = CarAssistantWorkflow(timeout=30, verbose=True)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/send_message", methods=["POST"])
async def send_message():
    data = request.get_json()
    user_query = data.get("message", "")

    if user_query:
        # Run the workflow asynchronously
        result = await workflow.run(query=user_query)
        return jsonify({"response": result})

    return jsonify({"error": "No message provided"}), 400

if __name__ == "__main__":
    app.run(debug=True)
