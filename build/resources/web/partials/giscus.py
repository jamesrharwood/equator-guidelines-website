import os

from build import file
from build.resources.web.partials.guidance.item import Item

class Giscus:
    def __init__(self, item):
        self.item = item
    
    def create_web(self, _):
        return make_html(self.item)






# def create_web(guideline):
#     create_html(guideline.items)
#     return ''

# def create_html(items):
#     print('creating html for giscus') 
#     skipped = 0      
#     for idx, item in enumerate(items):
#         if not os.path.exists(item.giscus_path):
#             print('Creating giscus HTML for item ', item.giscus_path)
#             web_item = Item(item, idx, item.guideline)
#             qmd = _make_html(item, web_item)
#             file.save_string(qmd, item.giscus_path)
#         else:
#             skipped += 1
#     if skipped:
#         print(f'Giscus HTML files already exist for {skipped} items')

# def _make_html(item, web_item):
#     return f"""\

def make_html(item):
    return TEMPLATE.format(item=item)

TEMPLATE = """
---
title: "Discussion for {item.guideline.short_name} item: [{item.title}](..)"
citation: false
---
## Discussion for {item.guideline.id} item: {item.title}

Do you have questions or feedback about this SRQR reporting guideline item? Do you want to ask other researchers for help? Or give feedback to the guideline developers? 

Leave a comment below! This website uses Giscus, an open source commenting system powered by [GitHub Discussions](https://docs.github.com/en/discussions). To use it, you will need an account with [GitHub](https://github.com/signup), the world leading repository platform used by academics globally.

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
