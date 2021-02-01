import feedparser


def get(URL):
    return feedparser.parse(URL)


def extract_links(content):
    """
    extracts all hyperlinks from the html recieved and returns a list of them
    :param content: feed parser object of the webpage
    :return: list of URLS
    """
    links = []
    for post in content.entries:
        links.append((post.title, post.link))
    return links

# extract_links(get("http://feeds.feedburner.com/TechCrunch/Android"))
