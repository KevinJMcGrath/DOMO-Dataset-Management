import os
import sys

import domo.dataset as ds


clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')

sourceDS = None
destDS = None

validSource = False
validDest = False

print("\nStep 1: Select DOMO Dataset for EXPORT: \n")

while True:
    index = 1
    print(" "*3 + " \tName   \t\t\t\tShort Name \t\tGUID")
    for dataset in ds.DatasetCollection:
        print("[" + str(index) + "] \t" + dataset.Name + " \t " + dataset.ShortName + " \t " + dataset.Id + "\n")
        index += 1

    option1: str = input("\nEnter option number [e to exit]:")

    if option1.isnumeric():
        opt = int(option1)
        if 0 <= opt < index:
            sourceDS = ds.DatasetCollection[opt - 1]
            validSource = True
            break
        else:
            clear()
            print("\nInvalid Selection\n")
    elif option1 == "e":
        sys.exit()
    else:
        print("\nInvalid Selection\n")

while True:
    print("\nStep 2: Select DOMO Dataset for UPLOAD: \n")

    index = 1
    print(" " * 3 + " \tName   \t\t\t\tShort Name \t\tGUID")
    print("[0] \tCreate New Dataset")

    for dataset in ds.UploadCollection:
        print("[" + str(index) + "] \t" + dataset.Name + " \t " + dataset.ShortName + " \t " + dataset.Id + "\n")
        index += 1

    print("[n] \tDo not upload to DOMO.")

    option2: str = input("\nEnter option number [e to exit]:")

    if option2.isnumeric():
        opt = int(option2)
        if -1 <= int(opt) < index:
            destDS = ds.UploadCollection[opt - 1]
            validDest = True
            break
        else:
            clear()
            print("\nInvalid Selection\n")
    elif option2 == "n":
        break
    elif option2 == "e":
        sys.exit()
    else:
        print("\nInvalid Selection\n")

if sourceDS is not None and validSource:
    print("Downloading dataset. Please wait.\n")
    ds.ExportDataset(sourceDS)
    print("Dataset " + sourceDS.Name + " exported to " + sourceDS.GetExportFullPath() + "\n")
else:
    print("No valid source dataset selected. Exiting.")
    sys.exit()

if validSource and destDS is not None and validDest:
    print("Uploading data to " + destDS.Name)
else:
    print("No destination selected. Exiting")
    sys.exit()
