def calculate_bmi(weight, height_cm):
    height_m = height_cm / 100
    bmi = weight / (height_m ** 2)
    return round(bmi, 1)

def get_bmi_category(bmi):
    if bmi < 18.5:
        category = 'Underweight'
        emoji = '⚠️'
        message = 'You are underweight! Time to fuel your body right. Focus on nutrient rich foods and build those muscles! You got this! 💪'
    elif bmi < 25:
        category = 'Normal'
        emoji = '✅'
        message = 'Amazing! You are in the healthy range! Keep up the great work and stay consistent. Your body is thanking you every day! 🌟'
    elif bmi < 30:
        category = 'Overweight'
        emoji = '⚠️'
        message = 'No worries! Every journey starts with one step. You are already ahead by knowing your numbers. Lets crush those goals! 🔥'
    else:
        category = 'Obese'
        emoji = '🔴'
        message = 'Today is the best day to start! Small changes lead to big results. Believe in yourself — your transformation starts NOW! 💯'
    return category, emoji, message

def calculate_body_fat(bmi, age, gender):
    if gender == 'male':
        body_fat = (1.20 * bmi) + (0.23 * age) - 16.2
    else:
        body_fat = (1.20 * bmi) + (0.23 * age) - 5.4
    return round(body_fat, 1)

def calculate_lean_mass(weight, body_fat):
    lean = weight * (1 - body_fat / 100)
    return round(lean, 1)

def get_ideal_weight(height_cm, gender):
    height_m = height_cm / 100
    min_weight = round(18.5 * height_m ** 2, 1)
    max_weight = round(24.9 * height_m ** 2, 1)
    return min_weight, max_weight

def full_bmi_analysis(weight, height_cm, age, gender):
    bmi = calculate_bmi(weight, height_cm)
    category, emoji, message = get_bmi_category(bmi)
    body_fat = calculate_body_fat(bmi, age, gender)
    lean_mass = calculate_lean_mass(weight, body_fat)
    ideal_min, ideal_max = get_ideal_weight(height_cm, gender)
    return {
        'bmi': bmi,
        'category': category,
        'emoji': emoji,
        'message': message,
        'body_fat': body_fat,
        'lean_mass': lean_mass,
        'ideal_min': ideal_min,
        'ideal_max': ideal_max
    }
