from build import file 

def create_web(guideline):
    file.copy(guideline.repo_paths.author_bios, guideline.destination_paths.author_bios)
    return ''