from build.guideline.glossary import add_glossary_to_string_using_spans

def create_web(guideline):
    text = '## Summary of guidance {#summary}\n\n'
    text += (
        'Although you should describe all items below, you can decide how to [order]'
        '(faqs.qmd#item-order) and [prioritize items](faqs.qmd#concise-writing) most '
        'relevant to your study, findings, context, and readership whilst '
        '[keeping your writing concise](faqs.qmd#concise-writing). You can read how '
        '{{< meta acronym >}} was developed in the [FAQs](faqs.qmd#development).\n\n'
    )
    text += '|\n'
    text += '----|------------\n'
    for dict_ in guideline.resource_definitions['web']:
        for key, filenames in dict_.items():
            text += f'**{key}**|\n'
            for filename in filenames:
                item = next(item for item in guideline.items if item.filename == filename)
                checklist_text = item.checklist_text()
                checklist_text = add_glossary_to_string_using_spans(checklist_text, guideline.glossary_dict)
                text += f'[{item.number("web")}. {item.title}](items/{item.destination_filename})|{checklist_text}\n'
    text += '\n: {tbl-colwidths="[25,75]"}'
    return text