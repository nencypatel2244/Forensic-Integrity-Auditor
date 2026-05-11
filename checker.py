import hashlib

# We are weighing the file that YOU changed in the folder
file_to_check = "Evidence_Folder\\History"

with open(file_to_check, "rb") as f:
    data = f.read()
    print("The Current Hash is:")
    print(hashlib.sha256(data).hexdigest())