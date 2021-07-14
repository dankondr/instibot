from aiogram.types import InlineKeyboardMarkup


class BotResponse:
    def __init__(
        self,
        text: str = None,
        markup: InlineKeyboardMarkup = None,
        edit_text: str = None,
        edit_markup: InlineKeyboardMarkup = None
    ):
        self.text = text
        self.markup = markup
        self.edit_text = edit_text
        self.edit_markup = edit_markup


class BotResponseNotAllowed(BotResponse):
    def __init__(self, allowed_methods: list[str], *args, **kwargs):
        if 'message' in allowed_methods:
            text = 'Сначала отправьте сообщение!'
        else:
            text = 'Сначала выберите действие!'
        kwargs.update(text=text)
        super().__init__(*args, **kwargs)
