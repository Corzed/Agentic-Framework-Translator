# AI Agent Framework Translator

## Introduction
The AI Agent Framework Translator is a tool designed to convert AI agents between different frameworks using AI-powered translation, making it easier for developers to switch frameworks without rewriting code.

## Supported Frameworks
- LangChain (Docs to be added)
- CrewAI (Docs to be added)
- More frameworks can be added by contributors!

## Features
- **AI-Powered Translation**: Uses OpenAI's chat completion API (via o3-mini-high) to perform accurate translations.
- **Documentation Context**: Incorporates framework documentation from a JSON file to improve translation accuracy.
- **Extensible Architecture**: Contributors can easily add support for new frameworks by updating `frameworks_docs.json` and adding custom translation logic in `translators.py`.
- **Modular Design**: The code is split into separate files for ease of maintenance and contributions.

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/Corzed/Agentic-Framework-Translator.git
   cd Agentic-Framework-Translator
   ```
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Set your OpenAI API key in an environment variable named `OPENAI_API_KEY` or directly in the code.

## Usage
To translate an AI agent from one framework to another, run:
```
python translate.py --source <source_framework> --target <target_framework> --input <input_file> --output <output_file>
```
Example:
```
python translate.py --source langchain --target crewai --input agent_langchain.py --output agent_crewai.py
```

## Contribution Guidelines
Contributions are welcome!
- **Documentation**: Add or update framework documentation in the `frameworks_docs.json` file.
- **Translation Logic**: Enhance translation logic in `translators.py`.
- Please submit a pull request with your changes. For any questions, feel free to open an issue.
