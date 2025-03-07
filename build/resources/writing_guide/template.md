---
title: The {{< meta acronym >}} reporting guideline writing guide
subtitle: 'For writing impactful {{< meta for-writing >}} that can be understood and used by everyone.'
bibliography: bibliographies/self.bib
csl: ../../vancouver.csl
execute:
    enabled: true
    echo: false
    freeze: false
format:
    docx:
        appendix-cite-as: display
        reference-doc: ../../custom-reference.docx
number-sections: false
crossref:
    sec-prefix: Note
---

::: {.callout-note}

If you have not used a writing guide before, read about our suggested "[packing for a holiday]({{< meta paths.html.about_writing_guides >}})" writing process.

This guide is not a template. Don't expect to fill it in and end up with a finished article. Instead, think of it as an exercise book.

1. Collate information and make notes in this guide;
2. Delete the prompts and headings, reorganise your notes into a narrative structure, and decide which information to prioritize;
3. Draft, revise, and edit your text in a separate file.

Before you begin, double check that {{< meta acronym >}} is the [most applicable reporting guideline]({{< meta paths.html.applicability >}}) for your work. Other reporting guidelines have their own writing guide.

:::

```{python}
from IPython.display import Markdown

import yaml

with open('_metadata.yml', 'r') as file_:
    meta = yaml.safe_load(file_)

import os
path = os.getcwd()
path = path.split('/guidelines')[0]
os.chdir(path)
from build.resources.writing_guide.guideline import Guideline

id_ = meta['id']
gl = Guideline.create(id_)

Markdown(gl.create_writing_guide())

```

## How to cite {#sec-cite .appendix}

Describe how you used {{< meta acronym >}} at the end of your Methods section e.g., 

> 'We used the {{< meta acronym >}}[@WritingGuide] writing guide to draft this manucript, and the {{< meta acronym >}} reporting checklist[@Checklist] when writing this manuscript, included in supplement A'

Then reference the resources you used.