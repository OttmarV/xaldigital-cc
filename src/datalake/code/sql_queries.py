# DROP TABLES
users_table_drop = "DROP TABLE IF EXISTS users"
departments_table_drop = "DROP TABLE IF EXISTS departments"
companies_table_drop = "DROP TABLE IF EXISTS companies"
staging_table_drop = "DROP TABLE IF EXISTS staging"

# CREATE TABLES

staging_table_create = """
CREATE TABLE IF NOT EXISTS staging(
        id SERIAL NOT NULL,
        first_name VARCHAR(100),
        last_name VARCHAR(100),
        company_name VARCHAR(100),
        address VARCHAR(100),
        city VARCHAR(50),
        state VARCHAR(2),
        zip VARCHAR(20),
        phone1 VARCHAR(25),
        phone2 VARCHAR(25),
        email VARCHAR(100),
        department VARCHAR(50),
        CONSTRAINT staging_pkey PRIMARY KEY(id)
);
"""

users_table_create = """
CREATE TABLE IF NOT EXISTS users(
        id SERIAL NOT NULL,
        first_name VARCHAR(100),
        last_name VARCHAR(100),
        email VARCHAR(100),
        phone1 VARCHAR(25),
        phone2 VARCHAR(25),
        zip VARCHAR(20),
        address VARCHAR(100),
        city VARCHAR(50),
        state CHAR(2),
        department_id INTEGER NOT NULL,
        company_id INTEGER NOT NULL,
        CONSTRAINT users_pkey PRIMARY KEY(id),
        CONSTRAINT users_department_id_fkey FOREIGN KEY (department_id) REFERENCES departments (id),
        CONSTRAINT users_company_id_fkey FOREIGN KEY (company_id) REFERENCES companies (id)
);
"""


departments_table_create = """
CREATE TABLE IF NOT EXISTS departments(
    id SERIAL NOT NULL,
    department VARCHAR(50),
    CONSTRAINT department_pkey PRIMARY KEY(id)
);
"""


companies_table_create = """
CREATE TABLE IF NOT EXISTS companies(
    id SERIAL NOT NULL, 
    company VARCHAR(100),
    CONSTRAINT company_pkey PRIMARY KEY(id)
);
"""

## FILL  TABLES FROM STAGING

users_fill_from_staging = """
INSERT INTO USERS (first_name, last_name, email, phone1, phone2, zip, address, city, state, department_id, company_id)
select 
    s.first_name,
    s.last_name,
    s.email, 
    s.phone1, 
    s.phone2, 
    s.zip, 
    s.address, 
    s.city, 
    s.state, 
    d.id as department_id, 
    c.id as company_id
from staging s
LEFT JOIN companies c
ON s.company_name = c.company
LEFT JOIN departments d
ON s.department = d.department;
"""

companies_fill_from_staging = """
    insert into companies (company)
    select distinct company_name
    from staging;
"""

departments_fill_from_staging = """
    insert into departments (department)
    select distinct department
    from staging;
"""


fill_table_queries = [
    companies_fill_from_staging,
    departments_fill_from_staging,
    users_fill_from_staging,
]
create_table_queries = [
    staging_table_create,
    departments_table_create,
    companies_table_create,
    users_table_create,
]
drop_table_queries = [
    users_table_drop,
    departments_table_drop,
    companies_table_drop,
    staging_table_drop,
]
