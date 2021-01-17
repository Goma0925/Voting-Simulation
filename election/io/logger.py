import os
import traceback

class ErrorLogger:
    def __init__(self, file: os.path):
        self.file = file

    def write(self, err: Exception):
        with open(self.file, "w") as file:
            file.write(err.__str__()+"\n")
            file.write(traceback.format_exc())
            print("Error caught in ErrorLogger. Check: " + str(self.file))
            print(traceback.format_exc())
