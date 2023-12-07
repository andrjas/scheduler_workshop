import requests

response = requests.get('https://raw.githubusercontent.com/dbt-labs/jaffle_shop/main/seeds/raw_orders.csv')
csvfile = response.content.decode('utf-8')

username = dbutils.notebook.entry_point.getDbutils().notebook().getContext().userName().get().split("@")[0]
dbutils.fs.put(f"dbfs:/FileStore/raw_orders_{username}.csv", csvfile, True)
