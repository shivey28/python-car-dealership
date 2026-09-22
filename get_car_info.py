def get_car_info(makes: list[str], years: list[int],
                 prices: list[int], choice: int) -> str:
    """
    input: list of makes, years, prices and choice from main()
    process: indexes the lists based on user choice
    output: string returning vehicle details
    """
    make = makes[choice]
    year = years[choice]
    price = prices[choice]

    return f"${price}: A {make} made in {year}"


def add_car(makes: list[str], years: list[int],
            prices: list[int]) -> str:
    """
    input: list of makes, years, prices from main()
    process: asks user for new car information and appends it to lists
    output: string if successfully added
    """

    make = input("Enter make: ")

    # Make sure make is not empty
    while make.strip() == "":
        make = input("Please enter a valid make: ")

    # Validate year
    while True:
        try:
            year = int(input("Enter year: "))

            if year < 1886 or year > 2027:
                print("Please enter a valid year between 1886 and 2027.")
            else:
                break

        except ValueError:
            print("Please enter the year as a number.")

    # Validate price
    while True:
        try:
            price = int(input("Enter $ price: "))

            if price <= 0:
                print("Price must be greater than $0.")
            else:
                break

        except ValueError:
            print("Please enter the price as a number.")

    makes.append(make)
    years.append(year)
    prices.append(price)

    return "Successfully added"


def remove_car(makes: list[str], years: list[int],
               prices: list[int], choice: int) -> str:
    """
    input: list of makes, years, prices and choice from main()
    process: removes car info from lists
    output: string if successfully removed
    """

    make = makes[choice]

    makes.pop(choice)
    years.pop(choice)
    prices.pop(choice)

    return f"{make} successfully removed"


def main() -> None:
    """
    input: action and choice
    process: goes to user's action (add/remove car or view car),
             calls get_car_info and indexes the choice in the lists
    output: car details in string
    """

    makes = ['Maserati', 'Honda', 'Subaru', 'Fiat', 'Ford',
             'Porsche', 'Mazda', 'Lotus']

    years = [2004, 1989, 2002, 2016, 2008, 1989, 2023, 2011]

    prices = [18000, 2499, 6000, 8495, 15499, 33250, 34999, 63915]

    while True:
        print("\nCar Dealership")
        print("1) Add car")
        print("2) Remove car")
        print("3) View car")
        print("4) View all cars")
        print("5) Exit")

        # Validate action
        while True:
            try:
                action = int(input(
                    "Please enter a number for what action you would like to do: "
                ))

                if action < 1 or action > 5:
                    print("Please enter a number between 1-5.")
                else:
                    break

            except ValueError:
                print("Please enter a number.")

        # Add car
        if action == 1:
            print(add_car(makes, years, prices))

        # Remove car
        elif action == 2:

            if len(makes) == 0:
                print("There are no cars to remove.")
                continue

            print("\nCars:")
            for i in range(len(makes)):
                print(f"{i + 1}) {get_car_info(makes, years, prices, i)}")

            while True:
                try:
                    choice = int(input(
                        f"Enter car to remove (1-{len(makes)}): "
                    ))

                    if choice < 1 or choice > len(makes):
                        print(
                            f"Please enter a number between 1-{len(makes)}."
                        )
                    else:
                        break

                except ValueError:
                    print("Please enter a number.")

            choice = choice - 1

            print(remove_car(makes, years, prices, choice))

        # View one car
        elif action == 3:

            if len(makes) == 0:
                print("There are no cars to view.")
                continue

            print("\nCars:")
            for i in range(len(makes)):
                print(f"{i + 1}) {makes[i]}")

            while True:
                try:
                    choice = int(input(
                        f"Please enter a number between 1-{len(makes)}: "
                    ))

                    if choice < 1 or choice > len(makes):
                        print(
                            f"Please enter a valid number between "
                            f"1-{len(makes)}."
                        )
                    else:
                        break

                except ValueError:
                    print("Please enter a number.")

            choice = choice - 1

            print(get_car_info(makes, years, prices, choice))

        # View every car
        elif action == 4:

            if len(makes) == 0:
                print("There are no cars available.")
            else:
                print("\nAvailable Cars:")

                for i in range(len(makes)):
                    print(
                        f"{i + 1}) "
                        f"{get_car_info(makes, years, prices, i)}"
                    )

        # Exit
        else:
            print("Goodbye!")
            break


main()
