import subprocess
import json
import re
import os

try:
    # Global Variables
    Myinput = input("$Script  ")
    callingFile = Myinput.split(" ")[0]
    calling_File_Path_Name = Myinput.split(" ")[1]
    arguments_To_Call = re.split(f'{ calling_File_Path_Name} ', Myinput)[1]
    jsonPaths = ''
    subprocess_Arguments_Array = []


    def call_file():

        getPaths()
        global subprocess_Arguments_Array
        subprocess_Arguments_Array = [f"{jsonPaths[callingFile][calling_File_Path_Name]}"]
        totalArgument()

        fileCalled = subprocess.run(
            subprocess_Arguments_Array
        )
        return f"Exit code is {fileCalled.returncode}"


    def getPaths():
        directry = os.getcwd()
        paths = open(str(directry)+"/Paths.json", "r")
        global jsonPaths
        jsonPaths = json.loads(paths.read())
        paths.close()


    def totalArgument():
        splitArgument = arguments_To_Call.split(" ")
        for i in splitArgument:
            subprocess_Arguments_Array.append(i)


    totalArgument()
    call_file()
except Exception as e:
    print("for adding new path go to paths.json where you install Multi-Runner\nMore information visit manmohittaiya.com")