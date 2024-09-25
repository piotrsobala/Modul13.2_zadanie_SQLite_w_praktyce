from ex_04_selecty_raw import *

conn = create_connection("database.db")

# wszystkie projekty
select_all(conn, "projects")

#print(select_all(conn, "projects"))


#wszystkie zadania
select_all(conn, "tasks")

#print(select_all(conn, "tasks"))


# wszystkie zadania dla projektu o id 1
select_where(conn, "tasks", project_id=1)

#print(select_where(conn, "tasks", project_id=1))

# wszystkie zadania ze statusem ended
select_where(conn, "tasks", status="ended")

print(select_where(conn, "tasks", status="ended"))