# Setters and Getters
class Person:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

        # By setting self.first_name , the set operation uses the setter method to set the
        # first_name attribute as opposed to bypassing it by accessing self._first_name

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('First Name must be String')
        if len(value) > 12:
            raise ValueError('First Name must be less than 13 characters')
        self._first_name = value

    # Deleter function (optional)
    @first_name.deleter
    def first_name(self):
        raise AttributeError("Can't delete attribute")


p1 = Person('Steve', 'Jobs', 30)


print(p1.first_name)

p1.first_name = 'Bill'

print(p1.first_name)

# del p1.first_name