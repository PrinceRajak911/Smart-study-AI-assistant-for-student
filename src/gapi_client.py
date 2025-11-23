# src/gapi_client.py
import os
from dotenv import load_dotenv

# google-genai SDK import
try:
    from google import genai
except Exception:
    raise ImportError("google-genai package not found. Install with: pip install google-genai")

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
DEFAULT_MODEL = os.getenv("GEMINI_MODEL", "gemini-1.5-pro")

if not API_KEY:
    raise EnvironmentError(
        "GEMINI_API_KEY not found in environment. Create a .env file and add your key."
    )

client = genai.Client(api_key=API_KEY)


def generate_text(
    prompt: str,
    model: str = DEFAULT_MODEL,
    max_output_tokens: int = 512,
    temperature: float = 0.2
):
    """
    Generate text using Gemini via the updated google-genai SDK.
    NOTE: The new SDK does NOT accept `generation_config=` dicts.
    All generation parameters must be passed directly.
    """

    response = client.models.generate_content(
        model=model,
        contents=prompt,          # correct argument name
        max_output_tokens=max_output_tokens,
        temperature=temperature
    )

    # Extract response text safely
    try:
        return response.text
    except Exception:
        parts = []
        if hasattr(response, "candidates"):
            for c in response.candidates:
                if hasattr(c, "content"):
                    parts.append(c.content)
        return "\n".join(parts) if parts else str(response)


def embed_texts(texts, model: str = "embed-text-1.0"):
    """Return list of embeddings for input texts."""
    emb_resp = client.embeddings.create(
        model=model,
        input=texts
    )
    return [item.embedding for item in emb_resp.data]
