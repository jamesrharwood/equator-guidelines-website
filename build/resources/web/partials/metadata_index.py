from build.paths import GUIDELINES_DIR

def create_web(guideline):
    aliases = guideline.config.get('aliases', [])
    aliases = [f'{GUIDELINES_DIR}/{alias}' for alias in aliases]
    aliases = '\n- '.join(aliases)
    aliases = f'aliases:\n- {aliases}' if aliases else ''
    metadata = f'---\n{aliases}\n---'
    return metadata