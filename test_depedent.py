# import pytest
#
#
# class TestHomepage:
#
#     @pytest.mark.dependency()
#     def test_login(self):
#         assert True
#
#     @pytest.mark.dependency(depends=['TestHomepage::test_login'])
#     def test_landing(self):
#         assert True
#     # now testinnercart and outercart or depedance on each other so test innercart will fail beacue its assert is false and
#     # test outcard will skip due to depedance
#     @pytest.mark.dependency(depends=['TestHomepage::test_landing'])
#     def test_innercart(self):
#         assert False
#
#     @pytest.mark.dependency(depends=['TestHomepage::test_login','TestHomepage::test_innercart'])
#     def test_outercard(self):
#         assert True
#
#     @pytest.mark.dependency(depends=['TestHomepage::test_login'])
#     def test_logout(self):
#         assert True
