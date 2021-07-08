import os
cwd = os.getcwd()
directory = cwd + '/labels'


def getFirstChars(m):
    with open(m) as infile:
        return ''.join(line[0] for line in infile if line)
        



for filename in os.listdir(directory):
    if filename.endswith(".txt"):
        if '2' in getFirstChars(os.path.join(directory, filename)):
            print ('2 found in {}'.format(os.path.join(directory, filename)))
        # print(os.path.join(directory, filename))
    else:
        continue

