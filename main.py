import datetime

def ageCalc_fromcurrentAge(age, current_year):
    """

    :param age: An integer
    :param current_year: An integer
    This function will calculate your age if you will enter your current age.
    """
    ans = 2090 - current_year
    calculated_age = age + ans
    birth_year_of_user = current_year - age
    print(f"Your current \"Birth Year\" is {birth_year_of_user}")
    print(f"So your age by the year \"2090\" will be \"{calculated_age}\"")
    print(f"More over if you want to know your age in specific year than enter that specific year.")
    choice = int(input("Type \"1\" for yes otherwise \"0\" : "))
    specific_year = 0
    if choice == 1:
        specific_year = int(input("Enter year here : "))
    else:
        exit(1)

    if specific_year < birth_year_of_user:

        print("This year is not valid because this year is before your actual birth year. This would be your last chance of entering age.")
        specific_year = int(input("Enter year here : "))

    calculated_age = 0
    calculated_age = specific_year - birth_year_of_user
    print(f"Your age in \"{specific_year}\" will be \"{calculated_age}\"")


def ageCalc_frombirthYear(birth_year):
    """

    :param birth_year: An integer
    This function will calculate your age when you enter your birth year.
    """
    calculated_age = 2090 - birth_year
    current_age = current_year - birth_year
    print(f"Your current age is \"{current_age}\"")
    print(f"You will be \"{calculated_age}\" years old in \"2090\".")
    print("More over if you want to know your age in specific year than enter that specific year.")
    choice = int(input("Type \"1\" for yes otherwise \"0\" : "))
    specific_year = 0
    if choice == 1:
        specific_year = int(input("Enter year here : "))
    else : exit(1)
    if specific_year < birth_year:

        print("This year is not valid because this year is before your actual birth year. This would be your last chance of entering age.")
        specific_year = int(input("Enter year here : "))

    age_in_spec_year = 0
    age_in_spec_year = specific_year - birth_year
    print(f"Your age in {specific_year} will be \"{age_in_spec_year}\"")

if __name__ == '__main__':
    birth_year = 0
    current_year = datetime.date.today().year
    input_age = 0
    input_age = int(input("Enter your age or birth year : "))
    if input_age > current_year:
        print("Invalid Input because this year still has to come. This will be your last chance to enter age otherwise program will be ended.")
        input_age = int(input("Enter your age or birth year : "))
    if input_age >= 130 and input_age <= 1900:
        print("You are the oldest person alive.")
        ageCalc_fromcurrentAge(input_age, current_year)
    elif input_age > 1900:
        birth_year = input_age
        ageCalc_frombirthYear(birth_year)
    elif input_age < 130:
        ageCalc_fromcurrentAge(input_age, current_year)



