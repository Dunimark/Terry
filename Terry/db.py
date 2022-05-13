import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="username",
  passwd="password",
  database="dbname"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE Entries (name VARCHAR(255), date_time DATETIME)")
    time = datetime.now()
    sql = "INSERT INTO Entries (name, date_time) VALUES (%s, %s)"
    val = ('{0.author.display_name} needs Support %s'.format(ctx), time)
    cursor.execute(sql, val)
    mydb.commit()