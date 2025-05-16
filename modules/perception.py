def parse(text: str) -> dict:
    """
    trim whitespace and wrap the user input in a dict
    allows us to extend parsing later
    """
    cleaned = text.strip()
    return {"raw": cleaned}
