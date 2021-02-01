from get_website import extract_links, get
from write_csv import save_to_csv
from write_json import save_to_json
from get_rss import extract_links as extract_rss
from get_rss import get as get_rss
from database import create_db
from json_to_db import read_json, to_db
from db_to_csv import to_csv, get_sites
from db_to_json import get_sites_j, to_json
import os

files = os.listdir()

# Checking for database file
if "database.db" not in files:
    print("Creating sqlite DB")
    # creating db file if not present
    create_db()

# getting webpage and extracting links
URL = "http://www.ashish.ch"
links = extract_links(URL, get(URL))

# saving the links as csv and json
save_to_csv(links, "links.csv")
save_to_json(links, "links.json")

# sending data from json to db
to_db(read_json("links.json"))

# DB to csv
to_csv(get_sites())

# DB to json
to_json(get_sites_j())

# get RSS feeds
URL = "http://feeds.feedburner.com/TechCrunch/Android"
links = extract_rss(get_rss(URL))
save_to_csv(links, "links_rss.csv")
save_to_json(links, "links_rss.json")
