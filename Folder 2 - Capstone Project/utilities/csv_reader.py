import csv
import os


class CSVReader:

    @staticmethod
    def read_data():
        csv_path = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            "test_data",
            "test_data.csv"
        )

        with open(csv_path, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            return list(reader)