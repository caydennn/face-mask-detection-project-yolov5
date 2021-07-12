import os, shutil 
cwd = os.getcwd()

modes = ["test", "train", "valid"]
# mode = "valid"

for mode in modes:
    directory = cwd + '/face_mask_dataset' + '/images/' + mode
    destination_directory = cwd + '/face_mask_dataset' + '/labels/' + mode

    print (directory)
            

    filesToMove = []

    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            print(os.path.join(directory, filename))
            filesToMove.append(os.path.join(directory, filename))
        else:
            continue


    for f in filesToMove:
        shutil.move(f, destination_directory)
