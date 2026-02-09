import argparse
import os
from tabnanny import verbose

from dotenv import load_dotenv
from google import genai
from google.genai import types


def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    parser = argparse.ArgumentParser(description="aiAgent")
    parser.add_argument("user_prompt", type=str, help="User input variable")
    parser.add_argument(
        "--verbose", action="store_true", help="Used to add additional info to response"
    )
    args = parser.parse_args()
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

    if api_key is None:
        raise RuntimeError("Please input api key into .env!")

    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model="gemini-2.5-flash", contents=f"{messages}"
    )
    if response.usage_metadata is None:
        raise RuntimeError("Possible API request failure?")

    if args.verbose:
        print(f"User prompt:{args.user_prompt}")
        print(f"Prompt tokens:{response.usage_metadata.prompt_token_count}")
        print(f"Response tokens:{response.usage_metadata.candidates_token_count}")

    print(response.text)


if __name__ == "__main__":
    main()
