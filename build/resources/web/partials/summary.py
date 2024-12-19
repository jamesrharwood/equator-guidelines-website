def create_web(guideline):
    text = '## Summary of guidance {#summary}\n\n'
    text += '|\n'
    text += '----|------------\n'
    for dict_ in guideline.resource_definitions['web']:
        for key, filenames in dict_.items():
            text += f'**{key}**|\n'
            for filename in filenames:
                item = next(item for item in guideline.items if item.filename == filename)
                text += f'[{item.title}]({item.destination_filename})|{item.checklist_text()}\n'
    text += '\n: {tbl-colwidths="[25,75]"}'
    return text