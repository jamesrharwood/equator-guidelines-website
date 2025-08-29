---
title: The {{< meta acronym >}} reporting checklist
subtitle: 'For checking that {{< meta for-writing >}} can be understood and used by everyone'
bibliography: bibliographies/self.bib
csl: ../../vancouver.csl
execute:
    enabled: true
    freeze: false
    echo: false
format:
    docx:
        appendix-cite-as: display
        reference-doc: ../../custom-reference.docx
number-sections: true
crossref:
    sec-prefix: Note
search: false
---

::: {.callout-note}

If you have not used a reporting guideline before, read about [how and why to use them]({{< meta paths.html.about_reporting_guidelines >}}) and check whether {{< meta acronym >}} is the [most applicable reporting guideline]({{< meta paths.html.applicability >}}) for your work.

Reporting guidelines are most useful when used early in research. When writing a manuscript or application, consider using the [Full Guidance]({{< meta paths.html.full_guideline >}}) where you'll see explanations and examples for each item.

After writing, demonstrate adherence by completing this checklist:

1. Specify where each item is described (see @sec-specify).
2. Cite this checklist (See @sec-cite).
3. Include your completed checklist as a supplement when submitting to a journal so that future readers can use it to find information.

:::

<br>

```{python}
from IPython.display import Markdown

import yaml

with open('_metadata.yml', 'r') as file_:
    meta = yaml.safe_load(file_)

import os
path = os.getcwd()
path = path.split('/reporting-guidelines')[0]
os.chdir(path)
from build.resources.checklist.guideline import Guideline

id_ = meta['id']
gl = Guideline.create(id_)

Markdown(gl.get_table_markdown())
```

{{< pagebreak >}}

## How to specify where content is {#sec-specify .appendix}

Tell the reader where they can find information. E.g.,

* Results; paragraph 2
* Methods, Participants; paragraphs 1 & 2.
* Table 3
* Supplement B, para. 4

If you have chosen not to describe an item, explain why. You can do this in the checklist, or as a note below it.

You can describe items in the article body, or in tables, figures, or supplementary materials, and should prioritize items you feel are most important to your intended audience. The order of items in your manuscript does not need to match the order of items in this checklist. You can decide how best to structure your work.

{{< include ../../build/resources/partials/how_to_cite.md >}}
