from database import create_connection, run_query
from write_json import save_to_json

DB_NAME = "database.db"


def get_sites_j():
    """ returns the sites stored in DB """
    query = "select link,title from sites"
    conn = create_connection(DB_NAME)
    sites = run_query(conn, query)
    return sites

def to_json(sites):
    """converts data recieved from DB to csv format"""
    links = []
    for items in sites:
        links.append([items[1], items[0]])
        save_to_json(links,"from_db.json")


