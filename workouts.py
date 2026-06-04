WORKOUT_PLANS = {
    'Ectomorph': {
        'Weight Loss': {
            'frequency': '4 days/week',
            'focus': 'Light cardio + Strength',
            'workouts': [
                '🏋️ Monday: Chest & Triceps (45 min)',
                '🏃 Tuesday: 30 min light cardio',
                '🏋️ Wednesday: Back & Biceps (45 min)',
                '🏃 Thursday: 20 min HIIT',
                '🏋️ Friday: Legs (45 min)',
                '🚴 Weekend: Light cycling/walking'
            ],
            'tips': [
                '✅ Keep lifting intensity high',
                '✅ Eat more before/after workout',
                '✅ Avoid excessive cardio',
                '✅ Rest 48h between same muscle'
            ]
        },
        'Weight Gain': {
            'frequency': '5 days/week',
            'focus': 'Heavy Strength Training',
            'workouts': [
                '🏋️ Monday: Chest & Triceps (60 min)',
                '🏋️ Tuesday: Back & Biceps (60 min)',
                '🏋️ Wednesday: Legs (60 min)',
                '🏋️ Thursday: Shoulders (45 min)',
                '🏋️ Friday: Full Body (45 min)',
                '💪 Eat 500+ calories extra daily'
            ],
            'tips': [
                '✅ Focus on compound movements',
                '✅ Progressive overload (increase weight)',
                '✅ Sleep 8+ hours',
                '✅ Eat calorie-dense foods'
            ]
        }
    },
    'Mesomorph': {
        'Weight Loss': {
            'frequency': '5 days/week',
            'focus': 'Balanced Strength + Cardio',
            'workouts': [
                '🏋️ Monday: Chest (45 min)',
                '🏃 Tuesday: 30 min cardio',
                '🏋️ Wednesday: Back (45 min)',
                '🏋️ Thursday: Legs (45 min)',
                '🏃 Friday: 20 min HIIT',
                '🚶 Weekend: Hiking/walking'
            ],
            'tips': [
                '✅ Mix strength and cardio',
                '✅ Maintain muscle while losing fat',
                '✅ Track macros closely',
                '✅ Consistency is key'
            ]
        },
        'Muscle Building': {
            'frequency': '5 days/week',
            'focus': 'Progressive Overload',
            'workouts': [
                '🏋️ Monday: Chest & Triceps (60 min)',
                '🏋️ Tuesday: Back & Biceps (60 min)',
                '🏋️ Wednesday: Legs (60 min)',
                '🏋️ Thursday: Shoulders (45 min)',
                '🏋️ Friday: Arms (45 min)',
                '💪 Eat 300+ surplus calories'
            ],
            'tips': [
                '✅ Lift heavy (8-12 reps)',
                '✅ Increase weight weekly',
                '✅ Eat high protein',
                '✅ Rest 48-72h between muscle groups'
            ]
        }
    },
    'Endomorph': {
        'Weight Loss': {
            'frequency': '6 days/week',
            'focus': 'Heavy Cardio + Strength',
            'workouts': [
                '🏃 Monday: 40 min cardio',
                '🏋️ Tuesday: Full body (45 min)',
                '🏃 Wednesday: 40 min cardio',
                '🏋️ Thursday: Full body (45 min)',
                '🏃 Friday: 40 min HIIT',
                '🏃 Saturday: 30 min walking'
            ],
            'tips': [
                '✅ Cardio is your friend',
                '✅ Keep lifting for muscle',
                '✅ Eat high protein (prevents muscle loss)',
                '✅ Track calories strictly'
            ]
        },
        'Muscle Building': {
            'frequency': '5 days/week',
            'focus': 'Strength with Cardio',
            'workouts': [
                '🏋️ Monday: Chest & Triceps (60 min)',
                '🏃 Tuesday: 20 min cardio',
                '🏋️ Wednesday: Back & Biceps (60 min)',
                '🏃 Thursday: 20 min cardio',
                '🏋️ Friday: Legs (60 min)',
                '🚴 Weekend: Light activity'
            ],
            'tips': [
                '✅ Lift heavy (6-10 reps)',
                '✅ Light cardio to control weight',
                '✅ High protein intake',
                '✅ Don\'t bulk too aggressively'
            ]
        }
    }
}

def get_workout_plan(body_type, goal):
    """Get workout plan for body type and goal."""
    goal_key = {
        'Weight Loss': 'Weight Loss',
        'Weight Gain': 'Weight Gain',
        'Muscle Building': 'Muscle Building',
        'Maintenance': 'Weight Loss'
    }.get(goal, 'Weight Loss')
    
    if body_type in WORKOUT_PLANS:
        if goal_key in WORKOUT_PLANS[body_type]:
            return WORKOUT_PLANS[body_type][goal_key]
    
    return WORKOUT_PLANS['Mesomorph']['Weight Loss']

def get_all_plans():
    """Get all available plans."""
    return WORKOUT_PLANS