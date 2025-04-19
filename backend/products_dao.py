from sql_connection import get_sql_connection
import mysql.connector

def get_all_products(connection):

    cursor = connection.cursor()
    query  = "SELECT a.product_id, a.Name, a.uom_id, a.price_per_unit, b.uom_name FROM products a  INNER JOIN uom_table b ON a.uom_id = b.uom_id;"
    cursor.execute(query)

    response =[]

    for (product_id, Name, uom_id, price_per_unit, uom_name) in cursor:
        response.append(
        {
            'product_id': product_id,
            'Name': Name,
            'uom_id': uom_id,
            'price_per_unit': price_per_unit,
            'uom_name': uom_name
        }
        ) 
    return response

def insert_new_product(connection, product):
    cursor = connection.cursor()
    query = ("INSERT INTO products (Name, uom_id, price_per_unit) VALUES (%s, %s, %s)")
    data =(product['Name'], product['uom_id'], product['price_per_unit'])
    cursor.execute(query, data)
    connection.commit()
    print(f"Inserted {cursor.rowcount} rows")
    return cursor.lastrowid

def delete_product(connection, product_id):
    cursor = connection.cursor()
    query = ("DELETE FROM products WHERE product_id ="+ str(product_id))
    cursor.execute(query)
    connection.commit()
    print(f"Deleted {cursor.rowcount} rows")
    return cursor.rowcount

if __name__ == "__main__":
    connection = get_sql_connection()
    # print(insert_new_product(connection, {
    #     'product_name': 'potatoes',
    #     'uom_id': '1',
    #     'price_per_unit': 10
    # }))