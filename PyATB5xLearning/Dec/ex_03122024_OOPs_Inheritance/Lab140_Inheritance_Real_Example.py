class BaseTest:
    def open_browser(self):
        print("Starting the browser")

    def read_from_excel(self):
        print("Read from Excel")

    def close_browser(self):
        print("Closing the browser")

class TestCase1(BaseTest):

    def test_positive(self):
        self.open_browser()
        print("Test case P1 Executed!!")
        self.read_from_excel()
        self.close_browser()

    def test_negative(self):
        self.open_browser()
        print("Test case N1 Executed!!")
        self.close_browser()

class TestCase2(BaseTest):

    def test_positive(self):
        self.open_browser()
        print("Test case P2 Executed!!")
        self.close_browser()

    def test_negative(self):
        self.open_browser()
        print("Test case N2 Executed!!")
        self.close_browser()


obj_ref = BaseTest()
obj_ref1 = TestCase1()
obj_ref2 = TestCase2()

obj_ref1.test_positive()
obj_ref1.test_negative()
obj_ref2.test_positive()
obj_ref2.test_negative()