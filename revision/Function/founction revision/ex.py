def party_planner(host, *guests, **food_table):
    print(f"Host: {host}")
    print("Guests:", guests)
    print("Food:", food_table)

party_planner("Alex", "Ben", "Sofyi", dessert="Ice Cream", drink="Juice")