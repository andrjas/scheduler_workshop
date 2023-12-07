- in Databricks anmelden
- Workspace -> Home -> Add -> Notebook
- load_data Notebook anlegen
- display_data Notebook anlegen

- Workflows -> Create job
- job_<namenskürzel> (z.B. job_arj)
- Tasks -> Add task
- load_data Task anlegen:
	- Type: Notebook
	- Source: Workspace
	- Path: .../load_data
	- Cluster: EtLITE Cluster
- Save Task

- Tasks -> Add Task
- display_data Task anlegen:
	- wie load_data
	- Depends on: load_data
	- Parameters: order_date = 2018-01-01
- Save Task

- Run now



Access Token für ADF anlegen:
- rechts oben auf den Usernamen -> User Settings
- Developer -> Access Tokens -> Manage
- Generate new token
	Comment: EtLITE
	Lifetime: 90
- Token kopieren!
