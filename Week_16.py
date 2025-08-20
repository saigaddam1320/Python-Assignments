
class NegativeAgeError(Exception):
    """Raised when the input age is negative"""

    def __init__(self, age):
        self.age = age
        super().__init__(f"Invalid age: {age}. Age cannot be negative.")


def check_age(age):
    if age < 0:
        raise NegativeAgeError(age)  # raise custom exception
    else:
        print(f"Age entered: {age}")


try:
    age_input = int(input("Enter your age: "))
    check_age(age_input)
except NegativeAgeError as e:
    print("Error:", e)
