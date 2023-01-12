from unittest import TestCase

from build.guideline.item.sections import Section, text_to_texts, text_to_section, HEADING_REGEX

class TestSection(TestCase):
    def test_section(self):
        section = Section(
            heading='Heading',
            index = 1,
            body = 'Paragraph.\n\nAnother paragraph.',
            item_index=9,
        )
        id = "#sec-9-1"
        self.assertEqual(section.id, id)
        self.assertEqual(section.toc_md, f"[Heading]({id})")
        self.assertEqual(section.body_heading, "## Heading{{"+id+"}}")
        self.assertEqual(
            section.md,
            (
                "## Heading{{"+id+"}}\n\n"
                "Paragraph.\n\nAnother paragraph."
            )
        )

    def test_text_to_texts(self):
        text = "1\n\n2\n\n3\n\n #Heading\n\n1\n2\n3\n##Heading 2   \n1\n\n2 \n\n3  \n\n\n "
        texts = list(text_to_texts(text))
        self.assertEqual(
            texts,
            [
                "1\n\n2\n\n3",
                "#Heading\n\n1\n\n2\n\n3",
                "##Heading 2\n\n1\n\n2\n\n3",
            ]
        )
    
    def test_text_to_headed_section(self):
        text = "#### Heading\n\nParagraph1\nParagraph2\n\nParagraph3"
        section = text_to_section(text, index=1, item_index=9)
        self.assertEqual(section.index, 1)
        self.assertEqual(section.item_index, 9)
        self.assertEqual(section.heading, 'Heading')
        self.assertEqual(section.body, "Paragraph1\nParagraph2\n\nParagraph3")

    def test_heading_regex(self):
        for text in ["## Heading", "###Heading   ", "# Heading", "  #   Heading"]:
            match = HEADING_REGEX.search(text)
            self.assertTrue(match)
            matched_text = match.groupdict()['heading'] #type: ignore
            self.assertEqual(matched_text.strip(), "Heading")
    
    def test_heading_regex_not_match(self):
        for text in ["", "Heading", "1. #  Heading"]:
            match = HEADING_REGEX.search(text)
            self.assertFalse(match)



