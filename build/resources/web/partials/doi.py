TEXT = """\
::: {.hero-banner}
::: {.content-block}
::: {.section}

{{< include partials/why_use.md >}}

::: {.citations-counter}
<span class="__dimensions_badge_embed__ badge-inline" data-doi=DATA_DOI data-legend="never" data-style="large_rectangle"></span>
<a type="button" class="badge-inline btn btn-sm btn-outline-secondary journal-endorsement black-font" href="HREF">Journals endorsing {{< meta acronym >}}</a>
<span class="journal-endorsement journal-endorsement-count">{{< meta journal-endorsement-count >}}</span>
<script async src="https://badge.dimensions.ai/badge.js" charset="utf-8"></script>
:::
:::{.text-small}
{{< meta acronym >}}: {{< meta acronym-definition >}}

::: {.content-hidden unless-meta="translations"}
Translations: {{< meta translations >}}
:::

Version: {{< meta version >}}. This is the latest version ✅
:::
:::
:::
:::
"""

def create_web(guideline):
    text = TEXT.replace('DATA_DOI', guideline.config['doi-for-citation-count'])
    text = text.replace('HREF', 'https://lookerstudio.google.com/s/tgpggDGiRDQ')
    return text
