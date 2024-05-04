import unittest

def divide(x, y):
    """Divides two numbers and handles any exceptions"""
    try:
        result = x / y
    except ZeroDivisionError as e:
        raise DivideByZeroError("Division by zero is not allowed.") from e
    except Exception as e:
        raise TypeError(f"Unsupported operand type(s) for /: {type(x)} and {type(y)}") from e
    else:
        return result

class DivideByZeroError(Exception):
    """Custom exception for division by zero"""
    pass

class TestDivide(unittest.TestCase):
    """Test case class for the divide function"""
    def test_divide(self):
        """Test the divide function with some inputs"""
        self.assertEqual(divide(10, 2), 5)
        
        with self.assertRaisesRegex(DivideByZeroError, "Division by zero is not allowed. Mang eak") as context:
            divide(10, 0)
        print("\n" + str(context.exception) + "\n")
        
        with self.assertRaisesRegex(TypeError, "Unsupported operand type\(s\) for /: <class 'str'> and <class 'int'>") as context:
            divide("10", 2)

        print("\n" + str(context.exception) + "\n")

if __name__ == '__main__':
    unittest.main()