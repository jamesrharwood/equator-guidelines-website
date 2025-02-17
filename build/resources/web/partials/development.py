from build import file 

def create_web(guideline):
    file.copy(guideline.repo_paths.development, guideline.destination_paths.development)
    return ''