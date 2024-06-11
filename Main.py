import Read
import Write
import Operation
import datetime

# Function to validate a name (only alphabets and spaces allowed)
def is_valid_name(name):
    return all(char.isalpha() or char.isspace() for char in name)


# Function to handle land renting process
def rent_land():
    invoices_content = []  # List to store invoice content strings

    while True:
        try:
            # Read all lands data
            lands = Read.read_lands()
            # Filter available lands (status='Available')
            available_lands = [land for land in lands if land['status'] == 'Available']
            # Check if any lands are available
            if not available_lands:
                print("No lands available:")
                return
            # Print header for available lands
            print("Available Lands:")
            print("-----------------------------------------------------------------------------------------------------------------")
            print("Kitta Number      City        Direction        Anna              Price          Status         ")
            print("-----------------------------------------------------------------------------------------------------------------")
            # Display details of each available land
            for land in available_lands:
                kitta_number = str(land['kitta_number']) + ' ' * (15 - len(str(land['kitta_number'])))
                city = land['city'] + ' ' * (15 - len(land['city']))
                direction = land['direction'] + ' ' * (15 - len(land['direction']))
                anna = str(land['anna']) + ' ' * (15 - len(str(land['anna'])))
                price = str(land['price']) + ' ' * (15 - len(str(land['price'])))
                status = land['status'] + ' ' * (15 - len(land['status']))
                print(kitta_number, city, direction, anna, price, status)
                print("-----------------------------------------------------------------------------------------------------------------")

            # Get customer name and validate it
            customer_name = input("Enter your name: ")
            while not is_valid_name(customer_name):
                print("Please enter a valid name (only alphabets and spaces allowed).")
                customer_name = input("Enter your name: ")
           
             # Get kitta number of the land to rent (as integer)
            kitta_number = int(input("Enter the kitta number of the land you want to rent: "))
            # Check if kitta number exists in available lands

            if kitta_number not in [land['kitta_number'] for land in available_lands]:
                print("Land with kitta number", kitta_number, "is not available for rent.")
                continue
            # Get rental duration (in months) as integer
            duration = int(input("Enter the duration of rent (in months): "))
            
            # Find the specific land details by kitta number
            land = Read.get_land_by_kitta_number(kitta_number)
            if land:
                available_anna = land["anna"]
                choice = input("Do you want to rent the entire available area (" + str(available_anna) + " anna)? (yes/no): ")
                if choice.lower() == 'yes':
                    selected_anna = available_anna
                elif choice.lower() == 'no':
                    selected_anna = int(input("Enter the number of anna you want to rent: "))
                    if selected_anna != available_anna:
                        print("You can only rent the entire available area (" + str(available_anna) + " anna).")
                        continue
                else:
                    print("Invalid choice. Please enter 'yes' or 'no'.")
                    continue
                # Calculate total price based on land price and selected anna using Operation module 
                total_price = Operation.calculate_land_price(land["price"], selected_anna)
                #generating the invoice using write module
                current_datetime = datetime.datetime.now()
                invoice_content = Write.print_rent_invoice(customer_name, land, land["price"], selected_anna, total_price, duration, current_datetime)
                invoices_content.append(invoice_content)
                print(invoice_content)
                #changing the land status to unavailable 
                lands = Read.read_lands()
                Operation.update_land_status(lands, [kitta_number], new_status='Unavailable')
                print("Land rented successfully!")
            else:
                print("Land with kitta number " + str(kitta_number) + " not found.")
                
            choice = input("Do you want to rent more lands? (yes/no): ").lower()
            if choice != 'yes':
                break

        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            continue

            

    # Combine invoice content and save to a file
    all_invoices_content = "\n\n".join(invoices_content)
    file_name = Write.save_invoice(all_invoices_content)
    print("Invoices saved in file:", file_name)

def return_land():
  invoices_content = []  # List to store invoice content strings

  while True:
    try:
      lands = Read.read_lands()
      unavailable_lands = [land for land in lands if land['status'] == 'Unavailable']
      if not unavailable_lands:
        print("There are no lands to return")
        return

      print("Unavailable Lands:")
      print("-----------------------------------------------------------------------------------------------------------------")
      print("Kitta Number   City           Direction      Anna           Price          Status         ")
      print("-----------------------------------------------------------------------------------------------------------------")
            # Display details of each available land
      for land in unavailable_lands:
          kitta_number = str(land['kitta_number']) + ' ' * (15 - len(str(land['kitta_number'])))
          city = land['city'] + ' ' * (15 - len(land['city']))
          direction = land['direction'] + ' ' * (15 - len(land['direction']))
          anna = str(land['anna']) + ' ' * (15 - len(str(land['anna'])))
          price = str(land['price']) + ' ' * (15 - len(str(land['price'])))
          status = land['status'] + ' ' * (15 - len(land['status']))
          print(kitta_number, city, direction, anna, price, status)
          print("-----------------------------------------------------------------------------------------------------------------")

      customer_name = input("Enter your name: ")
      while not is_valid_name(customer_name):
        print("Please enter a valid name (only alphabets and spaces allowed).")
        customer_name = input("Enter your name: ")


      kitta_number = int(input("Enter the kitta number of the land you want to return: "))

      # Check if kitta number exists in unavailable lands
      if kitta_number not in [land['kitta_number'] for land in unavailable_lands]:
        print("Land with kitta number", kitta_number, "is not available for return.")
        continue

      selected_land = None
      for land in unavailable_lands:
        if land['kitta_number'] == kitta_number:
          selected_land = land
          break

      if not selected_land:
        print("Land with kitta number" + str(kitta_number) + "is not available for return.")
        continue

      
      rental_months = int(input("Enter the number of months the land was rented for: "))
      total_price = Operation.calculate_land_price(selected_land["price"], selected_land['anna'])
      returned_months = int(input("Enter the number of months the land was returned after: "))
      fine = Operation.calculate_fine(total_price, rental_months, returned_months) 
      current_datetime = datetime.datetime.now()
      invoice_content = Write.print_return_invoice(customer_name, land, total_price, rental_months, returned_months, fine, current_datetime)
      invoices_content.append(invoice_content)
      print(invoice_content)

      # Re-read lands after each return for consistency (assuming Read.read_lands updates data)
      lands = Read.read_lands()
      Operation.update_land_status(lands, [kitta_number], new_status='Available')
      print("Land returned successfully!")

      choice = input("Do you want to return more lands? (yes/no): ").lower()
      if choice != 'yes':
        break  # Exit the loop for multiple returns

    except ValueError:
      print("Invalid input. Please enter a valid integer.")
      continue

  # Combine invoice content and save to a file
  all_invoices_content = "\n\n".join(invoices_content)
  file_name = Write.save_invoice(all_invoices_content)
  print("Invoices saved in file:", file_name)


def display_welcome():
    print
    print("-----------------------------------------------------------------------------------------------------------------")
    print("-------------------------------------Welcome to Techno Property Nepal Portal-------------------------------------")
    print("-----------------------------------------------------------------------------------------------------------------")
    print("About Us: Techno Property Nepal is a top land rental and return company in Nepal")
    print("We focus on offering premium land for rent and guarantee smooth and efficient land return processes.")
    print("-----------------------------------------------------------------------------------------------------------------")
    print("Contact Us:")
    print("Address: Chhorepatan, Pokhara, Nepal")
    print("Email: contact@hamrotechnopropertynepal.com")
    print("Phone: +977-4360969")
    print("Thank you for choosing Techno Property Nepal! ")

display_welcome()
while True:
    print("-----------------------------------------------------------------------------------------------------------------")
    print("1. Rent a land")
    print("2. Return a land")
    print("3. Exit")
    print("-----------------------------------------------------------------------------------------------------------------")

    try:
        choice = input("Enter your choice: ")

        if choice == '1':
            rent_land()
        elif choice == '2':
            return_land()
        elif choice == '3':
            print("Thank you for using Techno Property Nepal Portal!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 3.")
    except Exception as e:
        print("An error occurred:", e)


