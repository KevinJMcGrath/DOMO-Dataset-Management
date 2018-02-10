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


def ExportDataSet(dataset: models.DOMODataset):
    exportPath = os.path.join(config.ExportDatasetPath, dataset.GetExportFilename())
    endpoint = "https://api.domo.com/v1/datasets/" + dataset.Id + "/data?includeHeader=true&fileName=" + exportPath

    reqHeaders = {
        "Content-Type": "application/json",
        "Authorization": "bearer " + DOMOAuth.Token
    }

    requests.get(endpoint, headers=reqHeaders, stream=True)

    print("Export complete.")






