import os
import sqlite3
import uuid

import config


def CreateDatasetExportDatabse(datasetId: str):
    filename = datasetId + ".sqlite"
    dbpath = os.path.join(config.ExportDatasetPath, filename)

    conn = sqlite3.connect(dbpath)
    cur = conn.cursor()

    create_table_schema = """CREATE TABLE IF NOT EXISTS DOMO_Schema (
        Id text PRIMARY KEY,
        CreatedDate text);"""

    create_table_schema_detail = """CREATE TABLE IF NOT EXISTS DOMO_Schema_Detail (
        Id text PRIMARY KEY,
        Schema_Id text,
        Label text,
        Type text,
        FOREIGN KEY (Schema_Id) REFERENCES DOMO_Schema(Id));"""

    create_table_data = """CREATE TABLE IF NOT EXISTS DOMO_Data (
        Id text PRIMARY KEY,
        Import_Date text,
        Row_Id text,
        Col_Id text,
        Value text,
        FOREIGN KEY(Col_Id) REFERENCES DOMO_Schema_Detail(Id));"""

    if conn is not None:
        cur.execute(create_table_schema)
        cur.execute(create_table_schema_detail)
        cur.execute(create_table_data)
    else:
        print("Cannot connect to sqlite database at: " + dbpath)