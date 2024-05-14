import pytest

from pages.calc_page import CalcPage

"""
Positive Tests:

Clear Entry (CE):

Input: 7 + 3 CE 5 =
Expected Output: 75 (Clear Entry should only remove the last entry)
All Clear (AC):

Input: 9 + 5 AC 3 =
Expected Output: 3 (All Clear should reset the calculator)

Negative Tests:

Division by Zero:

Input: 8 ÷ 0 =
Expected Output: Error message "Cannot divide by zero"
Invalid Expression:

Input: 9 + × =
Expected Output: Error message "Invalid expression"
Unfinished Expression:

Input: 6 × 7 ÷ =
Expected Output: Error message "Incomplete expression"
Overflow:

Input: 9999999999999999 + 1 =
Expected Output: Error message "Result too large"
Incorrect Decimal Input:

Input: 3. × 5 =
Expected Output: Error message "Invalid decimal input"
Unsupported Operation:

Input: 10 % 5 =
Expected Output: Error message "Operation not supported"
Incorrect Key Press:

Input: 8 ÷ 2 * 3 =
Expected Output: Error message "Invalid input sequence"
Combination of Operations with No Operand:

Input: + - =
Expected Output: Error message "Invalid expression"
"""

class TestCalc:
    @pytest.fixture(autouse=True)
    def open_calculator(self, page):
        page = CalcPage(page)
        page.open_calc()

    def test_add(self, page):
        page = CalcPage(page)
        page.press_button("5")
        page.press_button("+")
        page.press_button("3")
        page.press_button("=")
        assert page.read_answer() == "8"

    def test_subtraction(self, page):
        page = CalcPage(page)
        page.press_button("1")
        page.press_button("0")
        page.press_button("-")
        page.press_button("6")
        page.press_button("=")
        assert page.read_answer() == "4"

    def test_multiplication(self, page):
        page = CalcPage(page)
        page.press_button("4")
        page.press_button("*")
        page.press_button("5")
        page.press_button("=")
        assert page.read_answer() == "20"

    def test_division(self, page):
        page = CalcPage(page)
        page.press_button("1")
        page.press_button("2")
        page.press_button("/")
        page.press_button("4")
        page.press_button("=")
        assert page.read_answer() == "3"

    def test_decimal_calculation(self, page):
        page = CalcPage(page)
        page.press_button("0")
        page.press_button(".")
        page.press_button("5")
        page.press_button("+")
        page.press_button("1")
        page.press_button(".")
        page.press_button("2")
        page.press_button("5")
        page.press_button("=")
        assert page.read_answer() == "1.75"

    def test_multiple_operations(self, page):
        page = CalcPage(page)
        page.press_button("6")
        page.press_button("+")
        page.press_button("3")
        page.press_button("*")
        page.press_button("2")
        page.press_button("=")
        assert page.read_answer() == "12"
