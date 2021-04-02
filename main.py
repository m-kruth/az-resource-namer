import json

with open('azure-resources.json') as azure_resources_file:
    azure_resources = json.load(azure_resources_file)
    azure_resources = dict(azure_resources)
    print(azure_resources['provider']['AnalysisServices']['entity'])
