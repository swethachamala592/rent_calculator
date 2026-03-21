def rent_calculator():
    persons=int(input("enter number of persons="))
    room_rent=int(input("enter room rent="))
    water_bill=int(input("enter water bill="))
    electricity_bill=int(input("enter electricity bill="))
    furniture_rent=int(input("enter furniture rent="))
    groceries=int(input("enter groceries="))
    kitchen_appliances=int(input("enter kitchen appliances="))
    washing_products=int(input("enter washing products="))
    other_expenses=int(input("enter other expenses="))
    total_rent=room_rent+water_bill+electricity_bill+furniture_rent+groceries+kitchen_appliances+washing_products+other_expenses
    print("total rent=",total_rent)
    rentPer_person=total_rent//persons
    print("rent per person=",rentPer_person)
rent_calculator()
