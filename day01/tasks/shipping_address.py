name = "Taha Kerem"
building_number = 4
street_name = "2348 sk."
city = "Kocaeli"
state = "Turkey"
zip_code = 41400

def shipping_address():
    print(f'Your Shipping address is:\n'
          f'{name}\n'
          f'{building_number} {street_name}\n'
          f'{city}, {state} {zip_code}')

shipping_address()