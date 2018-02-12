from typing import List

import config
import domo.models as models
import domo.callout as call

DatasetCollection: List[models.DOMODatasetBookmark] = []


# **************Load Datasets from Config*****************************
def LoadPrefabDatasets():
    if DatasetCollection is None or len(DatasetCollection) == 0:
        if len(config.DatasetDefinitions) > 0:
            for ds in config.DatasetDefinitions:
                DatasetCollection.append(models.DOMODatasetBookmark(ds))


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