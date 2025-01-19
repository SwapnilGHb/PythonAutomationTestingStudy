class ExcelReader:

    @staticmethod
    def read_from_excel():
        print("Reading from excel")

class MYSQLDBConnection:
    @staticmethod
    def readMySQLFile():
        print("Reading from MySQL")


class TC1:

    def testcase(self):
        MYSQLDBConnection.readMySQLFile()
        ExcelReader.read_from_excel()

tc1_obj = TC1()
tc1_obj.testcase()

