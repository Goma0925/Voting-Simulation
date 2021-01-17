import os

class DataPointBuffer:
    def __init__(self, file_name: os.path):
        self.file_name = file_name
        self.csv = []

    def write(self, x: str, y: str, z: str):
        self.csv.append(x + ",")
        self.csv.append(y + ",")
        self.csv.append(z)
        self.csv.append("\n")
        if len(self.csv) > 5:
            self.dump()

    def dump(self):
        csv = "".join(self.csv)
        with open(self.file_name, "a") as file:
            file.write(csv)
        print("Dumped data in " + self.file_name)
        self.csv.clear()
