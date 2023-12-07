- ADF -> Launch studio
- links Manage -> Connections -> Linked services
- +New -> Compute -> Azure Databricks -> Continue
	- Name: egal
	- Account selection method: From Azure Subscription
	- Azure subscription: ...
	- Databricks workspace: sbx-etlite-dbw
	- Select cluster: Existing interactive cluster
	- Authentication type: Access Token
	- Access Token: <paste own token>
	- Existing cluster ID: ...

- Author -> Pipelines ... -> New pipeline
	- Name: egal

- Parameters -> + New
	- Name: order_date
	- Type: String
	- Defualt value: 2018-01-01

- Activities -> Databricks -> Notebook (in die freie Fläche reinziehen)
	- General:
		- Name: load_data
	- Azure Databricks:
		- Databricks linkes service: auswählen
	- Settings:
		- Notebook path -> Browse
			- Users -> <username> -> load_data -> OK

- Activities -> Databricks -> Notebook (in die freie Fläche reinziehen)
	- General:
		- Name: display_data
	- Azure Databricks:
		- Databricks linkes service: auswählen
	- Settings:
		- Notebook path -> Browse
			- Users -> <username> -> display_data -> OK
		- Base parameters -> + New
			- Name: order_date
			- Value: @pipeline().parameters.order_date
				- über: Parameters -> order_date
			

- Activities verbinden:
	- aus load_data -> On success (grüner Hacken) nach display_data ziehen
	
- publish all

- Add trigger -> trigger now

- Add trigger -> New/Edit

