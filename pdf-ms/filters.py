from re import finditer


def title(value):
    matches = finditer('.+?(?:(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])|$)', value)
    words = [m.group(0).title() for m in matches]
    return ' '.join(words)
