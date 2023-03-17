import os

from build import file
from build.resources.web.partials.guidance.item import Item


def create_web(guideline):
    create_html(guideline.items)
    return ''

def create_html(items):  
    skipped = 0      
    for idx, item in enumerate(items):
        if not os.path.exists(item.giscus_path):
            print('Creating giscus HTML for item ', item.giscus_path)
            web_item = Item(item, idx, item.guideline)
            qmd = _make_html(item, web_item)
            file.save_string(qmd, item.giscus_path)
        else:
            skipped += 1
    if skipped:
        print(f'Giscus HTML files already exist for {skipped} items')

def _make_html(item, web_item):
    return f"""\
---
title: "Discussion for {item.guideline.config['title-prefix']} item: [{item.title}](..)"
citation: false
---
{TEMPLATE.format(item=web_item).strip()}

<script src="https://giscus.app/client.js"
data-repo="{item.guideline.data_repo}"
data-repo-id="R_kgDOIaTtVw"
data-category="Announcements"
data-category-id="DIC_kwDOIaTtV84CSe8S"
data-mapping="specific"
data-term="{item.title}"
data-strict="0"
data-reactions-enabled="1"
data-emit-metadata="0"
data-theme="preferred_color_scheme"
data-theme="light"
data-lang="en"
crossorigin="anonymous"
async>
</script>
"""

TEMPLATE = \
"""::: {{.grid id="{item.id}"}}
::: {{.g-col-9}}
#### {item.title}
:::
::: {{.g-col-3}}
:::
:::

{item.body}

{item.readmore}"""
