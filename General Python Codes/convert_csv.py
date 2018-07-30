import os
import glob
import csv
from xlsxwriter.workbook import Workbook

filepath = r"O:/Medical Informatics-General/2018 iPatientCare Data Extracts/2018_07_02 - Copy/"
filepathsave = r"O:\\Medical Informatics-General\\2018 iPatientCare Data Extracts\\Test\\"
convertfolder = r"2018_07_02 - Copy\\"

for csvfile in glob.glob(os.path.join(filepath, '*.csv')):
    print(csvfile)
    workbook = Workbook(csvfile[:-4] + '.xlsx')
    worksheet = workbook.add_worksheet()
    with open(csvfile, 'rt') as f:
        reader = csv.reader(f)
        for r, row in enumerate(reader):
            for c, col in enumerate(row):
                worksheet.write(r, c, col)
    workbook.close()