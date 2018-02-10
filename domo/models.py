from datetime import datetime
import utility


class DOMODataset:
    def __init__(self, dataset_json):
        self.Name: str = dataset_json['name']
        self.ShortName: str = dataset_json['shortname']
        self.Id: str = dataset_json['id']

    def GetExportFilename(self) -> str:
        return self.ShortName + "_" + datetime.today().strftime("%m%d%Y") + ".csv"

    def ExportData(self):
        pass


class DOMOAuthToken:
    def __init__(self, auth_json):
        self.Token: str = auth_json['access_token']
        self.Expires: datetime = utility.CurrentDateTimeAddSeconds(int(auth_json['expires_in']))
        self.UserId: str = str(auth_json['userId'])
        self.Role: str = auth_json['role']
        self.JTI: str = auth_json['jti']

    def IsExpired(self) -> bool:
        return self.Expires <= datetime.now()