import os
import hashlib
import sys
import time

file_list = []

rootdir = "C:/Users/Aritro chakraborty/Desktop/C"

print("Program starting!")
print("[+]Collecting virus definitions and allocating memory[+]")

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        #print os.path.join(subdir, file)
        filepath = subdir + os.sep + file

        if filepath.endswith(".exe") or filepath.endswith(".dll"):
            file_list.append(filepath)
            #print(filepath)
print("[+]Virus definition and memory allocation complete...[+]")
print("[+]Starting scan...[+]")
def countdown():
    for x in range(4):
        print(x+1)
        time.sleep(1)

countdown()

def Scan():
    infected_list = []
    for f in file_list:
        virus_defs = open("VirusLIST.txt", "r")
        file_not_read = False
        print("\nScanning: {}".format(f))
        hasher = hashlib.md5()
        try:
            with open(f, "rb") as file:
                try:
                    buf = file.read()
                    file_not_read = True
                    hasher.update(buf)
                    FILE_HASHED = hasher.hexdigest()
                    print("File md5 checksum: {}".format(FILE_HASHED))
                    for line in virus_defs:
                        if FILE_HASHED == line.strip():
                            print("[!]Malware Detected[!] | File name: {}".format(f))
                            infected_list.append(f)
                        else:
                            pass
                except Exception as e:
                    print("Could not read file | Error: {}".format(e))
        except:
            pass
    print("Infected files found: {}".format(infected_list))
    deleteornot = str(input("Would you like to delete the infected files (y/n): "))
    if deleteornot.upper() == "Y":
        for infected in infected_list:
            os.remove(infected)
            print("File removed: {}".format(infected))
    else:
        print("Executed with exit code 0")
        os.system("PAUSE")
Scan()