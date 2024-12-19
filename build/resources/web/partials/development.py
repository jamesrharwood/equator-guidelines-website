DEFAULT = """
## How {{< meta acronym >}} was made

{{< meta acronym >}} was made through a rigorous, evidence based process and originally published as an [academic article]({{< meta articles.development >}}). The UK EQUATOR Centre then worked with SRQR's developers to make it easier to use by clarifying language, adding definitions, examples, extra information and resources. Although worded differently, the guidance on this website is conceptually the same as the original publication and can be used interchangeably. Read more about [SRQR's development](./faq#development) in the FAQ.
"""

def create_web(guidelines):
    return DEFAULT