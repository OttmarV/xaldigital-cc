from fastapi import FastAPI
import uvicorn
import psycopg2
import db_engine as dbe
import os
from sql_queries import get_50_rows_from_users_table

POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_DB = os.getenv("POSTGRES_DB")
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "This is my database api"}


@app.post("/read")
async def read():
    try:

        params = {
            "host": POSTGRES_HOST,
            "database": POSTGRES_DB,
            "user": POSTGRES_USER,
            "password": POSTGRES_PASSWORD,
        }

        cur, conn = await dbe.create_connection(params)

        query = get_50_rows_from_users_table

        cur.execute(query)
        results = cur.fetchall()
        dbe.close_connection(cur, conn)
        return results

    except (Exception, psycopg2.Error) as error:
        msg = "Error while fetching data from PostgreSQL: {}".format(error)
        dbe.close_connection(cur, conn)
        return {"error": True, "message": msg}


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
