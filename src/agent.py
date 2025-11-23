# src/agent.py
from gapi_client import generate_text

def explain_topic(topic: str, level: str = "highschool") -> str:
    prompt = (
        f"Explain the topic '{topic}' in simple, step-by-step language suitable for a {level} student. "
        "Include definitions, a short example, and a 2–3 bullet summary at the end."
    )
    return generate_text(prompt, max_output_tokens=600)


def summarize_text(text: str, max_sentences: int = 6) -> str:
    prompt = (
        f"Summarize the following text into {max_sentences} concise bullet points:\n\n{text}"
    )
    return generate_text(prompt, max_output_tokens=400)


def create_quiz(topic: str, num_questions: int = 10) -> str:
    prompt = (
        f"Create {num_questions} multiple-choice questions for the topic '{topic}'. "
        "For each question provide 4 choices, mark the correct answer, and give a one-sentence explanation."
    )
    return generate_text(prompt, max_output_tokens=900)


def make_notes(text: str) -> str:
    prompt = (
        "Convert the following text into neat study notes with headings, bullet points, key formulas, and examples:\n\n"
        + text
    )
    return generate_text(prompt, max_output_tokens=700)