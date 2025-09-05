
def create_web(guideline):
    aliases = guideline.config.get('aliases', [])
    if not aliases:
        return ''
    aliases = [f'{alias}' for alias in aliases]
    item_line_start = '\n    - '
    aliases = item_line_start.join(aliases)
    aliases = f'aliases:{item_line_start}{aliases}' if aliases else ''
    metadata = f'---\n{aliases}\n---'
    return metadata