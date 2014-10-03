def main():
    print_underpaid_report("customer_orders.csv")
 

def create_customer_list(filename):

    customer_list = []

    f = open(filename)
    for line in f:
        customer_info = line.split(",")
        customer_list.append(customer_info)
    f.close()

    return customer_list


def check_for_underpaid(filename):

    underpaid = []

    customers = create_customer_list(filename)

    for customer in customers:
        if float(customer[2]) != float(customer[3]):
            underpaid.append(customer)

    return underpaid


def print_underpaid_report(filename):

    underpaid = check_for_underpaid(filename)

    for customer in underpaid:
        name = customer[1]
        amount_due = float(customer[2])
        price_paid = float(customer[3])
        print "%s paid $%.2f, expected $%.2f" % (name, price_paid, amount_due)


if __name__ == "__main__":
    main()
