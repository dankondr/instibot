from instibot.views.base import View


class FormMetaclass(type):
    pass  # TODO


class ModelFormMetaclass(FormMetaclass):
    pass  # TODO


class FormView(View, metaclass=FormMetaclass):
    pass  # TODO
    # class Meta:
    #     name: str = None
    #     display_name: str = None


class ModelForm(FormView, metaclass=ModelFormMetaclass):
    pass  # TODO
    # class Meta:
    #     name: str = None
    #     display_name: str = None
    #     model: Model = None
