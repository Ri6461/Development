import Read
#function to calculate land price
def calculate_land_price(price, selected_anna):
    return price * selected_anna


#function to update land status
def update_status(file_name, lands):
    """
    Updates the status of lands in the text file.
    """
    with open(file_name, 'w') as file:
        for land in lands:
            land_data = str(land['kitta_number']) + " " + str(land['city']) + " " + str(land['direction']) + " " + str(land['anna']) + " " + str(land['price']) + " " + str(land['status']) + "\n"
            file.write(land_data)

def update_land_status(lands, kitta_numbers, new_status):

    for land in lands:
        if land['kitta_number'] in kitta_numbers:
            land['status'] = new_status
    update_status('lands.txt', lands)

#function to calculate fine
def calculate_fine(total_price, rental_months, returned_months):
    fine_percentage = 0.2  # 20% fine per month
    fined_months = returned_months - rental_months
    fine = fine_percentage * total_price * fined_months
    return fine


