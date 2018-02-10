import csv
from contextlib import closing
import codecs


def ExportStreamToCSV(exportPath: str, response_stream):
    # The lineterminator parameter is necessary to ensure we don't see blank lines between
    # each row of data. The cause is a mismatch between *nix new lines (\n) and
    # Windows new lines (\r\n)
    # https://stackoverflow.com/questions/35371043/use-python-requests-to-download-csv
    writer = csv.writer(open(exportPath, 'w'), lineterminator='\n', quotechar='"')

    with closing(response_stream) as r:
        reader = csv.reader(codecs.iterdecode(r.iter_lines(), 'utf-8'))

        index = 0
        for row in reader:

            if row[0] == "ClientName":
                row.append("QuarterStartDate")
            elif row[7] == "Current":
                row.append()

            writer.writerow(row)