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
        text += ''.join(list(yield_rows(guideline, dict_)))
    # for dict_ in guideline.resource_definitions['web']:
    #     for key, filenames in dict_.items():
    #         text += f'**{key}**|\n'
    #         for filename in filenames:
    #             try:
    #                 item = next(item for item in guideline.items if item.filename == filename)
    #             except StopIteration:
    #                 continue
    #             checklist_text = item.checklist_text()
    #             checklist_text = add_glossary_to_string_using_spans(checklist_text, guideline.glossary_dict)
    #             text += f'[{item.title}](items/{item.destination_filename})|{checklist_text}\n'
    text += '\n: {tbl-colwidths="[25,75]"}'
    return text

def yield_rows(guideline, dict_, level=1):
    for key, value in dict_.items():
        decor = "**" if level==1 else ''
        yield f'{decor}{key}{decor}|\n'
        if type(value) is dict:
            yield from yield_rows(guideline, value, level+1)
        elif type(value) is list:
            for element in value:
                if type(element) is dict:
                    yield from yield_rows(guideline, element, level+1)
                else:
                    item = next(item for item in guideline.items if item.filename == element)
                    checklist_text = item.checklist_text()
                    checklist_text = add_glossary_to_string_using_spans(checklist_text, guideline.glossary_dict)
                    text = f'[{item.title}](items/{item.destination_filename})|{checklist_text}\n'
                    yield text