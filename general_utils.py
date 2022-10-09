import pickle

def save_file(path, obj):
    try:
        with open(path, "wb") as fp: # write bytes
            pickle.dump(obj, fp)
    except Exception as err:
        print(err)

def load_file(path):
    try:
        with open(path, "rb") as fp: # read bytes
            return pickle.load(fp)
    except Exception as err:
        print(err)