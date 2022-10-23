class Cat:
    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age

    def __call__(self):
        return f'name: {self.name}, \nsex: {self.sex}, \nage: {self.age}'
