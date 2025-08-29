---
title: The {{< meta acronym >}} reporting guideline writing guide
subtitle: 'For writing impactful {{< meta for-writing >}} that can be understood and used by a wide audience.'
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
    html:
        theme: cosmo
number-sections: false
crossref:
    sec-prefix: Note
search: false
---

::: {.callout-note}

If you have not used a writing guide before, read about our suggested [writing process]({{< meta paths.html.about_writing_guides >}}).

This guide is not a template. Don't expect to fill it in and end up with a finished article. Instead, think of it as an exercise book.

1. Collate information and make notes in this guide;
2. Delete the prompts and headings, reorganise your notes into a narrative structure, moving content to tables, figures, or appendices when appropriate, thereby creating a writing outline.
3. Draft, revise, and edit your text in a separate file, referring to your outline throughout.

Before you begin, double check that {{< meta acronym >}} is the [most applicable reporting guideline]({{< meta paths.html.applicability >}}) for your work. Other reporting guidelines have their own writing guide.

The [UK EQUATOR Centre training]({{< meta paths.html.training >}}) helps researchers develop writing skills and to use reporting guidelines (like this one) to write research articles and applications that are complete, concise, and compelling. It covers many of the items of the {{< meta acronym >}} reporting guideline, including how to prepare effective abstracts, titles, introduction and discussion sections, as well as how to use writing guides to create writing outlines, how to turn outlines into drafts, and drafts into polished text.

{{< pagebreak >}}

:::

```{python}
from IPython.display import Markdown

import yaml

with open('_metadata.yml', 'r') as file_:
    meta = yaml.safe_load(file_)

import os
path = os.getcwd()
path = path.split('/reporting-guidelines')[0]
os.chdir(path)
from build.resources.writing_guide.guideline import Guideline

id_ = meta['id']
gl = Guideline.create(id_)

Markdown(gl.create_writing_guide())

```

{{< include ../../build/resources/partials/how_to_cite.md >}}
