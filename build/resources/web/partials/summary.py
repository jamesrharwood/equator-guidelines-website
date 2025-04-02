from py_markdown_table.markdown_table import markdown_table # type: ignore

from build.guideline.glossary import add_glossary_to_string_using_spans
from build.resources.checklist.table import ChecklistTable

TEXT = '## Summary of guidance {#summary}\n\n'
TEXT += (
    'Although you should describe all items below, you can decide how to [order]'
    '(faqs.qmd#item-order) and [prioritize items](faqs.qmd#concise-writing) most '
    'relevant to your study, findings, context, and readership whilst '
    '[keeping your writing concise](faqs.qmd#concise-writing). You can read how '
    '{{< meta acronym >}} was developed in the [FAQs](faqs.qmd#development).\n\n'
)

TITLE = 'Item name'
DESC = 'What to write'
TABLE_PARAMS = dict(
    padding_weight='right',
    row_sep='always',
    quote=False,
    multiline_strategy='rows_and_header',
    multiline_delimiter=' ',
    multiline={TITLE: 250, DESC: 750}
)

def create_web(guideline):
    table = table_markdown(guideline)
    return TEXT + '\n\n' + table

def table_markdown(guideline):
    table = SummaryTable(guideline)
    return table.get_markdown()

class SummaryTable(ChecklistTable):
    resource_id = 'web'
    TABLE_PARAMS = TABLE_PARAMS
        
    def make_section_title_row(self, key, decorator):
        return {TITLE: f'\ {decorator}<!-- -->{key}{decorator}', DESC: ''}
    
    def yield_from_filename(self, filename, level):
        item = self.guideline.get_item_from_filename(filename)
        text = item.summary_text()
        text = add_glossary_to_string_using_spans(text, self.guideline.glossary_dict)
        title = f'[{item.summary_title()}](items/{item.destination_filename})'
        yield {
            TITLE: title,
            DESC: text,
        }

    def set_params(self, table):
        table.set_params(**self.TABLE_PARAMS)
        return table

# def create_web(guideline):
#     text += '|\n'
#     text += '----|------------\n'
#     for dict_ in guideline.resource_definitions['web']:
#         text += ''.join(list(yield_rows(guideline, dict_)))
#     text += '\n: {tbl-colwidths="[25,75]"}'
# #     return text

# def yield_rows(guideline, dict_, level=1):
#     for key, value in dict_.items():
#         decor = "**" if level==1 else ''
#         yield f'{decor}{key}{decor}|\n'
#         if type(value) is dict:
#             yield from yield_rows(guideline, value, level+1)
#         elif type(value) is list:
#             for element in value:
#                 if type(element) is dict:
#                     yield from yield_rows(guideline, element, level+1)
#                 else:
#                     item = guideline.get_item_from_filename(element)
#                     checklist_text = item.summary_text()
#                     checklist_text = add_glossary_to_string_using_spans(checklist_text, guideline.glossary_dict)
#                     text = f'[{item.summary_title()}](items/{item.destination_filename})|{checklist_text}\n'
#                     yield text