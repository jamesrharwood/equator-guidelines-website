TEXT = """\
::: {.hero-banner}
::: {.content-block}
::: {.section}

{{< include partials/why_use.md >}}

::: {.citations-counter}
<span class="__dimensions_badge_embed__ badge-inline" data-doi=DATA_DOI data-legend="never" data-style="large_rectangle"></span>
<span type="button" class="badge-inline btn btn-sm journal-endorsement">Journals endorsing {{< meta acronym >}}</span>
<span class="journal-endorsement journal-endorsement-count">{{< meta journal-endorsement-count >}}</span>
<script async src="https://badge.dimensions.ai/badge.js" charset="utf-8"></script>
:::
:::{.text-small}
{{< meta acronym >}}: {{< meta full-title >}}

{{< meta translations >}}

Version: This is the latest version
:::
:::
:::
:::
"""

def create_web(guideline):
    return TEXT.replace('DATA_DOI', guideline.doi)
