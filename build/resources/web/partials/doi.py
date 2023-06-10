TEXT = """\
["At our journal, we ensure all authors follow reporting guidelines as this makes articles easier for readers to understand and faster to publish." [Fiona Ludlow - Editor in Chief]{.attribution}]{.aside}

::: {.hero-banner}
::: {.content-block}
::: {.section}

{{< include partials/why_use.md >}}

::: {.citations-counter}
<span class="__dimensions_badge_embed__ badge-inline" data-doi=DATA_DOI data-legend="never" data-style="large_rectangle"></span>
<span type="button" class="badge-inline btn btn-sm journal-endorsement">Journal endorsements</span>
<span class="journal-endorsement journal-endorsement-count">500+</span>
<script async src="https://badge.dimensions.ai/badge.js" charset="utf-8"></script>
:::
:::{.text-small}
Full Title: {{< meta full-title >}}

Authors: {{< meta rg-authors >}}

DOI: {{< meta citation.doi >}}&nbsp;&nbsp;&nbsp;&nbsp;Version: 1.1

{{< meta translations >}}
:::
:::
:::
:::
"""

def create_web(guideline):
    return TEXT.replace('DATA_DOI', guideline.doi)
