import pytest


class TestClass:
    @pytest.mark.Sixth
    def test_Mthodsix(self):
        print("this is test method six")

    @pytest.mark.Second
    def test_Mthodtwo(self):
        print("this is test method two")

    @pytest.mark.Fourth
    def test_Mthodthour(self):
        print("this is test method four")

    @pytest.mark.Thired
    def test_Mthodthree(self):
        print("this is test method three")

    @pytest.mark.Fifth
    def test_Mthodthfive(self):
        print("this is test method five")

    @pytest.mark.First
    def test_Mthodone(self):
        print("this is test method one")
