def read_files():
    file_contents = None

    def save_contents(filename):
        # Use 'nonlocal' because file_contents is in the enclosing function, not global
        nonlocal file_contents # subject of discussion here is the nonlocal keyword under the topic scope
        if file_contents is None:
            file_contents = []
        with open(filename, encoding= "utf-8") as fin:
            file_contents.append(fin.read())

    for filename in ['../note_35_41/alice.txt', '../note_35_41/NVDA.txt']:  #, 'CatsEye.txt']:
        save_contents(filename)

    return file_contents


print('\n'.join(read_files()))
