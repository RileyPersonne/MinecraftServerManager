import subprocess
import sys


class Commands:
    status = "Start"
    process = subprocess.Popen(["powershell.exe"], stdin=subprocess.PIPE,
                               stdout=subprocess.PIPE, universal_newlines=True,
                               cwd="C://Users//dwalt//Downloads//BMC2//")

    def startserver(self):
        print("Starting server...")
        status = "Running"
        self.process.stdin.write(".//Start.ps1")

    def stopserver(self):
        print("Stopping server...")
        status = "Start"
        self.process.stdin.write("/stop")

    def ban(self, username):
        subprocess.run(["/ban"])