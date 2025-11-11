thonimport json
import csv

class Exporter:
    def __init__(self, output_format='json'):
        self.output_format = output_format

    def export_to_json(self, data):
        with open('output.json', 'w') as outfile:
            json.dump(data, outfile, indent=4)

    def export_to_csv(self, data):
        with open('output.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(data[0].keys())  # writing header
            for row in data:
                writer.writerow(row.values())

    def export_data(self, data):
        if self.output_format == 'json':
            self.export_to_json(data)
        elif self.output_format == 'csv':
            self.export_to_csv(data)
        else:
            raise ValueError("Unsupported output format")