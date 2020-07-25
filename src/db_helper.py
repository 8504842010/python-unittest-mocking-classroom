import  mysql.connector
import  json
class DbHelper:
    def __init__(self):
        self.dataBase = mysql.connector.connect(user='root',
                                       host='localhost',
                                       password="",
                                       database='solution')
    def get_maximum_salary(self):
        '''
        Implement the logic to find and return maximum salary from employee table
        '''
        cursorObject = self.dataBase.cursor()
        query = "SELECT max(salary) FROM employees"
        cursorObject.execute(query)
        myresult = cursorObject.fetchall()
        return (myresult[0][0])

    def get_minimum_salary(self):
        '''
        Implement the logic to find and return minimum salary from employee table
        '''
        cursorObject = self.dataBase.cursor()
        query = "SELECT min(salary) FROM employees"
        cursorObject.execute(query)
        myresult = cursorObject.fetchall()
        return (myresult[0][0])


if __name__ == "__main__":
    db_helper = DbHelper()
    min_salary = db_helper.get_minimum_salary()
    max_salary = db_helper.get_maximum_salary()
    print(max_salary)
    print(min_salary)