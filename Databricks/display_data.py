username = dbutils.notebook.entry_point.getDbutils().notebook().getContext().userName().get().split("@")[0]
raw_orders = spark.read.format("csv").option("header", "true").option("inferSchema", "true").load(f"dbfs:/FileStore/raw_orders_{username}.csv")
raw_orders.createOrReplaceTempView(f"raw_orders_{username}")

order_dates = spark.sql(f"select distinct(order_date) from raw_orders_{username}").rdd.map(lambda row : row[0]).collect()
order_dates.sort()

dbutils.widgets.dropdown("order_date", "2018-01-01", [str(x) for x in order_dates])
display(raw_orders.filter(raw_orders.order_date == dbutils.widgets.get("order_date")))
