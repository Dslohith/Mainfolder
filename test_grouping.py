import pytest

# to excute only spefic task we need to create the grouping
class TestMethod:
    @pytest.mark.sanity
    def test_LoginByEmail(self):
        print("login by email---1")
        assert 1 == 1

    @pytest.mark.sanity
    def test_LoginByFacebook(self):
        print("login by facebook---1")
        assert 1 == 1

    @pytest.mark.sanity
    def test_LoginByTwitter(self):
        print("login by twitter---1")
        assert 1 == 1

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_signinByEmail(self):
        print("login by email---1")
        assert 1 == 1

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_signinByTwitter(self):
        print("login by twitter---1")
        assert 1 == 1

    @pytest.mark.regression
    def test_signnByFacebook(self):
        print("login by facebook---1")
        assert 1 == 1


