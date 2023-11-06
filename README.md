# oneagentfeature_monaco_config

## Monaco Linux Install Steps (Required)
1. Download the latest version of Monaco, Windows install steps available: (Dynatrace Configuration as Code CLI tool https://www.dynatrace.com/support/help/manage/configuration-as-code/installation)
2. Rename executable to Monaco
3. Make the binary executable
4. Install CLI to central location in path (optional)
5. Run "monaco" to verify download CLI

## Prerequisites 
Install python >=3.8 and packages requests, json, os and ruamel.yaml

Once cloning the repo we will see our main configuration file (manifest.yaml) which requires the URL attribute to be changed to your tenant, and a devToken created with the following permissions:
-	Access problem and event fead, metrics, and topology
-	Read configuration
-	Write configuration
-	Read settings
-	Write settings
-	Read Entities

Leave the devToken variable as is in the manifest.yaml and export the token into your environment with the below command:

`export devToken=XXXXXXXXXXXXXXXXXXXXXXXXX`

### Set your Dynatrace Environment
Open the manifest.yaml file in the oneagentfeature_monaco_config directory and edit the "url" value to your intended environment. This same tenant url will need to be changed in the GET request of the "PG_ID_retrieval_template.py" file along with your scope detailed below.

Now that the Monaco environment has been configured, *we need to edit the url and scope of our config change in the “PG_ID_retrieval_template.py” script.* Adjust the entitySelector in the query params of the GET request to constrain the sensor toggle to only relevant process groups. Best approach for this project is creating an auto-tag to dynamically set your process group scope.

## Format the Config.yaml
Monaco requires a config.yaml file to determine project deployment; the python files formatJavaLogs.py or formatRUM.py parse the JSON to create the appropriate file structure depending on use-case. With these changes made, now we are ready to load the process groups and format into the yaml config file – run the following:

`python PG_ID_retrieval_template.py`

### Enable/Disable Real User Monitoring sensor
`python formatRUM.py`

### Enable/Disable Java Log Enrichment sensor
`python formatJavaLogs.py`

## Running the OneAgentfeature Config
First script loads the entityNames and IDs of all process groups in scope, and the second script formats the Monaco config.yaml based on the PG IDs. If you see “SAVED TO CONFIG.YAML” in the output and /builtinoneagent.features/config.yaml shows your loaded data, then we can initiate the Monaco config script by running the following in the onagentfeature_monaco_config directory:

`monaco deploy –dry-run manifest.yaml`

`monaco deploy manifest.yaml`

