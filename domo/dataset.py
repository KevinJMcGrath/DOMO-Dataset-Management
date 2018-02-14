from typing import List

import config
import data.export as export
import domo.models as models
import domo.callout as call

DatasetCollection: List[models.DOMODatasetBookmark] = []
UploadCollection: List[models.DOMODatasetBookmark] = []


# **************Load Datasets from Config*****************************
def LoadPrefabDatasets():
    if DatasetCollection is None or len(DatasetCollection) == 0:
        if len(config.SourceDatasetDefinitions) > 0:
            for ds in config.SourceDatasetDefinitions:
                DatasetCollection.append(models.DOMODatasetBookmark(ds))

    if UploadCollection is None or len(UploadCollection) == 0:
        if len(config.DestDatasetDefinitions) > 0:
            for ds in config.DestDatasetDefinitions:
                UploadCollection.append(models.DOMODatasetBookmark(ds))


LoadPrefabDatasets()
# ********************************************************************


def GetDatasetByShortname(shortname: str) -> models.DOMODatasetBookmark:
    for ds in DatasetCollection:
        if ds.ShortName == shortname:
            return ds
        else:
            return None


def GetDatasetSchemaFromDOMO(datasetId: str) -> models.DOMOSchemaFullDataset:
    schema_json = call.RetrieveDataset(datasetId)

    return models.DOMOSchemaFullDataset(schema_json)

# dsid = "ce442b07-934a-4a13-ac79-62efb96f1889"


def ExportDataset(dataset: models.DOMODatasetBookmark):
    exportPath = dataset.GetExportFullPath()

    export.ExportStreamToCSV(exportPath, call.StreamDatasetExport(dataset))