import csv

# file path of the target text file
path = ''


class Text:
    def __init__(self, file, file_name):
        self.file = file
        self.file_name = file_name

    def read_file(self):
        with open(self.file, 'r') as f:
            a = f.read().strip()
            return a.upper()

    def combine(self):
        nw = self.read_file()
        words = nw.split()
        return words

    def split_character(self):
        special = '''!()-[]{};:'"\,<>./?”@#$%~^&*_+=-'''
        words = self.combine()
        nw = ""
        for w in words:
            if w not in special:
                nw += w + ','
        return nw.split(',')

    def write_file(self):
        with open(self.file_name, 'w', newline='', encoding='utf-8-sig') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow(['Words'])
            words = self.split_character()
            for w in words:
                csv_writer.writerow([w])
                print("writing: ", w)
            print("Writing successfully")
            f.close()


# pass file path and file name end with csv
name = 'newfile1.csv'
text_file = Text(path, name)
Text.write_file(text_file)
