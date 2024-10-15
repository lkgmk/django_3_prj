import psycopg2

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'orm_query_db',
#         'USER': 'postgres',
#         'PASSWORD': 'admin123',
#         # 'HOST': 'w3-django-project.cdxmgq9zqqlr.us-east-1.rds.amazonaws.com',
#         'HOST': 'localhost',
#         'PORT': '5432'
#     }
# }

try:
    connection = psycopg2.connect(
        host="localhost",
        database="orm_query_db",
        user="postgres",
        password="admin123"
    )
    print("Connection successful")

    cursor = connection.cursor()

    # select_query = "select id, firstname from Author;"
    select_query = "select id, firstname, popularity_score from author where popularity_score > 9;"
    cursor.execute(select_query)
    data = cursor.fetchall()
    print("data :: ", data)

except Exception as e:
    print(f"An error occurred: {e}")

# finally:
#     # Close the connection
#     if cursor:
#         cursor.close()
#     if connection:
#         connection.close()
