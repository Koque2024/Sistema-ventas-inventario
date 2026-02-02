from database import connect

#obtener producto desde la bd
def get_products():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, price, stock FROM products")
    products = cursor.fetchall()
    conn.close()
    return products

#actualizar el stock de productos en funcion a la cantidad sumada/restada
def update_stock(product_id, quantity):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE products
        SET stock = stock - ?
        WHERE id = ?
    """, (quantity, product_id))
    conn.commit()
    conn.close()
