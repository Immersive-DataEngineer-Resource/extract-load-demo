from google.cloud import bigquery


def write_to_bigquery(table_id, rows_to_insert):
    client = bigquery.Client()
    table = client.get_table(table_id)
    errors = client.insert_rows(table, rows_to_insert)
    if errors:
        print("Encountered errors while inserting rows: {}".format(errors))


table_id = "your_project.your_dataset.your_table"
rows_to_insert = [(u"Phred Phlyntstone", 32), (u"Wylma Phlyntstone", 29)]
write_to_bigquery(table_id, rows_to_insert)
