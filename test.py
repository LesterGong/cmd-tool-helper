import subprocess

subprocess.run(["osascript", "-e", 'tell application "Terminal" to activate'])
print("test")