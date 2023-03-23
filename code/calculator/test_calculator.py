from calculator import Calculator

def test_calculator():
    calc = Calculator()

    # Test addition
    assert calc.add(2, 3) == 5, "Test case 1 failed"
    assert calc.add(-2, 3) == 1, "Test case 2 failed"

    # Test subtraction
    assert calc.subtract(5, 3) == 2, "Test case 3 failed"
    assert calc.subtract(0, -5) == 5, "Test case 4 failed"

    # Test multiplication
    assert calc.multiply(3, 4) == 12, "Test case 5 failed"
    assert calc.multiply(-2, 5) == -10, "Test case 6 failed"

    # Test division
    assert calc.divide(10, 2) == 5, "Test case 7 failed"
    assert calc.divide(-10, 5) == -2, "Test case 8 failed"

    # Test division by zero
    try:
        calc.divide(10, 0)
    except ValueError as e:
        assert str(e) == "Cannot divide by zero", "Test case 9 failed"

    print("All test cases passed")

if __name__ == "__main__":
    test_calculator()
