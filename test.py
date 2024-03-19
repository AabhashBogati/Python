
class Table():
    def __init__(self, capacity):
        self.capacity = capacity
        self.customers = []

    def add_customers (self, name):
        if not self.available():
            return False
        self.customers.append(name)
        return True

    def available (self):
        return self.capacity - len(self.customers)


tables = Table(5)
customers = ["Peter", "John", "Rory", "Jake", "Don", "Terry", "Dylan"]

for cust in customers:
    
    if tables.add_customers(cust):
        print(f"A table has been booked to {cust}")
    else:
        print(f"No more tables available for {cust}")

