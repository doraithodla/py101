import pymysql
import sqlite3

HOST = "localhost"
USER_NAME = "root"
PASSWORD = ""
DB_NAME = "database.db"


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Exception as e:
        print(e)

    return None


# def create_connection(db):
#     """ create a database connection to the SQLite database
#         specified by db_file
#     :param db_file: database file
#     :return: Connection object or None
#     """
#     try:
#         conn = pymysql.connect(host=HOST,
#                                user=USER_NAME,
#                                password=PASSWORD,
#                                db=DB_NAME,
#                                charset='utf8mb4',
#                                cursorclass=pymysql.cursors.DictCursor)
#
#         return conn
#     except Exception as e:
#         print("Connection to the database could not be created: ", e)
#         return None


def create_tables(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        conn.commit()
    except Exception as e:
        print("Tables could not be created:", e)


def create_db():
    """
    A function used to create a database file to store all the data
    """
    connection = create_connection(DB_NAME)
    sql_create_sites_table = """ CREATE TABLE IF NOT EXISTS sites (
                                  id INTEGER PRIMARY KEY,
                                  link text NOT NULL,
                                  title text
                                ); """

    create_tables(conn=connection, create_table_sql=sql_create_sites_table)


# create_db()

def run_query(conn, query, args=[]):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param query: a SQL query
    :return:
    """
    cursor = conn.cursor()
    if query.lower().startswith("select"):
        cursor.execute(query, args)
        return cursor.fetchall()
    else:
        cursor.execute(query, args)
    try:
        conn.commit()
    except Exception as e:
        print("ERROR OCCURED WHILE DB COMMIT", e)
