import logging

from peewee import Model

from instibot.tg.request import BotRequest
from instibot.tg.response import BotResponseNotAllowed

logger = logging.getLogger('botframework.request')


class View:
    request: BotRequest
    args: tuple
    kwargs: dict

    method_names = ['message', 'query']

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def render(self):
        pass

    def setup(self, request, *args, **kwargs):
        self.request = request
        self.args = args
        self.kwargs = kwargs

    def dispatch(self, request, *args, **kwargs):
        if request.method.lower() in self.method_names:
            handler = getattr(self, request.method.lower(),
                              self.method_not_allowed)
        else:
            handler = self.method_not_allowed
        return handler(request, *args, **kwargs)

    def method_not_allowed(self, request, *args, **kwargs):
        logger.warning('Запрещённое действие (%s): %s', request.method.upper(), repr(request))
        return BotResponseNotAllowed(self._allowed_methods())

    def _allowed_methods(self):
        return [method for method in self.method_names if hasattr(self, method)]
