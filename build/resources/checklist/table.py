from py_markdown_table.markdown_table import markdown_table # type: ignore

TITLE = ''
TEXT = 'Item Description'
LOCATION = 'Location\n(or reason for not reporting)'

class ChecklistTable:
    resource_id = 'checklist'
    TABLE_PARAMS = dict(
        padding_weight='right',
        row_sep='always',
        quote=False,
        multiline_strategy='rows_and_header',
        multiline_delimiter=' ',
        multiline={TITLE: 200, TEXT: 500, LOCATION: 300}
    )
    def __init__(self, guideline):
        self.guideline = guideline
    
    def get_markdown(self):
        data = self.yield_data()
        table = markdown_table(list(data))
        table = self.set_params(table)
        return table.get_markdown()
    
    def set_params(self, table):
        table.set_params(**self.TABLE_PARAMS)
        return table
    
    def yield_data(self):
        for element in self.guideline.resource_definitions[self.resource_id]:
            yield from self.yield_resource_element(element, level=1)

    def yield_resource_element(self, element, level):
        # will choose the yield strategy depending on string or list 
        if type(element) is dict:
            yield from self.yield_from_dict(element, level)
        if type(element) is str:
            yield from self.yield_from_filename(element, level)
    
    def yield_from_dict(self, dict, level):
        for key in dict.keys():
            decorator = '**' if level==1 else ''
            yield self.make_section_title_row(key, decorator)
            for value in dict[key]:
                yield from self.yield_resource_element(value, level+1)
    
    def make_section_title_row(self, key, decorator):
        return {TITLE: f'\ {decorator}<!-- -->{key}{decorator}', TEXT: '', LOCATION: ''}
    
    def yield_from_filename(self, filename, level):
        item = self.guideline.get_item_from_filename(filename)
        yield {
            TITLE: item.title_hyperlinked,
            TEXT: item.text,
            LOCATION: '',
        }

