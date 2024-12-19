from .partials import create_pages
from .sidebar import Sidebar

def create(guideline):
    pages = create_pages(guideline)
    for page in pages:
        page.create_web()
    sidebar = Sidebar(guideline)
    sidebar.save()