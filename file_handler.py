def read_file(filename):
    try:
        with open(filename, "r") as f:
            return f.readlines()
    except:
        return []

def write_file(filename, lines):
    with open(filename, "w") as f:
        f.writelines(lines)

def append_file(filename, data):
    with open(filename, "a") as f:
        f.write(data + "\n")