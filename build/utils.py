from dataclasses import dataclass

@dataclass
class CompositionBase():
    def __init__(self, composite):
        self._composite = composite
    
    def __getattr__(self, attr):
        return getattr(self._composite, attr)
