def main():
    ### Ask User for user info
    print("Please enter the required information below:")
    name = input("Name: ")
    age = int(input("Age: "))
    height = float(input("Height in inches: "))
    weight = float(input("Weight in lbs: "))
    goal = int(input("What is your fitness goal? \n 1. Lose Fat \n 2. Gain Muscle \n 3. Gain Muscle and Lose Fat \n"))
    activity_level = int(input("What activity level can you commit to? \n 0 - Sedentary (No Exersize) \n 1 - Occasional (Exercise once every 2 weeks for approx 30 min) \n 2 - Light (Exercise once a week for approx 30 min) \n 3 - Average (Exercise 2-3 times a week for approx 1-3 hours) \n 4 - Daily (Exercise daily for approx 4-7 hrs) \n 5 - Advanced (Intense daily exercise for approx 7-14 hrs) \n"))
    time_commitment = int(input("How much time can you commit to working out each week? \n 1. 3 Days/week \n 2. 4 Days/week \n 3. 5 Days/week \n 4. 6 Days/week \n"))
    
    ### Calculate BMR
    bmr = 88.362+(13.397*(weight/2.205))+(4.799*(height*2.54))

    ### Initialize variables
    percent_bmr_change = 0
    activity_level_change = 0
    calorie_target = 0
    protein_adjustment = 0
    carb_adjustment = 0
    fat_adjustment = 0

    ### Change percent_bmr_change based on user input
    match goal:
        case 1:
            percent_bmr_change = .8
        case 2:
            percent_bmr_change = 1.2
        case 3:
            percent_bmr_change = 1

    ### Change activity_level_change based on user input
    match activity_level:
        case 0:
            activity_level_change = percent_bmr_change - 0.04
        case 1:
            activity_level_change = percent_bmr_change - 0.03
        case 2:
            activity_level_change = percent_bmr_change - 0.02
        case 3:
            activity_level_change = percent_bmr_change
        case 4:
            activity_level_change = percent_bmr_change + 0.015
        case 5:
            activity_level_change = percent_bmr_change + 0.03

    ### Adjust user calorie target based on user data
    calorie_target = round(bmr * activity_level_change)

    ### Create Macro Profile
    if goal == 1 and activity_level <= 2:
        protein_adjustment = .8
    elif goal == 1 and activity_level >= 3:
        protein_adjustment = 1
    if goal == 2 and activity_level <= 2:
        protein_adjustment = 1
    elif goal == 2 and activity_level >= 3:
        protein_adjustment = 1.2
    if goal == 3 and activity_level <= 2:
        protein_adjustment = .9
    elif goal == 3 and activity_level >= 3:
        protein_adjustment = 1.1

    ##### Do math to find what carbs and protein should be based off of the percentage protein in relation to total calories
    total_protein = (weight*protein_adjustment)*4
    protein_percent = total_protein/calorie_target
    remaining_percent = 1-protein_percent
    carb_adjustment= remaining_percent * .75
    fat_adjustment= remaining_percent * .25

    #### Macro Profile
    protein = round(weight*protein_adjustment)
    carbs = round((carb_adjustment*calorie_target)/4)
    fats = round((fat_adjustment*calorie_target)/9)

    #### Check that all macros add up to 1
    total_adjustment = protein_percent + carb_adjustment + fat_adjustment

    ### Get Program Type
    match time_commitment:
        case 1:
            program = "Full Body Program"
        case 2:
            program = "Upper/Lower"
        case 3:
            program = "PPL (5 days)"
        case 4:
            program = "PPL (6 days)"

    ### Display User Data
    print("Your Fitness Profile!")
    print("----------------------")
    print(bmr)
    print(activity_level_change)
    print(f"Target Daily Calories: {calorie_target}")
    print(f"Protein Reccomendation (grams): {protein}")
    print(f"Carb Reccomendation (grams): {carbs}")
    print(f"Fat Reccomendation (grams): {fats}")
    print("----------------------")
    print("Your Program")
    print(program)

if __name__ == '__main__':
    main()