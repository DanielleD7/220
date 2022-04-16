"""
Name: Danielle Di Pace
sales_force.py

Problem: Creates a sales force comprised of sales people. It can create sales people from a file,
create a quota report as a list, finds the top sellers, finds a specific sales person by id number,
and creates a dictionary with the frequency of each sale.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from sales_person import SalesPerson


class SalesForce:
    """
    Constructs a sales force with a list of sales people
    """
    def __init__(self):
        self.sales_people = []

    def add_data(self, file_name):
        people_file = open(file_name, "r")

        for line in people_file.readlines():
            split_line = line.split(",")
            person = SalesPerson(eval(split_line[0].strip()), split_line[1].strip())
            split_line = split_line[2].strip().split(" ")

            for sale in split_line:
                person.enter_sale(eval(sale))
            # nested for loop END

            self.sales_people.append(person)
        # for loop END
        people_file.close()

    def quota_report(self, quota):
        quota_list = []
        for person in self.sales_people:
            quota_list.append([person.get_id(), person.get_name(),
                               person.total_sales(), person.met_quota(quota)])

        return quota_list

    def top_seller(self):
        top_seller_list = []
        top_seller_person = self.sales_people[0]

        # Finds the person who is top in sales
        for person in self.sales_people:
            if top_seller_person.compare_to(person) == -1:
                top_seller_person = person

        # Compares the top seller person with each person to find ties
        for person in self.sales_people:
            if top_seller_person.compare_to(person) == 0:
                top_seller_list.append(person)

        return top_seller_list

    def individual_sales(self, employee_id):
        found_person = None
        for person in self.sales_people:
            if person.get_id() == employee_id:
                found_person = person

        return found_person

    def get_sale_frequencies(self):
        sale_freq_dict = {}

        for person in self.sales_people:
            for sale in person.get_sales():
                if not sale_freq_dict.get(sale):
                    sale_freq_dict[sale] = 0
                sale_freq_dict[sale] += 1
            # nested for loop END
        # for loop END
        return sale_freq_dict
