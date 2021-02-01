import json
from database import create_connection, run_query

DB_NAME = "database.db"


def read_json(filename):
    """takes a json file and returns a json object"""

    with open(filename, "r") as f:
        return json.loads(f.read())


def to_db(json_data):
    """
    takes json object and sends it to the database
    :param json_data: json data loaded from file
    """
    for site in json_data:
        title = site["title"]
        link = site["link"]
        query = "INSERT into sites(link,title) VALUES(?,?)"
        conn = create_connection(DB_NAME)
        run_query(conn, query, [link, title])
        conn.close()


# to_db(read_json("links.json"))
