import csv


def save_to_csv(links, filename):
    """
    saves extracted data to a csv file
    :param links: list of links
    """
    csvFile = open(filename, 'w', newline='', encoding='utf-8')
    csvWriter = csv.writer(csvFile)
    csvWriter.writerow(["title", "link"])
    for link in links:
        csvWriter.writerow([link[0], link[1]])
