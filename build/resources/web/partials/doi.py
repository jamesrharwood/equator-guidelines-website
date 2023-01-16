TEXT = """\
::: {.citations-counter}
<span class="__dimensions_badge_embed__" data-doi=DOI data-legend="never" data-style="large_rectangle"></span><script async src="https://badge.dimensions.ai/badge.js" charset="utf-8"></script>
:::"""

def create_web(guideline):
    return TEXT.replace('DOI', guideline.doi)
