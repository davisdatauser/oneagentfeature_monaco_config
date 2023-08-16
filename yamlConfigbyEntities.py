import json
import ruamel.yaml
import copy

def import_json_file(json_file_path):
    with open(json_file_path, 'r') as file:
        return json.load(file)

def import_yaml_file(yaml_file_path):
    yaml=ruamel.yaml.YAML()
    with open(yaml_file_path, 'r') as file:
        return yaml.load(file)

def save_yaml_file(dictionary, file_path):
    yaml=ruamel.yaml.YAML()
    with open(file_path, 'w') as file:
        yaml.dump(dictionary, file)


# Path to your JSON and YAML files
json_file_path = "scope.json"
yaml_file_path = "builtinoneagent.features\config_template.yaml"
new_yaml_file_path = "builtinoneagent.features\config.yaml"

# Load the data
json_data = import_json_file(json_file_path)
yaml_data = import_yaml_file(yaml_file_path)
print(f'DICTIONARY IDs IMPORTED FROM JSON')
#new_yaml_file = 


# Make a copy of the original YAML data
new_yaml_data = copy.deepcopy(yaml_data)


# Iterate through JSON data and append feature change to new YAML for each entity
dataLoad = []

for k, v in json_data.items():
    entity_name = k
    entity_id = v

    new_data = [
        {
            'id': str(entity_name) + '_context_logs',
            'config': {
                'name': str(entity_name),
                'template': 'feature_instrument_template.json',
                'skip': False,
                'parameters': {
                    'enabled': False,
                    'key': 'SENSOR_JAVA_LOG_ENRICHMENT'
                }
            },
            'type': {
                'settings': {
                    'schema': 'builtin:oneagent.features',
                    'schemaVersion': '1.5.7',
                    'scope': str(entity_id)
                }
            }
        },
        {
            'id': str(entity_name) + '_context_unstructured',
            'config': {
                'name': str(entity_name),
                'template': 'feature_template.json',
                'skip': False,
                'parameters': {
                    'enabled': False,
                    'key': 'JAVA_LOG_ENRICHMENT_UNSTRUCTURED'
                }
            },
            'type': {
                'settings': {
                    'schema': 'builtin:oneagent.features',
                    'schemaVersion': '1.5.7',
                    'scope': str(entity_id)
                }
            }
        }
    ]
    dataLoad.append(new_data[0])
    dataLoad.append(new_data[1])

# Load formatted config and save to new YAML file
output = {'configs': dataLoad}
save_yaml_file(output, new_yaml_file_path)
print(f'\nSAVED TO CONFIG.YAML')