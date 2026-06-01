def detect_body_type(weight, height_cm, wrist_cm, gender):
    """Detect body type from measurements."""
    height_m = height_cm / 100
    bmi = weight / (height_m ** 2)

    if gender == 'male':
        if wrist_cm < 16:
            frame = 'small'
        elif wrist_cm <= 18:
            frame = 'medium'
        else:
            frame = 'large'
    else:
        if wrist_cm < 14:
            frame = 'small'
        elif wrist_cm <= 16:
            frame = 'medium'
        else:
            frame = 'large'

    if bmi < 18.5 or (bmi < 22 and frame == 'small'):
        body_type = 'Ectomorph'
    elif bmi < 25 or frame == 'medium':
        body_type = 'Mesomorph'
    else:
        body_type = 'Endomorph'

    return body_type

def get_body_type_info(body_type):
    """Get description for each body type."""
    info = {
        'Ectomorph': {
            'emoji': '🔵',
            'description': 'Lean and slender build',
            'metabolism': 'Fast metabolism',
            'tendency': 'Hard to gain weight',
            'strength': 'Naturally lean physique',
            'challenge': 'Building muscle mass',
            'tip': 'Eat more calories and carbs. '
                   'Focus on strength training. '
                   'Never skip meals! 💪'
        },
        'Mesomorph': {
            'emoji': '🟢',
            'description': 'Athletic and muscular build',
            'metabolism': 'Medium metabolism',
            'tendency': 'Gains and loses weight easily',
            'strength': 'Responds well to exercise',
            'challenge': 'Maintaining consistency',
            'tip': 'Balanced diet works best. '
                   'Mix cardio and strength training. '
                   'You have the best genetics! 🌟'
        },
        'Endomorph': {
            'emoji': '🔴',
            'description': 'Bigger and rounder build',
            'metabolism': 'Slow metabolism',
            'tendency': 'Gains weight easily',
            'strength': 'High natural strength',
            'challenge': 'Losing body fat',
            'tip': 'Focus on cardio and low carbs. '
                   'Eat high protein meals. '
                   'Small consistent steps win! 🔥'
        }
    }
    return info[body_type]

def full_body_type_analysis(weight, height_cm,
                             wrist_cm, gender):
    """Complete body type analysis."""
    body_type = detect_body_type(
        weight, height_cm, wrist_cm, gender)
    info = get_body_type_info(body_type)
    return {
        'body_type': body_type,
        'emoji': info['emoji'],
        'description': info['description'],
        'metabolism': info['metabolism'],
        'tendency': info['tendency'],
        'strength': info['strength'],
        'challenge': info['challenge'],
        'tip': info['tip']
    }