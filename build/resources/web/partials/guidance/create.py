from .guidance import Guidance

from build import file

def create_web(guideline):
    guidance = Guidance(guideline)
    content = guidance.create_web()
    file.save_string(content, guideline.destination_paths.guidance)
    return f"{{{{< include {guideline.relative_destination_paths.guidance} >}}}}"
