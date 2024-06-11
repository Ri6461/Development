import datetime

def print_rent_invoice(customer_name, land, price, selected_anna, total_price, duration, current_datetime):
    invoice_content =(
        "\nInvoice:\n" +
        "-----------------------------------------------------------------------------------------------------------------\n"
        "-------------------------------------Welcome to Techno Property Nepal Portal-------------------------------------\n"
        "-----------------------------------------------------------------------------------------------------------------\n\n"

        "Invoice Date: " + current_datetime.strftime("%Y-%m-%d %H:%M:%S") + "\n"
        "Customer Name: " + customer_name + "\n"
        "Kitta Number: " + str(land["kitta_number"]) + "\n"  # Convert kitta number to string
        "City: " + land["city"] + "\n"
        "Direction: " + land["direction"] + "\n"
        "Anna Available: " + str(land["anna"]) + "\n"  # Convert anna available to string
        "Selected Area (Anna): " + str(selected_anna) + "\n"  # Convert selected anna to string
        "Price: NPR " + str(price) + "\n"  # Convert price to string
        "Rental Duration: " + str(duration) + " months\n"  # Convert duration to string
        "Total Price: NPR " + str(total_price) + "\n"  # Convert total price to string 
    )
    return invoice_content



def save_invoice(invoice_content):
    desired_filename = input("Enter desired invoice filename: ")
    file_name = desired_filename + ".txt"  # Concatenate extension
    with open(file_name, "w") as file:
        file.write(invoice_content)
        file.write("\n\n") # Add a separator between invoices
        return file_name

            
def print_return_invoice(customer_name, land, total_price, rental_months, returned_months, fine, current_datetime):
    invoice_content =(
        "\nInvoice:\n"
        "-----------------------------------------------------------------------------------------------------------------\n"
        "-------------------------------------Welcome to Techno Property Nepal Portal-------------------------------------\n"
        "-----------------------------------------------------------------------------------------------------------------\n\n"

        "Invoice Date: " + current_datetime.strftime("%Y-%m-%d %H:%M:%S") + "\n"
        "Customer Name: " + customer_name + "\n"
        "Kitta Number: " + str(land["kitta_number"]) + "\n"  # Convert kitta number to string
        "Rental Duration: " + str(rental_months) + " months\n"  # Convert rental months to string
        "Returned After: " + str(returned_months) + " months\n"  # Convert returned months to string
        "Total Price: NPR " + str(total_price) + "\n"  # Convert total price to string (format as NPR)
        "Fine: NPR " + str(fine) + "\n"  # Convert fine to string (format as NPR)
        "Total Amount Due: NPR " + str(total_price + fine) + "\n"  # Convert total amount due to string (format as NPR)
        "Return Completed."
    )

    return invoice_content


