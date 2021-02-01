import pickle


def save_object(obj, filename):
    """
    Saves python object as pickle file
    :param obj: object to be saved eg, dict,list,set,class...
    :return: None
    """
    with open(filename, 'wb') as output:  # Overwrites any existing file.
        pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)


def load_object(file_name):
    """
    load object from pickle file
    :param file_name: name of the file to load the object from
    :return:object
    """
    with open(file_name, "rb") as f:
        obj = pickle.load(f)
    return obj


list = ["Ashish", "test"]
save_object(list, "test.pkl")
l = load_object("test.pkl")
print(type(l))
print(l)
