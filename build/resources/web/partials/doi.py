TEXT = """\
:::{.text-muted}
Full Title: {{< meta full-title >}}

Authors: {{< meta rg-authors >}}

::: {.citations-counter}
<span class="__dimensions_badge_embed__" data-doi=DATA_DOI data-legend="never" data-style="large_rectangle"></span><script async src="https://badge.dimensions.ai/badge.js" charset="utf-8"></script>
:::

DOI: {{< meta citation.doi >}}&nbsp;&nbsp;&nbsp;&nbsp;Version: 1.1

{{< meta translations >}}
:::
"""

def create_web(guideline):
    return TEXT.replace('DATA_DOI', guideline.doi)
