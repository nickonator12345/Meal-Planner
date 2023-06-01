import random

# Define the meals for each day of the week along with their nutritional information
meals = {
    'Monday': {'calories': 450, 'protein': 30, 'carbs': 50, 'fat': 15},
    'Tuesday': {'calories': 350, 'protein': 25, 'carbs': 20, 'fat': 20},
    'Wednesday': {'calories': 400, 'protein': 35, 'carbs': 40, 'fat': 12},
    'Thursday': {'calories': 300, 'protein': 20, 'carbs': 30, 'fat': 10},
    'Friday': {'calories': 500, 'protein': 30, 'carbs': 40, 'fat': 25},
    'Saturday': {'calories': 550, 'protein': 40, 'carbs': 10, 'fat': 35},
    'Sunday': {'calories': 400, 'protein': 30, 'carbs': 20, 'fat': 18}
}

# Function to generate a random meal plan with macros based on a 2000 calorie diet
def generate_meal_plan():
    meal_plan = {}

    for day in meals.keys():
        print(f"What would you like for {day}?")
        print("Please enter the number corresponding to your choice:")
        for i, meal in enumerate(meals.keys(), start=1):
            print(f"{i}. {meal}")
        choice = int(input())

        selected_meal = list(meals.keys())[choice - 1]
        meal_plan[day] = {'name': selected_meal, 'calories': meals[selected_meal]['calories'],
                          'protein': meals[selected_meal]['protein'], 'carbs': meals[selected_meal]['carbs'],
                          'fat': meals[selected_meal]['fat']}

    # Calculate the remaining calories and macros based on a 2000 calorie diet
    total_calories = sum(meal['calories'] for meal in meal_plan.values())
    total_protein = sum(meal['protein'] for meal in meal_plan.values())
    total_carbs = sum(meal['carbs'] for meal in meal_plan.values())
    total_fat = sum(meal['fat'] for meal in meal_plan.values())

    remaining_calories = 2000 - total_calories
    remaining_protein = max(0, 50 - total_protein)
    remaining_carbs = max(0, 275 - total_carbs)
    remaining_fat = max(0, 65 - total_fat)

    # Add a snack to the meal plan to fulfill the remaining calories and macros
    snack = {'name': 'Snack', 'calories': remaining_calories, 'protein': remaining_protein,
             'carbs': remaining_carbs, 'fat': remaining_fat}
    meal_plan['Snack'] = snack

    return meal_plan

# Function to print the meal plan with macros
def print_meal_plan(meal_plan):
    for day, meal in meal_plan.items():
        print(day + ':', meal['name'])
        print('Calories:', meal['calories'])
        print('Protein:', meal['protein'], 'g')
        print('Carbs:', meal['carbs'], 'g')
        print('Fat:', meal['fat'], 'g')
        print()

# Generate and print the meal plan with macros
plan = generate_meal_plan()
print_meal_plan(plan)
