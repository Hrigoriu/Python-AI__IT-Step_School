from db import DB

class CustomerManager:
    def __init__(self, db:DB):
        self.db = db

    def list_customers(self, limit=10):
        query = 'SELECT customer_id, company_name, country FROM customers LIMIT %s;'
        result = self.db.execute(query, (limit,))
        return result

    def get_customer_by_id(self, customer_id: int):
        query = 'SELECT * FROM customers WHERE customer_id = %s;'
        result = self.db.execute(query, (customer_id,))
        return result

