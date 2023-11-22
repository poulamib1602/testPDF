# pdf_app/database_operations.py
from django.db import connection
from django.http import JsonResponse

def create_table_if_not_exists():
    create_table_query = """
    CREATE TABLE IF NOT EXISTS demo (
        section VARCHAR NOT NULL,
        question_no VARCHAR NOT NULL,
        marks VARCHAR NOT NULL,
        question TEXT NOT NULL,
        answer TEXT NOT NULL
    );
    """

    try:
        with connection.cursor() as cursor:
            # Create the table
            cursor.execute(create_table_query)

        print("Table created successfully.")

    except Exception as e:
        print("Error:", e)

def insert_data(final_QA):
    insert_query = """
    INSERT INTO demo (section, question_no, marks, question, answer) VALUES (%s, %s, %s, %s, %s);
    """

    try:
        with connection.cursor() as cursor:
            # Insert data into the table
            for item in final_QA:
                cursor.execute(insert_query, (item['section'], item['question_no'], item['marks'], item['question'], item['answer']))

        print("Data inserted successfully.")

    except Exception as e:
        print("Error:", e)


def get_demo_data(request):
    try:
        # Connect to the database
        with connection.cursor() as cursor:
            # Execute a simple query to fetch all data from the demo table
            cursor.execute("SELECT * FROM demo")
            # Fetch all rows from the result set
            rows = cursor.fetchall()
            # print(rows)

        # Convert the result into a list of dictionaries
        data = []
        for row in rows:
            data.append({
                'section': row[0],
                'question_no': row[1],
                'marks': row[2],
                'question': row[3],
                'answer': row[4],
            })

        # print("data", data)
        # Return the data as JSON response
        return data
    except Exception as e:
        print("Error:", e)