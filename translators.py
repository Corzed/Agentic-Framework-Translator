import os
import json
import openai

def load_framework_docs():
    """
    Loads framework documentation from the frameworks_docs.json file.
    Contributors can update this file to add documentation for new frameworks.
    """
    docs_file = "frameworks_docs.json"
    if os.path.exists(docs_file):
        with open(docs_file, "r") as f:
            return json.load(f)
    else:
        return {}

def get_framework_doc(framework, docs):
    """
    Retrieves the documentation snippet for a specified framework.
    """
    return docs.get(framework.lower(), "Documentation not available for this framework.")

def ai_translate(source_framework, target_framework, agent_code, source_doc, target_doc):
    """
    Uses OpenAI's ChatCompletion API (with GPT-4) to translate agent code from the source framework
    to the target framework using provided documentation as context.
    """
    prompt = (
        f"Translate the following AI agent code from {source_framework} framework to {target_framework} framework.\n\n"
        f"Source Framework Documentation:\n{source_doc}\n\n"
        f"Target Framework Documentation:\n{target_doc}\n\n"
        f"Source Code:\n{agent_code}\n\n"
        "Translated Code:"
    )

    messages = [
        {"role": "system", "content": "You are an expert in translating AI agent code between different frameworks."},
        {"role": "user", "content": prompt}
    ]

    response = openai.chat.completions.create(
        model="o3-mini-high",
        messages=messages,
        temperature=0.3,
        max_tokens=1500
    )
    
    translated_code = response["choices"][0]["message"]["content"].strip()
    return translated_code

def translate_agent(source_framework, target_framework, agent_code):
    """
    Translates agent code by loading relevant documentation and using the AI translation method.
    Contributors can add framework-specific logic here if needed.
    """
    docs = load_framework_docs()
    source_doc = get_framework_doc(source_framework, docs)
    target_doc = get_framework_doc(target_framework, docs)

    return ai_translate(source_framework, target_framework, agent_code, source_doc, target_doc)
