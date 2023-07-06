from django.shortcuts import render
from django.http import HttpResponse

from .models import FitnessProfile

def fitness_profile(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = int(request.POST.get('age'))
        height = float(request.POST.get('height'))
        weight = float(request.POST.get('weight'))
        goal = int(request.POST.get('goal'))
        activity_level = int(request.POST.get('activity_level'))
        time_commitment = int(request.POST.get('time_commitment'))

        # Calculate BMR
        bmr = 88.362 + (13.397 * (weight / 2.205)) + (4.799 * (height * 2.54))

        # Initialize variables
        percent_bmr_change = 0
        activity_level_change = 0
        calorie_target = 0
        protein_adjustment = 0
        carb_adjustment = 0
        fat_adjustment = 0

        # Change percent_bmr_change based on user input
        if goal == 1:
            percent_bmr_change = 0.9
        elif goal == 2:
            percent_bmr_change = 1.2
        elif goal == 3:
            percent_bmr_change = 1

        # Change activity_level_change based on user input
        if activity_level == 0:
            activity_level_change = percent_bmr_change - 0.05
        elif activity_level == 1:
            activity_level_change = percent_bmr_change - 0.03
        elif activity_level == 2:
            activity_level_change = percent_bmr_change - 0.02
        elif activity_level == 3:
            activity_level_change = percent_bmr_change
        elif activity_level == 4:
            activity_level_change = percent_bmr_change + 0.015
        elif activity_level == 5:
            activity_level_change = percent_bmr_change + 0.03

        # Adjust user calorie target based on user data
        calorie_target = round(bmr * activity_level_change)

        # Create Macro Profile
        if goal == 1 and activity_level <= 2:
            protein_adjustment = 0.8
        elif goal == 1 and activity_level >= 3:
            protein_adjustment = 1
        if goal == 2 and activity_level <= 2:
            protein_adjustment = 1
        elif goal == 2 and activity_level >= 3:
            protein_adjustment = 1.2
        if goal == 3 and activity_level <= 2:
            protein_adjustment = 0.9
        elif goal == 3 and activity_level >= 3:
            protein_adjustment = 1.1

        # Calculate macros
        total_protein = (weight * protein_adjustment) * 4
        protein_percent = total_protein / calorie_target
        remaining_percent = 1 - protein_percent
        carb_adjustment = remaining_percent * 0.75
        fat_adjustment = remaining_percent * 0.25

        protein = round(weight * protein_adjustment)
        carbs = round((carb_adjustment * calorie_target) / 4)
        fats = round((fat_adjustment * calorie_target) / 9)

        # Check that all macros add up to 1
        total_adjustment = protein_percent + carb_adjustment + fat_adjustment

        # Get Program Type
        if time_commitment == 1:
            program = "Full Body Program"
        elif time_commitment == 2:
            program = "Upper/Lower"
        elif time_commitment == 3:
            program = "PPL (5 days)"
        elif time_commitment == 4:
            program = "PPL (6 days)"

        # Create a FitnessProfile object and save it to the database
        fitness_profile = {
            'name':name,
            'age':age,
            'height':height,
            'weight':weight,
            'goal':goal,
            'activity_level':activity_level,
            'time_commitment':time_commitment,
            'calorie_target':calorie_target,
            'protein':protein,
            'carbs':carbs,
            'fats':fats,
            'program':program
        }
        

        # Create context dictionary
        context = {
            'fitness_profile': fitness_profile
        }
        if 'fitness_profile' in request.session:
            del request.session['fitness_profile']
        

        return render(request, 'fitness/input_form.html', context)

    return render(request, 'fitness/input_form.html')

