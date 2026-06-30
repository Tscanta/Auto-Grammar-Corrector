import src.ai.providers as providers

from src.ai.gemini import correct_text as gemini_correct
from src.ai.ollama import correct_text as ollama_correct

def correct_text(text, mode):

    print(f"🤖 AI Provider: {providers.CURRENT_PROVIDER}")

    if providers.CURRENT_PROVIDER == "gemini":
        return gemini_correct(text, mode)
    
    if providers.CURRENT_PROVIDER == "ollama":
        return ollama_correct(text, mode)
    
    raise ValueError("Unknown AI provider")