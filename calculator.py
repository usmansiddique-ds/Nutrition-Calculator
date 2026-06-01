def calculate_nutrition(current_weight, goal_weight):
    """Calculate daily nutrition needs."""
    
    calories = current_weight * 24
    protein = goal_weight * 1.9
    fats = current_weight * 0.7
    fiber = (calories / 1000) * 14
    carbs = (calories - (protein * 4 + fats * 9)) / 4
    water = current_weight * 0.033

    return {
        'calories': round(calories, 1),
        'protein': round(protein, 1),
        'fats': round(fats, 1),
        'fiber': round(fiber, 1),
        'carbs': round(carbs, 1),
        'water': round(water, 2)
    }

def calculate_bmr(weight, height, age, gender):
    """Calculate Basal Metabolic Rate."""
    if gender == 'male':
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    else:
        bmr = 10 * weight + 6.25 * height - 5 * age - 161
    return round(bmr, 1)

def calculate_tdee(bmr, activity):
    """Calculate Total Daily Energy Expenditure."""
    multipliers = {
        'sedentary': 1.2,
        'light': 1.375,
        'moderate': 1.55,
        'active': 1.725,
        'very_active': 1.9
    }
    return round(bmr * multipliers[activity], 1)

def predict_transformation(current, goal, calories):
    """Predict week by week transformation."""
    predictions = {}
    weight = current
    
    if current > goal:
        weekly_change = (current - goal) / 12
    else:
        weekly_change = (goal - current) / 12
        
    for week in range(1, 13):
        if current > goal:
            weight = max(goal, 
                        current - (weekly_change * week))
        else:
            weight = min(goal,
                        current + (weekly_change * week))
        predictions[f'Week {week}'] = round(weight, 1)
    return predictions