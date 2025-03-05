from build.guideline.guideline import Guideline as Base

# from .item import Item

TEMPLATE = """

## [Item number {number}]()
Here is a longish sentence that will introduce the topic a little bit. And here are some bullet points. 

* Bullet one tells you to do something
* Bullet two says if you did X, you should write Y
* Bullet 3 says if you did not or could not do something, explain why, and then discuss how this may have affected your results in the discussion section (or explain why you feel like it won't have affected your results).  

"""

class Guideline(Base):
    # item_class = Item

    def create_writing_guide(self):
        text = ""
        for i in range(20):
            text += TEMPLATE.format(number=str(i))
        return text


    
   