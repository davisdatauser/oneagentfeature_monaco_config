import requests 
import json
import os

# Define the URL and headers
url = 'https://XXXXXXXX.live.dynatrace.com/api/v2/entities'
envToken = os.environ["devToken"]
token = str('Api-Token ' + envToken)
headers = {
    'Authorization': token, # Your API Token environment variable
    'Content-Type': 'application/json; charset=utf-8', # Content-Type

}
params = {
    'entitySelector': 'type("PROCESS_GROUP"),tag("HostGroup:Test"),softwareTechnologies("JAVA")', # Replace with your entity selector
    'pageSize': '100', # Increase limit for larger clusters

}

# Perform the GET request
response = requests.get(url, headers=headers, params=params)

# Check for a valid response
if response.status_code == 200:
    # Parse the response JSON
    data = response.json()
    print(f'Response:\n' + str(data))
    
    # Initialize list to hold entity IDs, names
    entity_ids = []
    entity_names = []

    # Iterate through entities in data, save "entityId" and "displayName" values to entity_ids,entity_names
    if 'entities' in data:
        for entity in data['entities']:
            if 'entityId' in entity:
                print(f'EntityId in data: ' + str(entity['entityId']))
                entity_ids.append(entity['entityId'])
            else:
                continue
            if 'displayName' in entity:
                print(f'EntityName in data: ' + str(entity['displayName']))
                entity_names.append(entity['displayName'])
            else:
                continue

                
    # Create dictionary of names and IDs
    merged_dict = {entity_names[i]: entity_ids[i] for i in range(len(entity_names))}
    print(f'dict: ' + str(merged_dict))

    # Alternative data format in tuple list
    #scope_zip = zip(entity_names, entity_ids)
    #scope_tuple_list = list(scope_zip)

    # Save the dict or tuple list to a JSON
    with open('scope.json', 'w') as file:
        json.dump(merged_dict, file)

    print('Entity Ids, names saved to scope.json')

else:
    print(f'Error: Received status code {response.status_code} {response.reason} {response.raise_for_status}')
