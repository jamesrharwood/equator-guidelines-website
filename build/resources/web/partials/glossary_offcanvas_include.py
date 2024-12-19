def create_web(guideline):
    return f"{{{{< include {guideline.relative_destination_paths.glossary_offcanvas} >}}}}"
