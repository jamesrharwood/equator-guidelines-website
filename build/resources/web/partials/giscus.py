import os

from build import file
from build.resources.web.partials.guidance.item import Item

def create_web(guideline):
    print('creating giscus files')
    create_html(guideline.items)
    return ''

def create_html(items):
    for idx, item in enumerate(items):
        print('creating giscus for item ', item.giscus_path)
        web_item = Item(item, idx, item.guideline)
        qmd = _make_html(item, web_item)
        file.save_string(qmd, item.giscus_path)

def _make_html(item, web_item):
    return f"""\
---
title: "Discussion for {item.guideline.config['title-prefix']} item: [{item.title}](..)"
---
{web_item.md}

<script src="https://giscus.app/client.js"
data-repo="{item.guideline.data_repo}"
data-repo-id="R_kgDOIaTtVw"
data-category-id="DIC_kwDOIaTtV84CSe8U"
data-mapping="specific"
data-term="{item.title}"
data-strict="0"
data-reactions-enabled="1"
data-emit-metadata="0"
data-input-position="bottom"
data-theme="light"
data-lang="en"
crossorigin="anonymous"
async>
</script>
"""
