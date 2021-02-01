import random


def write_file(file_name):
    """
    writes ranfom lines to a file for testing
    :param file_name: file name provided by the user
    :return: None
    """
    with open(file_name, "w") as f:
        count = 0
        for i in range(random.randint(1, 100)):
            count += 1
            f.write(str(i))
            f.write("\n")


def line_count(file_name):
    """
    reads a file and returns the number of lines in the file
    :param file_name: name of the file to be read
    :return: number of lines in the file
    """
    with open(file_name, "r") as f:
        lines = f.readlines()
        return (len(lines))


write_file("something.txt")
print(line_count("something.txt"))
