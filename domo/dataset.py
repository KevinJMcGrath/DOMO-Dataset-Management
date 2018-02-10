from typing import List

import config
import domo.models as models


DatasetCollection: List[models.DOMODataset] = []


# **************Load Datasets from Config*****************************
def LoadPrefabDatasets():
    if DatasetCollection is None or len(DatasetCollection) == 0:
        if len(config.DatasetDefinitions) > 0:
            for ds in config.DatasetDefinitions:
                DatasetCollection.append(models.DOMODataset(ds))


LoadPrefabDatasets()
# ********************************************************************


def GetDatasetByShortname(shortname: str) -> models.DOMODataset:
    for ds in DatasetCollection:
        if ds.ShortName == shortname:
            return ds
        else:
            return None


