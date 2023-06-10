"display approximated reading time"

from .guidance.guidance import Guidance

def create_web(guideline: str) -> str:
    "display approximated reading time"
    guidance = Guidance(guideline)
    reading_time = guidance.get_reading_time('web')
    return TEMPLATE.format(reading_time=reading_time)

TEMPLATE = \
"""## Guidance

<small>Approx. {reading_time} min read</small>"""
