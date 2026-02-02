import datetime
from database import connect

#total de iva calculado
IVA = 0.19

#calculo del total, iva y subtotal
def calculate_totals(items):
    subtotal = sum(item["subtotal"] for item in items)
    tax = subtotal * IVA
    total = subtotal + tax
    return subtotal, tax, total

#guardar venta en bd
def save_sale(total):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO sales (date, total)
        VALUES (?, ?)
    """, (datetime.date.today(), total))
    conn.commit()
    conn.close()
