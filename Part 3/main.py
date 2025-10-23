import os
from google import genai
from groq import Groq

# --- ANSI Color Codes for Readability ---
class Colors:
    LLAMA = '\033[94m'  # Blue
    GEMINI = '\033[92m' # Green
    SYSTEM = '\033[93m' # Yellow
    RESET = '\033[0m'    # Reset

# --- 1. CONFIGURATION & CLIENT SETUP ---

try:
    # Get API keys from environment variables
    GROQ_API_KEY = ""
    GEMINI_API_KEY = ""

    if not GROQ_API_KEY:
        print(f"{Colors.SYSTEM}Warning: GROQ_API_KEY not found. Llama will fail.{Colors.RESET}")
    
    if not GEMINI_API_KEY:
        print(f"{Colors.SYSTEM}Warning: GEMINI_API_KEY not found. Gemini will fail.{Colors.RESET}")

    # Initialize Groq client (for Llama)
    groq_client = Groq(api_key=GROQ_API_KEY)
    
    # Configure Gemini client  
    genai_client = genai.Client(api_key=GEMINI_API_KEY)  # NEW: Create the Gemini client instance
    GEMINI_MODEL_NAME = "gemini-2.5-flash"  # or latest production model as desired
    
except Exception as e:
    print(f"Error during initialization: {e}")
    exit(1)

# --- 2. DEFINE MODELS AND PERSONALITIES ---

LLAMA_MODEL = "llama-3.1-8b-instant"
MAX_TURNS = 5 # Set a limit for the chat loop (5 turns = 5 Llama attempts, 5 Gemini reviews)

# This is the placeholder for the problem (d[2]['question'])
# I've used a simple HumanEval problem.
INITIAL_PROBLEM = """
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    \"\"\" Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    \"\"\"
"""

# System prompt for Llama (The Coder)
LLAMA_SYSTEM_PROMPT = {
    "role": "system",
    "content": "You are a junior Python developer. You will be given a programming problem. First, outline a plan to solve it. Second, write the Python function based on your plan. You must implement the feedback from the senior developer (Gemini)."
}

# System prompt for Gemini (The Supervisor)
GEMINI_SYSTEM_PROMPT = {
    "role": "system",
    "content": """You are a senior developer and expert code reviewer. A junior developer (Llama) will provide you with a plan and a code solution. Your job is to supervise this output.
1.  Review their plan. Is it logical?
2.  Review their code. Is it correct? Does it match the plan? Does it handle edge cases? Are there bugs?
3.  Provide clear, concise, actionable feedback, but do not give the solution right away. 
4.  If the code is 100% correct and robust, end your message with "LGTM!" (Looks Good To Me!). Otherwise, do NOT say this."""
}


# --- 3. API CALL FUNCTIONS ---

def call_llama(messages):
    """Calls the Groq API (Llama) with a list of messages."""
    try:
        completion = groq_client.chat.completions.create(
            model=LLAMA_MODEL,
            messages=messages,
            temperature=0.7,
            max_tokens=1024,
            # max_completion_tokens=1024,
            top_p=1,
            stream=False,
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"Error calling Llama: {e}"

def call_gemini(messages):
    """Calls the Gemini API with a list of messages, translating roles."""

    # Send only 'user' and 'model' roles to Gemini, skip 'system'.
    gemini_history = []
    for msg in messages:
        if msg["role"] == "system":
            continue  # Gemini does NOT support system roles
        role = "model" if msg["role"] == "assistant" else msg["role"]
        gemini_history.append({"role": role, "parts": [{"text": msg["content"]}]})

    try:
        response = genai_client.models.generate_content(
            model=GEMINI_MODEL_NAME,
            contents=gemini_history
        )
        return response.text
    except Exception as e:
        return f"Error calling Gemini: {e}"


# --- 4. THE MAIN CHAT LOOP ---

def main_chat_loop():
    print(f"{Colors.SYSTEM}--- Starting Supervised Chat Loop ---{Colors.RESET}")
    print(f"{Colors.SYSTEM}Problem to solve:\n{INITIAL_PROBLEM}{Colors.RESET}")

    # The shared chat history
    # We start with the system prompts for both
    chat_history = []
    
    # This is the "user" prompt for the *next* turn
    current_input = INITIAL_PROBLEM
    
    for i in range(MAX_TURNS):
        print(f"\n{Colors.SYSTEM}--- Turn {i+1} ---{Colors.RESET}")

        # --- LLAMA'S TURN (CODE) ---
        print(f"{Colors.LLAMA}Llama (Junior Developer) is thinking...{Colors.RESET}")
        
        # Prepare messages for Llama: System + History + New Input
        llama_messages = [LLAMA_SYSTEM_PROMPT] + chat_history + [{"role": "user", "content": current_input}]
        
        llama_output = call_llama(llama_messages)
        
        print(f"{Colors.LLAMA}Llama:{Colors.RESET}\n{llama_output}")
        
        # Update shared history
        chat_history.append({"role": "user", "content": current_input})
        chat_history.append({"role": "assistant", "content": llama_output})


        # --- GEMINI'S TURN (SUPERVISE) ---
        print(f"\n{Colors.GEMINI}Gemini (Supervisor) is reviewing...{Colors.RESET}")

        # Prepare messages for Gemini: System + Full History
        gemini_messages = [GEMINI_SYSTEM_PROMPT] + chat_history
        
        gemini_output = call_gemini(gemini_messages)
        
        print(f"{Colors.GEMINI}Gemini:{Colors.RESET}\n{gemini_output}")

        # Check for approval
        if "LGTM!" in gemini_output:
            print(f"\n{Colors.SYSTEM}--- Gemini approved the code! Ending loop. ---{Colors.RESET}")
            break
        
        # Update shared history: Gemini's critique becomes the *next input* for Llama
        chat_history.append({"role": "user", "content": gemini_output})
        current_input = gemini_output
    
    else:
        print(f"\n{Colors.SYSTEM}--- Max turns ({MAX_TURNS}) reached. Ending loop. ---{Colors.RESET}")

if __name__ == "__main__":
    main_chat_loop()