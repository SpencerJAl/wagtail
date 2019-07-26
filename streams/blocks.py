from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
class TitleAndTextBlock(blocks.StructBlock):

    title = blocks.CharBlock(required=True, help_text='Add Title')
    text = blocks.TextBlock(required=True, help_text='Add new Text')

    class Meta: #noqa
        template = "streams/title_and_text_block.html"
        icon = "edit"
        label = "Title and Text"

class CardBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True, help_text="Add you title")

    cards = blocks.ListBlock(
        blocks.StructBlock(
        [
            ("image", ImageChooserBlock(required=True)),
            ("title", blocks.CharBlock(required=True, max_length=40)),
            ("text", blocks.TextBlock(required=True, max_length=200)),
            ("button_page", blocks.PageChooserBlock(required=False)),
            ("button_url", blocks.URLBlock(required=False, help_text="If the button page is selected, it will be selected first"))
        ]
      )
    )
    class meta: #noqa
        template = "streams/card_block.html"
        icon = "placeholder"
        label = "Staff Cards"

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