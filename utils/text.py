def strip_backticks(text: str, lang: str = "json") -> str:
    if text.startswith(f"```{lang}"):
        return text[3 + len(lang) : -3]
    return text