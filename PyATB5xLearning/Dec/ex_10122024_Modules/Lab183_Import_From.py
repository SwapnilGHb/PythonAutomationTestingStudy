from browserPackage.OpenBrowser import start_browser
from browserPackage.CloseBrowser import stop_browser

def test_case():
    start_browser()
    print("Hello Running TC")
    stop_browser()


test_case()

