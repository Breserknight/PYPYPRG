import os
import zipfile


# with open("caliber.txt", "w+") as file:
    # file.write(f"\n\n{'SI' : <5}{'Username' : ^50}{'Password' : ^50}{'Website':>20}")

with zipfile.ZipFile("pop.zip") as zip:
    zip.extract("caliber.txt")


SI = 1
usr = "Test_Name"
pwd = "Test_Pass"
site = "www.Test_Case.com"

with open("caliber.txt", "a+") as file:
    file.write(f"\n\n{SI : <5}{usr:^50}{pwd:^50}{site:>20}")

with zipfile.ZipFile("pop.zip", "w") as zip:
    zip.write("caliber.txt")

os.remove("caliber.txt")