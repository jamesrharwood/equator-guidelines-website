from build.file import copy

def create_web(guideline):
    copy(guideline.repo_paths.why_use, guideline.destination_paths.why_use)
    return ''
