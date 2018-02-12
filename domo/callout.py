import os
import requests

import domo.models as models
import config


DOMOAuth: models.DOMOAuthToken = None


def DomoAuthenticate():
    global DOMOAuth

    auth_tuple = (config.DOMOClientId, config.DOMOClientSecret)
    authEP = "https://api.domo.com/oauth/token?grant_type=client_credentials&scope=data user"

    if DOMOAuth is None or DOMOAuth.IsExpired():
        response = requests.post(authEP, auth=auth_tuple)

        if response.status_code == 200:
            resp_json = response.json()
            DOMOAuth = models.DOMOAuthToken(resp_json)


def GetDOMOAuthHeader():
    if DOMOAuth is None or DOMOAuth.IsExpired():
        DomoAuthenticate()

    return {
        "Content-Type": "application/json",
        "Authorization": "bearer " + DOMOAuth.Token
    }


def ExportDataSet(dataset: models.DOMODatasetBookmark):
    exportPath = os.path.join(config.ExportDatasetPath, dataset.GetExportFilename())
    endpoint = "https://api.domo.com/v1/datasets/" + dataset.Id + "/data?includeHeader=true&fileName=" + exportPath

    reqHeaders = GetDOMOAuthHeader()

    requests.get(endpoint, headers=reqHeaders, stream=True)

    print("Export complete.")


def CreateDataSet(schema_json):
    endpoint = "https://api.domo.com/v1/datasets"

    reqHeaders = GetDOMOAuthHeader()

    response = requests.post(endpoint, data=schema_json, headers=reqHeaders)

    print(response.content)


def RetrieveDataset(datasetId: str):
    endpoint = "https://api.domo.com/v1/datasets/" + datasetId

    reqHeaders = GetDOMOAuthHeader()

    response = requests.get(endpoint, headers=reqHeaders)

    return response.content


def TestSchemaSubmission(schema_json):
    url = "https://requestb.in/169shwu1"

    head = {"Content-Type": "application/json"}

    response = requests.post(url, data=schema_json, headers=head)

    print(response.content)




