import pytest

from pages.calc_page import CalcPage


class TestCalc:
    """Suite with the functionality of the calculator component on Google tests"""
    @pytest.fixture(autouse=True)
    def open_calculator(self, page):
        """Fixture rto open Calculator before each test"""
        page = CalcPage(page)
        page.open_calc()

    def test_add(self, page):
        """Test adding functionality"""
        page = CalcPage(page)
        page.press_button("5")
        page.press_button("+")
        page.press_button("3")
        page.press_button("=")
        output = page.read_answer()
        assert output == "8", f"expected - '8', got - '{output}'"

    def test_subtraction(self, page):
        """Test subtraction functionality"""
        page = CalcPage(page)
        page.press_button("1")
        page.press_button("0")
        page.press_button("-")
        page.press_button("6")
        page.press_button("=")
        output = page.read_answer()
        assert output == "4", f"expected - '4', got - '{output}'"

    def test_multiplication(self, page):
        """Test multiplication functionality"""
        page = CalcPage(page)
        page.press_button("4")
        page.press_button("*")
        page.press_button("5")
        page.press_button("=")
        output = page.read_answer()
        assert output == "20", f"expected - '20', got - '{output}'"

    def test_division(self, page):
        """Test division functionality"""
        page = CalcPage(page)
        page.press_button("1")
        page.press_button("2")
        page.press_button("/")
        page.press_button("4")
        page.press_button("=")
        output = page.read_answer()
        assert output == "3", f"expected - '3', got - '{output}'"

    def test_decimal_calculation(self, page):
        """Test decimal calculation functionality"""
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
        output = page.read_answer()
        assert output == "1.75", f"expected - '1.75', got - '{output}'"

    def test_multiple_operations(self, page):
        """Test multiple operations functionality"""
        page = CalcPage(page)
        page.press_button("6")
        page.press_button("+")
        page.press_button("3")
        page.press_button("*")
        page.press_button("2")
        page.press_button("=")
        output = page.read_answer()
        assert output == "12", f"expected - '12', got - '{output}'"

    def test_clear_entry(self, page):
        """Test Clear Entry (CE) functionality"""
        page = CalcPage(page)
        page.press_button("7")
        page.press_button("+")
        page.press_button("3")
        page.press_button("CE")
        page.press_button("5")
        page.press_button("=")
        output = page.read_answer()
        assert output == "12", f"expected - '12', got - '{output}', Clear Entry should only remove the last entry"

    def test_all_clear(self, page):
        """Test All Clear (AC) functionality"""
        page = CalcPage(page)
        page.press_button("9")
        page.press_button("+")
        page.press_button("5")
        page.press_button("AC", delay=1000)
        page.press_button("3")
        page.press_button("=")
        output = page.read_answer()
        assert output == "3", f"expected - '3', got - '{output}', All Clear (AC) should remove all entries"

    def test_zero_division(self, page):
        """Test Division by Zero functionality"""
        page = CalcPage(page)
        page.press_button("8")
        page.press_button("/")
        page.press_button("0")
        page.press_button("=")
        output = page.read_answer()
        assert output == "Infinity", f"expected - 'Infinity', got - '{output}', Cannot divide by zero"
