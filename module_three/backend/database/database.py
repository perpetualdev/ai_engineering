from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from pymysql.constants import CLIENT
from dotenv import load_dotenv
import os

load_dotenv()

# dialect+driver://username:password@host:port/database

db_url=os.getenv("dburl")

engine = create_engine(db_url, connect_args={"client_flag": CLIENT.MULTI_STATEMENTS}) # pyright: ignore[reportArgumentType]

session = sessionmaker(bind=engine)

db = session()

# # ==== Select all the users from the user table =====
# query = text("SELECT * FROM user")

# # ===== pass the query into the db and put it in a variable called users ======
# users = db.execute(query).fetchall()

# # ==== display these users in the console ========
# print(users)

create_table_query = text("""
CREATE TABLE IF NOT EXISTS courses (
  id INT AUTO_INCREMENT PRIMARY KEY,
  title VARCHAR(100) NOT NULL,
  level VARCHAR(100) NOT NULL  
);
                          
CREATE TABLE IF NOT EXISTS users(
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  email VARCHAR(100) NOT NULL,
  password VARCHAR(100) NOT NULL
);                    
                          
CREATE TABLE IF NOT EXISTS enrollments (
  id INT AUTO_INCREMENT PRIMARY KEY,
  userid INT,
  courseId INT,
  FOREIGN KEY (userId) REFERENCES users(id),
  FOREIGN KEY (courseId) REFERENCES courses(id)
);
""")

db.execute(create_table_query)
print("Tables have been created successfully")
