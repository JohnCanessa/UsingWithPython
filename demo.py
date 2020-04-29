# **** file: demo.py ****

# **** import libraries and classes ****
import os


# **** file to write ****
fileName = "C:\\Temp\\output.txt"

# **** text to write ****
text = "This is a test. That's all folks"

# **** inform the user what is going on ****
print("write operation started...")

#**** open and write to the specified file ****
# try:
#     stream = open(fileName, "wt")
#     stream.write(text)
# except OSError:
#     print(f"open failed fileName ==>{fileName}<==")
#     os._exit(-1)
# finally:
#     stream.close()

# **** open and write to the specified file (automatically closes stream) ****
with open(fileName, "wt") as stream:
    stream.write(text)

# **** inform user of completed operation ****
print("write operation completed!!!")

# **** file to read ****
fileName = "c:\\temp\\README.txt"

# **** ****
print("read operation started...")

# **** open and read the specified file ****
try:
    with open(fileName, "rt") as stream:
        while True:
            line = stream.readline()
            if not line:
                break
            line = line.rstrip()
            if line == "":
                continue
            print(f"line ==>{line}<==")
except OSError:
    print(f"open fileName ==>{fileName}<== exception OSError")
    os._exit(-1)
except:
    print(f"open fileName ==>{fileName}<== failed")
    os._exit(-1)

# **** ****
print("write operation completed!!!")
