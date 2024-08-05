import pytest


class TestClass:

    def test_LoginByEmailOne(self):
        print("this is login by email")
        assert True == True

    def test_LoginByPasswordTwo(self):
        print("this is login by Password")
        assert True == True

    def test_LoginByGoogleThree(self):
        print("this is login by Google")
        assert True == True
    #     if we add this below markser it will skip the methods 
    @pytest.mark.skip
    def test_SignupByEmailOne(self):
        print("this is login by email")
        assert True == True

    @pytest.mark.skip
    def test_SignupByPasswordTwo(self):
        print("this is login by Password")
        assert True == True

    @pytest.mark.skip
    def test_SignupGoogleThree(self):
        print("this is login by Google")
        assert True == True
