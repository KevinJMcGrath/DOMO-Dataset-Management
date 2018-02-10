import codecs
import json
import os
# from string import Template

_configPath = os.path.abspath('./config.json')

with codecs.open(_configPath, 'r', 'utf-8-sig') as json_file:
    _config = json.load(json_file)

DOMOClientId = _config['domoClientId']
DOMOClientSecret = _config['domoClientSecret']

ExportDatasetPath = os.path.abspath(_config['exportFolder'])

DatasetDefinitions = _config['datasets']