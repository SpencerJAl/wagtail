from wagtail.core import blocks

class TitleAndTextBlock(blocks.StructBlock):

    title = blocks.CharBlock(required=True, help_text='Add Title')
    text = blocks.TextBlock(required=True, help_text='Add new Text')

    class Meta: #noqa
        template = "streams/title_and_text_block.html"
        icon = "edit"
        label = "Title and Text"


class RichTextBlock(blocks.RichTextBlock):
     
     class meta: #noqa
         template = "streams/richtext_block.html"
         icon = "doc-full"
         label = "Full Rich Text"

class SimpleRichTextBlock(blocks.RichTextBlock):
    
    def __init__(self, required=True, help_text=None, editor='default', features=None, validators=(), **kwargs):
     super().__init__(**kwargs)
     self.features = [
        "bold",
        "italic",
        "link",
      ]

    class meta: #noqa
            template = "streams/richtext_block.html"
            icon = "edit"
            label = "Simple Rich Text"