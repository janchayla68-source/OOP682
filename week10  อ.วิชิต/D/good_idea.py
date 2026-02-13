from abc import ABC , abstractclassmethod

class Database(ABC):
  @abstractclassmethod
  def save(self, data):
    pass

class MySQLDatabase(Database):
  def save (self, data):
    print("Saving data to MySQL database")

class PostgresDatabase(Database):
  def save (self, data):
    print("Saving data to Postgres database")

class App:
  def __init__(self, database: Database):
    self.database = database

  def save_data(self, data):
    self.database.save(data)

# ส่งสิ่งที่ต้องใช้เข้าไป (Injection)
app = App(MySQLDatabase())
app = App(PostgresDatabase())