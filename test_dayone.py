import pytest

class TestClass:
    @pytest.fixture()
    # this will excuate at in the begning
    def setup(self):
        print("this contains logins and other credentials")
        yield
        print("this cosing method")
        # /yeild will excuate at the end of the project
    def testHome(self,setup):
        print("one method")
    def testMainpage(self,setup):
        print("secound method")
    def testInsidepage(self,setup):
        print("third method")