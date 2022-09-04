from .prompts import *

inquirers = {
    "string": String,
    "password": Password,
    "number": Number,
    "confirm": Confirm,
    "radio": Radio,
    "checkbox": Checkbox
}


def prompt(questions, answers=None):
    answers = answers or {}

    for question in questions:
        if 'type' not in question:
            raise Exception("缺少 `type` 属性")
        if 'name' not in question:
            raise Exception("缺少 `name` 属性置")
        if 'title' not in question:
            raise Exception("缺少 `title` 属性")
        try:

            _kwargs = {}
            _kwargs.update(question)
            name = _kwargs.pop('name')
            _type = _kwargs.pop('type')
            title = _kwargs.pop('title')

            if _type not in inquirers:
                raise Exception(f"问答器 `{_type}` 不存在")

            application = inquirers[_type](title, **_kwargs)

            answer = application.get()

            answers[name] = answer
        except AttributeError as e:
            print(e)
            raise ValueError('No question type \'%s\'' % type)
        except KeyboardInterrupt:
            print('')
            print("用户取消")
            print('')
            return {}
    return answers
