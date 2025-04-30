# Представьте, что это старая библиотека, которая умеет работать только с форматом CSV
class CSVConverter:
    def __init__(self, csv_data):
        self.csv_data = csv_data

    def convert_to_csv(self):
        return self.csv_data

import json

class JSONConverter:
    def __init__(self, json_data):
        self.json_data = json_data

    def convert_to_json(self):
        return json.dumps(self.json_data)

class CSVToJSONAdapter:
    def __init__(self, csv_converter):
        self.csv_converter = csv_converter

    def convert_to_json(self):
        csv_string = self.csv_converter.convert_to_csv()

        lines = csv_string.strip().split('\n')
        if not lines:
            return json.dumps([])
        header = lines[0].split(',')
        data = []
        for line in lines[1:]:
            values = line.split(',')
            item = {}
            for i in range(len(header)):
                item[header[i]] = values[i]
            data.append(item)

        json_data = json.dumps(data)
        return json_data


if name == "__main__":
    csv_data = """name,age,city
John,30,New York
Jane,25,London"""
    csv_converter = CSVConverter(csv_data)
    adapter = CSVToJSONAdapter(csv_converter)
    json_result = adapter.convert_to_json()
    print(json_result)


#Вопрос:
#Для чего в данном коде используется паттерн Адаптер?
#Варианты ответа:
#a) Для увеличения производительности при конвертации данных.
#b) Для переиспользования функциональности, предоставляемой библиотекой, работающей с CSV данными, в коде, который ожидает JSON формат.
#c) Для обеспечения масштабируемости системы путем добавления новых типов данных без изменения существующего кода.
#d) Для обеспечения безопасности данных при их конвертации между разными форматами.
