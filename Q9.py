def days_since_birthday():
    # Ask for the user's birthday
    birthday = input("Please enter your birthday in DD-MM-YYYY format: ")

    # Assuming the current year for demonstration purposes
    current_year = 2024

    # Extract the year from the birthday
    birth_year = int(birthday.split('-')[2])

    # Calculate the number of whole years excluding the birth year and the current year
    years = current_year - birth_year - 1

    # Count leap years in the range
    leap_years = 0
    for year in range(birth_year + 1, current_year):
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            leap_years += 1

    # Calculate total days (excluding days in the birth year and the current year)
    total_days = years * 365 + leap_years

    return total_days


# To run the function and print the result
print(days_since_birthday())
