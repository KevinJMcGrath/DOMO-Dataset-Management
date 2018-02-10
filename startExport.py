import datetime
import requests
import csv
from contextlib import closing
import codecs

import utility

today = datetime.datetime.today()
domoDatasetId = "7237f51d-b02c-4ffb-ba93-c9a8bd461b11"
exportFileName = "CBIData_Export_" + today.strftime("%m%d%y") + ".csv"
authToken = ""


def DOMOAuth():
    global authToken
    domoClientId = "d899de34-1789-4064-944a-a0a8778f5b8b"
    domoClientSecret = "19293be57420ce10ce2613c9afb698e2c30063e45fdacbcd1f9cb22f682f2cec"

    authEP = "https://api.domo.com/oauth/token?grant_type=client_credentials&scope=data user"
    response = requests.post(authEP, auth=(domoClientId, domoClientSecret))

    if response.status_code == 200:
        respJ = response.json()
        authToken = respJ['access_token']
        return True
    else:
        return False


def GetDataSet(datasetId, exportName):
    exportPath = "D:\DOMOExport\\" + exportName
    endpoint = "https://api.domo.com/v1/datasets/" + datasetId + "/data?includeHeader=true&fileName=" + exportPath

    reqHeaders = {
        "Content-Type": "application/json",
        "Authorization": "bearer " + authToken
    }

    # The lineterminator parameter is necessary to ensure we don't see blank lines between
    # each row of data. The cause is a mismatch between *nix new lines (\n) and
    # Windows new lines (\r\n)
    # https://stackoverflow.com/questions/35371043/use-python-requests-to-download-csv
    writer = csv.writer(open(exportPath, 'w'), lineterminator='\n', quotechar='"')
    with closing(requests.get(endpoint, headers=reqHeaders, stream=True)) as r:
        reader = csv.reader(codecs.iterdecode(r.iter_lines(), 'utf-8'))

        index = 0
        for row in reader:

            if row[0] == "ClientName":
                row.append("QuarterStartDate")
            elif row[7] == "Current":
                row.append()

            writer.writerow(row)

    print("Export complete.")


def ExportDataSet():
    if DOMOAuth():
        GetDataSet(domoDatasetId, exportFileName)


ExportDataSet()
