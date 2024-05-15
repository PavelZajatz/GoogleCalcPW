class CalcPage:
    """Class with methods for Google calculator interaction"""
    URL = "https://www.google.com/"
    CALC_NAME = "calculator"

    def __init__(self, page):
        self.page = page
        self.search_field = page.locator('[aria-label="Search"]')
        self.first_option = page.locator(f'[data-entityname="{self.CALC_NAME}"]')
        self.point_btn = page.locator('[aria-label="point"]')
        self.zero_btn = page.locator("//*[@role='button'][text()='0']")
        self.one_btn = page.locator("//*[@role='button'][text()='1']")
        self.two_btn = page.locator("//*[@role='button'][text()='2']")
        self.three_btn = page.locator("//*[@role='button'][text()='3']")
        self.four_btn = page.locator("//*[@role='button'][text()='4']")
        self.five_btn = page.locator("//*[@role='button'][text()='5']")
        self.six_btn = page.locator("//*[@role='button'][text()='6']")
        self.seven_btn = page.locator("//*[@role='button'][text()='7']")
        self.eight_btn = page.locator("//*[@role='button'][text()='8']")
        self.nine_btn = page.locator("//*[@role='button'][text()='9']")
        self.divide_btn = page.locator('[aria-label="divide"]')
        self.multiply_btn = page.locator('[aria-label="multiply"]')
        self.minus_btn = page.locator('[aria-label="minus"]')
        self.plus_btn = page.locator('[aria-label="plus"]')
        self.equals_btn = page.locator('[aria-label="equals"]')
        self.clear_entry_btn = page.locator('[aria-label="clear entry"]')
        self.answer = page.locator('//*[@role="presentation"][@tabindex="0"]//span')

    def open_calc(self):
        """Method to Open Calculator on Google page"""
        self.page.goto(self.URL)
        self.search_field.fill(self.CALC_NAME)
        self.first_option.click()

    def press_button(self, button, delay=0):
        """Method to press Calculator buttons
        :param button: One of the Calculator buttons - "0123456789.=+-×÷AC/CE"
        :param delay: Time to wait between `mousedown` and `mouseup` in milliseconds. Defaults to 0.
        """
        buttons = {
            ".": self.point_btn,
            "0": self.zero_btn,
            "1": self.one_btn,
            "2": self.two_btn,
            "3": self.three_btn,
            "4": self.four_btn,
            "5": self.five_btn,
            "6": self.six_btn,
            "7": self.seven_btn,
            "8": self.eight_btn,
            "9": self.nine_btn,
            "+": self.plus_btn,
            "-": self.minus_btn,
            "/": self.divide_btn,
            "*": self.multiply_btn,
            "=": self.equals_btn,
            "AC": self.clear_entry_btn,
            "CE": self.clear_entry_btn
        }
        buttons[str(button)].click(delay=delay)

    def read_answer(self):
        """Method to read calculated answer"""
        return self.answer.inner_text()
