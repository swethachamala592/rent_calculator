
# Function to calculate and split rent among persons
def rent_calculator():
 # Taking input for number of persons and various expenses
    persons=int(input("enter number of persons="))
    if persons<=0:
        print("invalid input")
        return
    room_rent=int(input("enter room rent="))
    if room_rent<0:
        print("invalid input")
        return
    water_bill=int(input("enter water bill="))
    if water_bill<0:
        print("invalid input")
        return
    electricity_bill=int(input("enter electricity bill="))
    if electricity_bill<0:
        print("invalid input")
        return
    furniture_rent=int(input("enter furniture rent="))
    if furniture_rent<0:
        print("invalid input")
        return
    groceries=int(input("enter groceries="))
    if groceries<0:
        print("invalid input")
        return
    kitchen_appliances=int(input("enter kitchen appliances="))
    if kitchen_appliances<0:
        print("invalid input")
        return
    washing_products=int(input("enter washing products="))
    if washing_products<0:
        print("invalid input")
        return
    other_expenses=int(input("enter other expenses="))
    if other_expenses<0:
        print("invalid input")
        return
    total_rent=room_rent+water_bill+electricity_bill+furniture_rent+groceries+kitchen_appliances+washing_products+other_expenses
    # Display total rent and rent per person
    print("total rent=",total_rent)
    rentPer_person=total_rent/persons
    print("rent per person=",rentPer_person)
# Calling the rent calculator function
rent_calculator()

