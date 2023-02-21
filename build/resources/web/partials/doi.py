TEXT = """\
:::{.text-muted}
Version: 1.1   
DOI: 10.1234/equator/1010101
:::

::: {.citations-counter}
<span class="__dimensions_badge_embed__" data-doi=DATA_DOI data-legend="never" data-style="large_rectangle"></span><script async src="https://badge.dimensions.ai/badge.js" charset="utf-8"></script>
:::"""

def create_web(guideline):
    return TEXT.replace('DATA_DOI', guideline.doi)
