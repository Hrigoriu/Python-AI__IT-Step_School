from db import DB


class OrderManager:
    def __init__(self, db: DB):
        self.db = db

    def get_orders_by_customer(self, customer_id: int, limit=5):
        query = '''
            SELECT order_id, order_date, ship_country
            FROM orders
            WHERE customer_id = %s
            ORDER BY order_date DESC
            LIMIT %s;
        '''
        result = self.db.execute(query, (customer_id, limit))
        return result
