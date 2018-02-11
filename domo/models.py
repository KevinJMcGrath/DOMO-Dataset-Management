from enum import Enum
from typing import List

from datetime import datetime
import utility


class DOMOAuthToken:
    def __init__(self, auth_json):
        self.Token: str = auth_json['access_token']
        self.Expires: datetime = utility.CurrentDateTimeAddSeconds(int(auth_json['expires_in']))
        self.UserId: str = str(auth_json['userId'])
        self.Role: str = auth_json['role']
        self.JTI: str = auth_json['jti']

    def IsExpired(self) -> bool:
        return self.Expires <= datetime.now()


class DOMODatasetBookmark:
    def __init__(self, dataset_json):
        self.Name: str = dataset_json['name']
        self.ShortName: str = dataset_json['shortname']
        self.Id: str = dataset_json['id']

    def GetExportFilename(self) -> str:
        return self.ShortName + "_" + datetime.today().strftime("%m%d%Y") + ".csv"

    def ExportData(self):
        pass


class DOMODataType(Enum):
    String = 'STRING'
    Decimal = 'DECIMAL'
    LongInt = 'LONG'
    Double = 'DOUBLE'
    Date = 'DATE'
    Datetime = 'DATETIME'


class DOMOSchemaDataset:
    def __init__(self):
        self.name: str = ''
        self.description: str = ''
        self.rows: int = 0
        self.schema: DOMOSchemaColumnCollection = DOMOSchemaColumnCollection()

    def add_column(self, colName: str, colType: DOMODataType = DOMODataType.String):
        self.schema.columns.append(DOMOSchemaColumn(colName, colType))

    def ExportJSON(self):
        return utility.ExportModelToJSON(self)


class DOMOSchemaColumnCollection:
    def __init__(self):
        self.columns: List[DOMOSchemaColumn] = []


class DOMOSchemaColumn:
    def __init__(self, colName: str, colType: DOMODataType = DOMODataType.String):
        self.type = colType
        self.name = colName

    def to_json(self):
        return {"type": self.type.value, "name": self.name}


def CreateDemoData():
    ds = DOMOSchemaDataset()
    ds.name = 'Test Dataset'
    ds.description = 'Testing dataset creation from Python'
    ds.add_column('col1_name')
    ds.add_column('col2_name', DOMODataType.LongInt)

    return ds