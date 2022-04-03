# WRITE YOUR FUNCTIONS HERE

# Test 1 get pet shop name
def get_pet_shop_name(pet_shop):
    return pet_shop ["name"]

# Test 2 get total cash
def get_total_cash(cash):
    return cash ["admin"]["total_cash"]

# Test 3 & 4 add/remove cash
def add_or_remove_cash(pet_shop_admin, new_total_cash):
    pet_shop_admin["admin"]["total_cash"] += new_total_cash

# Test 5 gets total pets sold
def get_pets_sold(total_pets_sold):
    return total_pets_sold["admin"]["pets_sold"]

# Test 6 increase total number of pets sold
def increase_pets_sold(total_pets_sold, pet_shop):
   total_pets_sold ["admin"]["pets_sold"] += pet_shop

# Test 7 get total stock count
def get_stock_count(total_animals):
    return len(total_animals["pets"])

# Test 8 & 9 return list & number of pet breed
def get_pets_by_breed(pet_shop, breed):
    pets = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == breed:
            pets.append(pets)
    return pets 

# Test 10 & 11 gets pets by name
def find_pet_by_name(pet_shop, pet_name):
    for pet in pet_shop["pets"]:
        if pet["name"] == pet_name:
            return pet 

# Test 12 removes a pet by name
def remove_pet_by_name(pet_shop, pet_name):
    for pet in pet_shop["pets"]:
        if pet["name"] == pet_name:
            pet_shop["pets"].remove(pet)

# Test 13 add dictionary to list of dictionaries
def add_pet_to_stock(pet_shop, new_pet):
  pet_shop["pets"].append(new_pet)

# Test 14 get customer cash
def get_customer_cash(customer_name):
    return customer_name ["cash"]

# Test 15 remove customer cash
# def remove_customer_cash(customer, customer_cash):
#     customer["cash"] - customer_cash[100]
#     return ["cash"]

# Test 16
# def get_customer_pet_count(customer_pets):
#     pet_count = []
#     for pets in customer_pets["pets"]:
#         pet_count.append(pets)
#     return pet_count     

# Test 17
    
            



        
