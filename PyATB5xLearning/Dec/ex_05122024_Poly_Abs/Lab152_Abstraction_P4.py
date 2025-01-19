from abc import ABC, abstractmethod

class ExcelReader(ABC):
    @abstractmethod
    def readFromExcel(self):
        pass

class Browser(ExcelReader):
    @abstractmethod
    def startBrowser(self):
        pass

    def stopBrowser(self):
        pass
class Hidden(Browser):
    @abstractmethod
    def hidden(self):
        print("Hidden")

class TC1(Browser):
    def startBrowser(self):
        print("Starting")

    def stopBrowser(self):
        print("Stopping")

    def readFromExcel(self):
        print("readFromExcel is ready")

    def runTc(self):
        self.startBrowser()
        self.readFromExcel()
        self.stopBrowser()


tc1 = TC1()
tc1.runTc()