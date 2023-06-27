def main():
    ### Ask User for user info
    print("Please enter the required information below:")
    name = input("Name: ")
    age = input("Age: ")
    height = input("Height in inches: ")
    weight = input("Weight in lbs: ")
    goal = input("What is your fitness goal? \n 1. Lose Fat \n 2. Gain Muscle \n 3. Gain Muscle and Lose Fat")
    activity_level = input("What is your activity level? \n 0 - Sedentary (No Exersize) \n 1 - Occasional (Exercise once every 2 weeks for approx 30 min. \n 2 - Light (Exercise once a week for approx 30 min \n 3 - Average (Exercise 2-3 times a week for approx 1-3 hours \n 4 - Daily (Exercise daily for approx 4-7 hrs \n 5 - Advanced (Intense daily exercise for approx 7-14 hrs")
    time_commitment = input("How much time can you commit to working out each week? \n 1. 3 Days/week \n 2. 4 Days/week \n 3. 5 Days/week \n 4. 6 Days/week \n")
    
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
        case "1":
            percent_bmr_change = .08
            
        case "2":
            percent_bmr_change = 1.2
        case "3":
            percent_bmr_change = 1

    ### Change activity_level_change based on user input
    match activity_level:
        case "0":
            activity_level_change = percent_bmr_change - 0.05
        case "1":
            activity_level_change = percent_bmr_change - 0.03
        case "2":
            activity_level_change = percent_bmr_change - 0.02
        case "3":
            activity_level_change = percent_bmr_change
        case "4":
            activity_level_change = percent_bmr_change + 0.015
        case "5":
            activity_level_change = percent_bmr_change + 0.03

    ### Adjust user calorie target based on user data
    calorie_target = bmr * activity_level_change

    ### Create Macro Profile
    protein = (calorie_target * .3)/4
    carbs = (calorie_target * .5)



if __name__ == '__main__':
    main()