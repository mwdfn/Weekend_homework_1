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

    

