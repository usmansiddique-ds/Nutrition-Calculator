import random

BREAKFAST_OPTIONS = {
    'Ectomorph': [
        [
            '🥣 Masala oats with banana and honey',
            '🥚 3 whole eggs scrambled with veggies',
            '🥛 Full fat milk 1 glass',
            '🥜 Handful of mixed nuts almonds cashews',
            '🍞 Peanut butter on multigrain toast'
        ],
        [
            '🍌 Banana smoothie with whey protein',
            '🥞 Besan cheela with paneer stuffing',
            '🥛 Warm milk with turmeric and honey',
            '🍠 Boiled sweet potato with ghee',
            '🥜 Soaked walnuts and almonds'
        ],
        [
            '🍚 Poha with peanuts and vegetables',
            '🥚 Egg omelette with cheese',
            '🍌 2 bananas with peanut butter',
            '🥛 Banana milkshake full fat',
            '🌾 Upma with cashews and vegetables'
        ]
    ],
    'Mesomorph': [
        [
            '🥣 Oats with mixed berries and honey',
            '🥚 2 boiled eggs',
            '🥛 Low fat milk',
            '🌻 Mixed seeds sunflower pumpkin flax',
            '🍎 1 apple or orange'
        ],
        [
            '🫓 Whole wheat toast with avocado',
            '🥚 Egg white omelette with spinach',
            '🥛 Greek yogurt with fruits',
            '🌾 Daliya with vegetables',
            '🍵 Green tea'
        ],
        [
            '🥞 Moong dal chilla with mint chutney',
            '🥚 2 boiled eggs with black pepper',
            '🍓 Mixed fruit bowl papaya mango apple',
            '🥛 Buttermilk with jeera',
            '🌰 Handful of walnuts'
        ]
    ],
    'Endomorph': [
        [
            '🥚 Vegetable omelette spinach mushroom',
            '🫓 2 besan chilla no oil',
            '🍵 Green tea with lemon',
            '🥜 4 soaked walnuts',
            '🍈 Papaya or guava slice'
        ],
        [
            '🥣 Oats with chia seeds no sugar',
            '🥚 2 egg whites scrambled',
            '🍵 Ginger lemon tea',
            '🌱 Sprouts salad with lemon',
            '🥒 Cucumber slices with hummus'
        ],
        [
            '🫓 Ragi dosa with coconut chutney',
            '🥚 Boiled eggs 2 whites 1 yolk',
            '🍵 Chamomile tea',
            '🍈 Guava with black salt',
            '🌿 Soaked methi seeds water'
        ]
    ]
}

LUNCH_OPTIONS = {
    'Ectomorph': [
        [
            '🍚 Brown rice 2 cups',
            '🫘 Dal tadka with ghee',
            '🍗 Grilled chicken 150g or Paneer 100g',
            '🫓 2 ghee rotis',
            '🥗 Cucumber tomato onion salad',
            '🥛 Curd 1 bowl'
        ],
        [
            '🍚 Jeera rice 2 cups',
            '🫘 Rajma curry',
            '🥚 2 boiled eggs or Soya chunks',
            '🫓 3 whole wheat rotis',
            '🥦 Stir fried vegetables with ghee',
            '🥛 Raita with boondi'
        ],
        [
            '🍚 Pulao with vegetables and nuts',
            '🫘 Chana masala',
            '🍗 Chicken curry or Paneer butter masala',
            '🫓 2 parathas with ghee',
            '🥗 Mixed salad',
            '🥛 Lassi sweet'
        ]
    ],
    'Mesomorph': [
        [
            '🍚 Brown rice 1.5 cups',
            '🫘 Moong dal',
            '🍗 Grilled chicken 120g or Paneer tikka',
            '🫓 2 whole wheat rotis',
            '🥗 Green salad with olive oil dressing',
            '🥛 Buttermilk'
        ],
        [
            '🌾 Quinoa vegetable bowl',
            '🫘 Dal palak',
            '🐟 Grilled fish or Tofu stir fry',
            '🫓 2 jowar rotis',
            '🥦 Steamed broccoli carrots beans',
            '🥛 Curd'
        ],
        [
            '🍚 Millet khichdi with vegetables',
            '🫘 Sambhar',
            '🥚 Egg curry or Paneer bhurji',
            '🫓 2 ragi rotis',
            '🥗 Kachumber salad',
            '🥛 Chaas with jeera'
        ]
    ],
    'Endomorph': [
        [
            '🍚 Brown rice 1 cup only',
            '🫘 Masoor dal no oil',
            '🐟 Grilled fish 100g or Boiled chicken',
            '🫓 1 whole wheat roti',
            '🥗 Big green salad lettuce spinach',
            '🥦 Steamed vegetables'
        ],
        [
            '🌾 Quinoa 1 cup',
            '🫘 Moong dal soup',
            '🥚 2 egg whites curry',
            '🫓 1 bajra roti',
            '🥦 Stir fried broccoli no oil',
            '🥛 Thin buttermilk no salt'
        ],
        [
            '🌾 Daliya khichdi',
            '🫘 Palak soup',
            '🐟 Steamed fish or Tofu',
            '🥗 Raw vegetable salad',
            '🥦 Boiled sweet corn',
            '🍵 Green tea after lunch'
        ]
    ]
}

SNACK_OPTIONS = {
    'Ectomorph': [
        [
            '🍌 Banana with peanut butter',
            '🥛 Full fat milk shake',
            '🌴 5 dates with almonds'
        ],
        [
            '🍠 Sweet potato chaat',
            '🥜 Mixed nuts and dried fruits',
            '🥛 Paneer cubes with pepper'
        ],
        [
            '🍞 Peanut butter sandwich',
            '🥛 Chocolate milk',
            '🌾 Granola bar homemade'
        ]
    ],
    'Mesomorph': [
        [
            '🍎 Apple with almond butter',
            '🫘 Roasted chana',
            '🥥 Coconut water'
        ],
        [
            '🌱 Sprouts chaat with lemon',
            '🍓 Mixed fruit bowl',
            '🥛 Buttermilk with mint'
        ],
        [
            '🥒 Vegetable sticks with hummus',
            '🥜 Handful of mixed nuts',
            '🍵 Green tea with honey'
        ]
    ],
    'Endomorph': [
        [
            '🥒 Cucumber carrot sticks',
            '🥛 Thin buttermilk no sugar',
            '🍈 1 guava'
        ],
        [
            '🍿 Roasted makhana fox nuts',
            '🍵 Green tea with lemon',
            '🌿 Soaked chia seeds water'
        ],
        [
            '🥗 Sprouts with tomato cucumber',
            '🍵 Ginger tea no sugar',
            '🥜 4 almonds 2 walnuts'
        ]
    ]
}

DINNER_OPTIONS = {
    'Ectomorph': [
        [
            '🫓 3 multigrain rotis',
            '🫘 Rajma or Chole curry',
            '🥚 Egg bhurji or Paneer',
            '🥬 Sabzi with ghee',
            '🥛 Curd 1 bowl'
        ],
        [
            '🍚 Brown rice 1.5 cups',
            '🫘 Dal makhani',
            '🍗 Chicken curry or Mushroom masala',
            '🥦 Stir fried vegetables',
            '🥛 Lassi'
        ],
        [
            '🫓 2 parathas with ghee',
            '🫘 Mixed dal',
            '🥚 Omelette 3 eggs',
            '🥗 Salad',
            '🥛 Warm milk'
        ]
    ],
    'Mesomorph': [
        [
            '🫓 2 jowar bajra rotis',
            '🫘 Dal palak',
            '🐟 Fish curry or Soya chunks',
            '🥦 Stir fried vegetables',
            '🥛 Buttermilk'
        ],
        [
            '🌾 Quinoa vegetable pulao',
            '🫘 Moong dal',
            '🥚 Egg curry or Paneer tikka',
            '🥗 Green salad',
            '🍵 Chamomile tea'
        ],
        [
            '🫓 2 ragi rotis',
            '🫘 Sambhar',
            '🍗 Grilled chicken or Tofu',
            '🥦 Steamed broccoli',
            '🥛 Curd'
        ]
    ],
    'Endomorph': [
        [
            '🫓 2 bajra rotis',
            '🥬 Palak dal no oil',
            '🧀 Grilled paneer 80g or Tofu',
            '🥦 Stir fried veggies minimal oil',
            '🍅 Clear tomato soup'
        ],
        [
            '🌾 Ragi dosa 2 pieces',
            '🫘 Moong dal soup',
            '🥚 Boiled eggs 2',
            '🥗 Raw salad',
            '🍵 Green tea'
        ],
        [
            '🫓 1 whole wheat roti',
            '🫘 Masoor dal soup',
            '🐟 Steamed fish',
            '🥦 Boiled vegetables',
            '🥛 Thin buttermilk'
        ]
    ]
}

BEDTIME_OPTIONS = {
    'Ectomorph': [
        ['🥛 Warm turmeric milk', '🍌 1 banana',
         '🥜 Handful of cashews'],
        ['🥛 Chocolate milk', '🌴 3 dates',
         '🥜 Peanut butter 1 spoon'],
        ['🥛 Warm milk with honey',
         '🌰 6 soaked almonds',
         '🍞 1 slice bread']
    ],
    'Mesomorph': [
        ['🥛 Warm milk', '🌰 6 soaked almonds',
         '🌱 1 tsp flaxseeds'],
        ['🥛 Low fat milk with turmeric',
         '🥜 4 walnuts', '🍵 Chamomile tea'],
        ['🥛 Buttermilk with jeera',
         '🌰 5 almonds', '🍎 Small apple']
    ],
    'Endomorph': [
        ['🍵 Chamomile tea no sugar',
         '🌱 Chia seeds soaked',
         '🌰 4 almonds only'],
        ['🍵 Ginger lemon tea',
         '🥒 Cucumber slices',
         '🌿 Tulsi tea'],
        ['🍵 Green tea',
         '🌰 3 walnuts',
         '🥛 Very thin buttermilk']
    ]
}

def get_meal_plan(body_type, goal):
    """Get random varied meal plan."""
    idx = random.randint(0, 2)
    return {
        'breakfast': BREAKFAST_OPTIONS[body_type][idx],
        'lunch': LUNCH_OPTIONS[body_type][idx],
        'snack': SNACK_OPTIONS[body_type][idx],
        'dinner': DINNER_OPTIONS[body_type][idx],
        'bedtime': BEDTIME_OPTIONS[body_type][idx]
    }

def get_water_timing():
    """Get water drinking schedule."""
    return [
        '⏰ 6:00 AM  — Warm water with lemon',
        '⏰ 7:00 AM  — Breakfast',
        '⏰ 10:00 AM — Morning snack',
        '⏰ 1:00 PM  — Lunch',
        '⏰ 4:00 PM  — Evening snack',
        '⏰ 7:00 PM  — Dinner',
        '⏰ 9:30 PM  — Bedtime snack',
        '⏰ All day  — 2.5 to 3L water'
    ]

def get_superfoods(body_type):
    """Get recommended superfoods."""
    common = [
        'Turmeric — powerful anti inflammation',
        'Ginger — boosts metabolism naturally',
        'Amla — highest vitamin C source',
        'Jeera — improves digestion',
        'Ashwagandha — reduces stress hormones'
    ]
    specific = {
        'Ectomorph': [
            'Banana — instant natural energy',
            'Peanut butter — healthy fats protein',
            'Sweet potato — complex slow carbs',
            'Whole milk — protein calcium fat',
            'Dates — natural sugar energy'
        ],
        'Mesomorph': [
            'Berries — powerful antioxidants',
            'Greek yogurt — high protein probiotic',
            'Quinoa — complete protein source',
            'Coconut water — natural electrolytes',
            'Sprouts — living food enzymes'
        ],
        'Endomorph': [
            'Green tea — natural fat burner',
            'Chia seeds — fiber omega 3',
            'Makhana — low calorie high protein',
            'Apple cider vinegar — metabolism boost',
            'Moringa — nutrient dense superfood'
        ]
    }
    return common + specific[body_type]

def get_foods_to_avoid(body_type):
    """Foods to avoid based on body type."""
    common = [
        '❌ Sugary drinks and sodas',
        '❌ Processed packaged foods',
        '❌ Deep fried foods',
        '❌ White bread maida products',
        '❌ Alcohol'
    ]
    specific = {
        'Ectomorph': [
            '⚠️ Avoid skipping meals',
            '⚠️ Avoid too much cardio',
            '⚠️ Avoid very low calorie diets'
        ],
        'Mesomorph': [
            '⚠️ Avoid inconsistent eating',
            '⚠️ Avoid excess sugar',
            '⚠️ Avoid late night heavy meals'
        ],
        'Endomorph': [
            '⚠️ Avoid white rice in excess',
            '⚠️ Avoid high sugar fruits at night',
            '⚠️ Avoid eating after 8 PM'
        ]
    }
    return common + specific[body_type]