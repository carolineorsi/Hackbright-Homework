MELON_COST = 1.00

def main():

    customer_data = open("customer_orders.csv")

    for customer in customer_data:
        cid, name, num_melons, amt_paid = customer.strip().split(',')
        amt_owed = int(num_melons) * MELON_COST
        amt_paid = float(amt_paid)

        if amt_paid != amt_owed:
            print "%s paid $%.2f, expected $%.2f" % (name, amt_paid, amt_owed)

    customer_data.close()
 

# def create_customer_list(filename):

#     customer_list = []

#     f = open(filename)
#     for line in f:
#         customer_info = line.split(",")
#         customer_list.append(customer_info)
#     f.close()

#     return customer_list


# def print_underpaid_report(filename):

#     customers = create_customer_list(filename)

#     for customer in customers:
#         name = customer[1]
#         amount_due = float(customer[2])
#         price_paid = float(customer[3])        
#         if amount_due > price_paid:
#             print "%s paid $%.2f, expected $%.2f" % (name, price_paid, amount_due)


if __name__ == "__main__":
    main()
