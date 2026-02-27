from build.file import copy, load_string

TRAINING_PARTIAL = 'training_partial'
DEFAULT_TRAINING_PARTIAL = 'default.md'

def create_web(guideline):
    for item in guideline.items:
        copy(item.source_path, item.web_path)
    return ''

class Item:
    def __init__(self, item):
        self.item = item
    
    def create_web(self, _):
        text = self.make_text()
        return text

    def make_text(self):
        text = load_string(self.item.source_path)
        text = self.prepend_search(text)
        text = self.append_training(text)
        if self.item.guideline.has_data_repo:
            text = self.append_discussion(text)
        return text

    def prepend_search(self, text):
        assert text[:3]=='---'
        text = '---\nsearch: false' + text[3:]
        return text

    def append_training(self, text):
        if not self.needs_training():
            return text
        lines = [
            text,
            '## Training',
            self.get_training_include(),
        ]
        return '\n\n'.join(lines)

    def needs_training(self):
        return bool(self.item.meta.get(TRAINING_PARTIAL, True))
    
    def get_training_include(self):
        partial = self.item.meta.get(TRAINING_PARTIAL, DEFAULT_TRAINING_PARTIAL)
        if not partial.endswith('.md'):
            partial += '.md'
        fp = '../../../build/resources/partials/training/'+partial
        include = '{{< include ' + fp + ' >}}'
        return include

    def append_discussion(self, text):
        text += f"""\n\n## Discuss this item\n\nVisit this items' [discussion page]({self.item.giscus_rel_path}) to ask questions and give feedback."""
        return text
