import json


def save_to_json(links, filename):
    """
    saves extracted data to a json file
    :param links: list of links
    """
    data = []
    for link in links:
        data.append({"title": link[0], "link": link[1]})

    with open(filename, 'w') as outfile:
        json.dump(data, outfile)
