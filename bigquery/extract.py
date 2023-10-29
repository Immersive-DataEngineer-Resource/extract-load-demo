from google.cloud import bigquery


def read_from_bigquery(sql_query):
    client = bigquery.Client()
    query = client.query(sql_query)
    return [row for row in query.result()]


sql_query = "SELECT * FROM `your_project.your_dataset.your_table` LIMIT 100"
data_from_bigquery = read_from_bigquery(sql_query)
