"""
Name: Danielle Di Pace
sales_person.py

Problem: Creates a sales person with an ID number, name, and a list of their sales.
It can calculate the sales person's total sales, check if quota is met, and
compare total sales to other sale people.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


class SalesPerson:
    """
    Constructs a sales person with an ID number, name, and a list of their sales
    """
    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name
        self.sales = []

    def get_id(self):
        return self.employee_id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def enter_sale(self, sale):
        self.sales.append(sale)

    def total_sales(self):
        total = 0
        for sale in self.sales:
            total += sale
        return total

    def get_sales(self):
        return self.sales

    def met_quota(self, quota):
        if self.total_sales() >= quota:
            return True
        return False

    def compare_to(self, other):
        self_total = self.total_sales()
        other_total = other.total_sales()
        result_value = None

        if other_total > self_total:
            result_value = -1
        if other_total < self_total:
            result_value = 1
        if other_total == self_total:
            result_value = 0

        return result_value

    def __str__(self):
        return "{}-{}: {}".format(self.employee_id, self.name, self.total_sales())
