from wagtail.core import blocks

class TitleAndTextBlock(blocks.StructBlock):

    title = blocks.CharBlock(required=True, help_text='Add Title')
    text = blocks.TextBlock(required=True, help_text='Add new Text')

    class Meta: #noqa
        template = "streams/title_and_text_block.html"
        icon = "edit"
        label = "Title and Text"