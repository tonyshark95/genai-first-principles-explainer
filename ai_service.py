import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

class FirstPrinciplesAI:
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY not found in environment variables.")
        
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-2.5-flash')

    def deconstruct_topic(self, topic: str, temperature: float, complexity: str):
        """
        Generates a first-principles breakdown of a given topic using controlled 
        prompt injection for complexity and temperature tuning.
        """
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
            return "Error: Generation halted due to safety protocols. Please modify the topic."
        except Exception as e:
            return f"Service unavailable. Connection or API error. (Ref: {str(e)[:20]}...)"