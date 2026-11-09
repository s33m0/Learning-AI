from dotenv import load_dotenv
import os
load_dotenv()

def main() -> None:
    print("Hello from langchain!")
    print("GEMINI_API_KEY:", os.getenv("GEMINI_API_KEY"))

if __name__ == "__main__":
    main()