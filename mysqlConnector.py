import mysql.connector

class GetData:

    def __init__(self):

        self.con = None
        self.cur = None

    def createConnection(self):
        """
        To Stablish Db Connection

        :return: None
        """
        # Establishing a connection to the MySQL database
        self.con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Aarush123$",
            database="iail"
        )
        self.cur = self.con.cursor()

if __name__ == "__main__":
    obj = GetData()
    obj.createConnection()
   # print(obj.pullData("SELECT Distinct `Diagnostic Test Name` FROM lab_dataset"))
    print(obj.cur.execute("SELECT * FROM lab_dataset").fetchall)
