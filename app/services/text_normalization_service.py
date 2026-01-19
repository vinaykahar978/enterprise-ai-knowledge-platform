import re


def normalize_text(text: str) -> str:
    # Replace line breaks with spaces
    text = text.replace("\n", " ")

    # Remove extra whitespace
    text = re.sub(r"\s+", " ", text)

    return text.strip()
