def read_lands():
  """Reads land data from 'lands.txt' and returns a list of dictionaries."""
  lands = []
  try:
    with open('lands.txt', 'r') as file:
      for line in file:
        # Split line into data elements (assuming whitespace separated)
        data = line.split()
        if len(data) >= 6:  # Ensure minimum data elements (6 columns)
          kitta_number = int(data[0])  # Convert first element (kitta number) to integer
          city = data[1]  # City name
          direction = data[2]  # Land direction
          anna = int(data[3])  # Land area (anna) - convert to integer
          price = int(data[4])  # Land price - convert to integer
          status = data[5]  # Land status
          # Create a dictionary for each land entry
          land_data = {
              'kitta_number': kitta_number,
              'city': city,
              'direction': direction,
              'anna': anna,
              'price': price,
              'status': status
          }
          lands.append(land_data)
  except FileNotFoundError:
    print("Error: Data file not found.")
  return lands


#created for rent_land()
def get_land_by_kitta_number(kitta_number):
  """
  Searches for a land with the given kitta number and returns its details (dictionary) or None if not found.
  """
  lands = read_lands()  # Get all land data from the file
  for land in lands:
    if land['kitta_number'] == kitta_number:
      return land  # Return land details if kitta number matches
  return None  # Return None if no matching land found


