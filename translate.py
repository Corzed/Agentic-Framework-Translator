import argparse
import os
import openai
from translators import translate_agent

# Set your OpenAI API key from the OPENAI_API_KEY environment variable or keep the fallback key here.
openai.api_key = os.getenv("OPENAI_API_KEY", "YOUR_OPENAI_API_KEY")

def main():
    parser = argparse.ArgumentParser(description="Translate AI agents between different frameworks.")
    parser.add_argument("--source", required=True, help="Source framework")
    parser.add_argument("--target", required=True, help="Target framework")
    parser.add_argument("--input", required=True, help="Input file containing the agent code")
    parser.add_argument("--output", required=True, help="Output file for the translated agent code")

    args = parser.parse_args()

    # Read the input file
    with open(args.input, "r") as infile:
        agent_code = infile.read()

    # Translate the agent code using AI translation
    try:
        translated_code = translate_agent(args.source, args.target, agent_code)
    except Exception as e:
        print(f"Error during translation: {e}")
        return

    # Write the translated code to the output file
    with open(args.output, "w") as outfile:
        outfile.write(translated_code)

    print(f"Translation from {args.source} to {args.target} completed. Output written to {args.output}")

if __name__ == "__main__":
    main()