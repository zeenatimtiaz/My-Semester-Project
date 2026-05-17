# Check if input field is empty
def check_empty(value):

    if value.strip() == "":
        return True

    return False


# Format product price
def format_price(price):

    return "PKR " + str(price)