import csv

# Ingestion file csv in

def ingest_csv(cursor, connection, file_path="sales_data.csv"):

#   we have created a default function ingest_csv named took cursor, connection(from db) and file path then we will give
#   name same as the file named sales_data.csv in our case

    cursor.execute("DELETE FROM sales_data;")           #   cursor is is the class which contain sevral functions so we used execute function.                                                       #    
    connection.commit()                                 #   here we can write our SQL queries in cursor.execute function.

    with open(file_path, "r") as file:                  #   now we open the file as read mode and insert file_path which we have defined above.
        reader = csv.DictReader(file)                   #   now we create a varible and use DictReader function now it contain our file data

        for row in reader:                              #   throgh for loop we ittrate into our file and run this query which will insert the data
            cursor.execute("""
                INSERT INTO sales_data (sale_date, product_name, quantity, price)
                VALUES (%s, %s, %s, %s)
            """, (
                row["sale_date"],
                row["product_name"],
                int(row["quantity"]),
                float(row["price"])
            ))

    connection.commit()
    print("CSV data inserted successfully.")