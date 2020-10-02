"""Simple calculator."""


class Calculation:
    """Perform basic mathematical operations based on user input."""

    def __init__(self, num_1, num_2):
        """Initialize."""
        self.num_1 = num_1
        self.num_2 = num_2

    def add_numbers(self):
        """Add numbers."""
        return self.num_1 + self.num_2

    def subtract_numbers(self):
        """Subtract numbers."""
        return self.num_1 - self.num_2

    def multiply_numbers(self):
        """Multiply numbers."""
        return self.num_1 * self.num_2

    def divide_numbers(self):
        """
        Prior to performing the division operation check
        whether the second input is 0 (zero) or not.
        Return an error in case it is.
        """
        try:
            return round((self.num_1 / self.num_2), 2)
        except ZeroDivisionError as err:
            return f"Cannot perform this operation -> {err}"

    def calculate(self, operation):
        """
        Instead of if-elif statements I am using
        dictionary dispatch here.
        Found it on O'Reilly:
        https://www.oreilly.com/library/view/python-cookbook/0596001673/ch01s07.html
        """
        menu = {
            'a': self.add_numbers,
            's': self.subtract_numbers,
            'm': self.multiply_numbers,
            'd': self.divide_numbers,
        }

        return menu[operation]()


def main():
    try:
        num_1 = int(input("Please type a number: "))
        num_2 = int(input("Please type another number: "))
    except ValueError:
        print("Please provide a number.")
        return  # replaced 'else:' with 'return'

    operation = input("What kind of mathematical operation would you "
                      "like to perform on these numbers?\n"
                      "[A]dd, [S]ubtract, [M]ultiply, [D]ivide: ").lower()

    inst = Calculation(num_1, num_2)

    try:
        result = inst.calculate(operation)
    except KeyError:
        print("Please provide a correct letter -> (A, S, M, D).")
        return  # replaced 'else:' with 'return'

    signs = {
        'a': '+',
        's': '-',
        'm': '*',
        'd': '/',
    }

    print(f"Your operation: {num_1} {signs[operation]} {num_2} = {result}")


if __name__ == '__main__':
    main()
