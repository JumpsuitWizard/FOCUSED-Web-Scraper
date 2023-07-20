def remove_at_symbol(text):
    if text is not None:
        if text.startswith('@@'):
            return text[2:]
        elif text.startswith('@'):
            return text[1:]
    return text
