import pytest

# ordering the test steps can be done by two ways like we have to install pytest-ordering package and have to create
# order or else we can use defult markers as shown in below

class TestOrder:
    @pytest.mark.run(order=3)
    def test_Mthodsix(self):
        print("this is test method 3")

    @pytest.mark.run(order=2)
    def test_Mthodtwo(self):
        print("this is test method 2")

    @pytest.mark.run(order=1)
    def test_Mthodthour(self):
        print("this is test method 1")

    @pytest.mark.run(order=4)
    def test_Mthodthree(self):
        print("this is test method 4")

    @pytest.mark.run(order=5)
    def test_Mthodthfive(self):
        print("this is test method 5")

    @pytest.mark.run(order=6)
    def test_Mthodone(self):
        print("this is test method 6")
