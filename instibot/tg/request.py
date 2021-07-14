from typing import Union

from aiogram.types import InlineKeyboardMarkup, Message, CallbackQuery

RequestObject = Union[Message, CallbackQuery]


class BotRequest:
    def __init__(self, method: str, obj: RequestObject):
        self.method = method
        self.obj = obj

    def __repr__(self):
        return f'BotRequest <{self.method=}, {repr(self.obj)}>'


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
