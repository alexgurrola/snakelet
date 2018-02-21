from .document import Document


def foo(func):
    def inner(*args, **kwargs):
        return func(*args, **kwargs)

    return inner


class Cat(Document):
    def __init__(self, name: str, **kwargs):
        # Parental
        super().__init__(**kwargs)
        self.name = name

    @foo
    def meow(self):
        return self.name


litter = [
    Cat('kitty'),
    Cat('cutey')
]

print('meow:', [cat.meow() for cat in litter])
