# 🧩 GenAI First-Principles Deconstructor

## Overview
This is a generative AI micro-application designed to break down complex topics into their fundamental, indisputable truths using first-principles thinking. It utilizes a modular architecture to separate the frontend interface from the backend AI services.

## Tech Stack
* **Language:** Python 3.x
* **Frontend:** Streamlit (Reactive UI)
* **AI Engine:** Google Gemini 2.5 Flash Large Language Model
* **Security:** Python-dotenv for environment variable management

## Architecture Design
The project avoids a monolithic script design by separating concerns:
* `app.py`: Handles the presentation layer, user state, and asynchronous streaming UI.
* `ai_service.py`: Contains the business logic, API authentication, and prompt engineering framework.
* `.env`: Secures the API credentials.

## How to Run Locally
1. Clone the repository and navigate to the project directory.
2. Install dependencies: `pip install -r requirements.txt`
3. Create a `.env` file and add your Google Gemini API key: `GEMINI_API_KEY=your_key_here`
4. Launch the application: `streamlit run app.py`