import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

class FirstPrinciplesAI:
    def __init__(self):
        # Securely fetch the API key
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("API Key not found. Please check your .env file.")
        
        genai.configure(api_key=api_key)
        # Initialize the model
        self.model = genai.GenerativeModel('gemini-2.5-flash')

    # 1. Add 'temperature: float' to the required arguments
    def deconstruct_topic(self, topic: str, temperature: float, complexity: str):
        """
        Takes a topic, temperature, and complexity level to generate a customized breakdown.
        """
        # Dynamically change the system instruction based on the UI dropdown
        if complexity == "Explain Like I'm 5":
            instruction = "Use extremely simple language, everyday examples, and avoid all jargon."
        elif complexity == "University Level":
            instruction = "Use advanced terminology, academic rigor, and assume prior technical knowledge."
        else:
            instruction = "Use standard, clear structural logic avoiding unnecessary jargon."

        prompt = f"""
        Analyze the concept of '{topic}' using first-principles thinking.
        Audience/Tone Rule: {instruction}
        
        Follow this strict structure:
        1. Definition: Define the concept simply in one sentence.
        2. Foundational Truths: Break it down into 2-3 fundamental, indisputable facts.
        3. The 'Why': Build the explanation back up from those facts, explaining the 'why' at each logical step.
        """
        
        try:
            response = self.model.generate_content(
                prompt, 
                stream=True,
                generation_config=genai.types.GenerationConfig(
                    temperature=temperature,
                )
            )
            return response
        except genai.types.generation_types.StopCandidateException:
            # Catches if the AI generated something unsafe and stopped
            return "Error: The model halted generation due to safety protocols. Please try a different topic."
        except Exception as e:
            # Catches network timeouts or API key issues
            return f"System currently unavailable. Please check your connection or try again later. (Error Code: {str(e)[:20]}...)"