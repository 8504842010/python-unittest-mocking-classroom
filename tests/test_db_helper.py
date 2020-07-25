import  unittest
from unittest.mock import patch
from src.db_helper import DbHelper

class Test_Db_helper(unittest.TestCase):
    def setUp(self):
        self.help=DbHelper()
    def test_without_mocking(self):
        max=self.help.get_maximum_salary()
        min=self.help.get_minimum_salary()
        self.assertGreater(max,min)

    @patch('src.db_helper.DbHelper')
    def test_with_mocking(self,MockDatabase):
        obj=MockDatabase()
        obj.get_maximum_salary.return_value=4
        max=obj.get_maximum_salary()
        obj.get_minimum_salary.return_value=2
        min=obj.get_minimum_salary()
        self.assertGreater(max,min)

        #one more
