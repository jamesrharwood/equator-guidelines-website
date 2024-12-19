from build.file import copy

def create_web(guideline):
    copy(guideline.repo_paths.item_order, guideline.destination_paths.item_order)
    return '{{< include partials/item_order.md >}}'