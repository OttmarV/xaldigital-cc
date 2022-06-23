import db_engine as dbe
import os

POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_DB = os.getenv("POSTGRES_DB")
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
RAW_DATA = os.getenv("RAW_DATA")


class Pipeline:
    def __init__(self, params, staging_file):
        self.params = params
        self.staging_file = staging_file

    def run(self):
        tables = ["users", "companies", "departments"]
        columns_staging = [
            "first_name",
            "last_name",
            "company_name",
            "address",
            "city",
            "state",
            "zip",
            "phone1",
            "phone2",
            "email",
            "department",
        ]

        cur, conn = dbe.create_connection(self.params)
        dbe.drop_tables(cur, conn)
        dbe.create_tables(cur, conn)
        dbe.set_staging(cur, conn, self.staging_file, columns_staging)
        dbe.fill_from_staging_all(cur, conn)
        dbe.drop_table(cur, conn, "staging")
        count_tables = dbe.check_data(cur, conn, tables)

        for k, v in count_tables.items():
            print("Table {0} has {1} records".format(k, v))
        dbe.close_connection(cur, conn)


if __name__ == "__main__":

    params = {
        "host": POSTGRES_HOST,
        "database": POSTGRES_DB,
        "user": POSTGRES_USER,
        "password": POSTGRES_PASSWORD,
    }

    print(f"Database parameters: {params}")

    staging_file = RAW_DATA

    print(f"Raw data: {staging_file}")

    pipeline = Pipeline(params, staging_file)
    pipeline.run()
