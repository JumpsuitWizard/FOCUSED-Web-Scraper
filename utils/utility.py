def remove_at_symbol(text):
    if text.startswith('@@'):
        return text[2:]
    elif text.startswith('@'):
        return text[1:]
    else:
        return text
