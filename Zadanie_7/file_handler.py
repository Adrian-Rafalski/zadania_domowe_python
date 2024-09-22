import csv


class FileHandler:
    def __init__(self, input_file, output_file, changes):
        self.input_file = input_file
        self.output_file = output_file
        self.changes = changes
        self.matrix = self.load_data_from_file()

    def load_data_from_file(self):
        temp_matrix = []
        with open(self.input_file) as file:
            reader = csv.reader(file)
            for line in reader:
                temp_line = []
                for number in line:
                    temp_line.append(number)
                temp_matrix.append(temp_line)
        return temp_matrix

    def save_data_to_file(self):
        with open(self.output_file, mode="w+") as file:
            writer = csv.writer(file)
            for line in self.matrix:
                writer.writerow(line)

    def transform(self):
        for transformation in self.changes:
            transformation_list = transformation.split(",")
            row = int(transformation_list[0])
            column = int(transformation_list[1])
            value = transformation_list[2]
            self.matrix[column][row] = value

    def display_matrix(self):
        for line in self.matrix:
            print(','.join(line))
