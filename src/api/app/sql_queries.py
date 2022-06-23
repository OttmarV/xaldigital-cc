get_50_rows_from_users_table = """
        SELECT u.id, u.first_name, u.last_name, u.email, u.phone1, u.phone2,
        u.zip, u.address, u.city, u.state, d.department, c.company
        FROM users u
        left join companies c
        ON c.id = u.company_id
        left join departments d
        on d.id = u.department_id
        where u.company_id = c.id and u.department_id = d.id
        limit 50;
        """
