# 💪 Personal Nutrition Calculator

A web app that gives you a completely personalized
nutrition and diet plan based on your body type,
weight and fitness goals.

## What It Does
- Detects your body type automatically
  (Ectomorph, Mesomorph, Endomorph)
- Calculates your daily calories, protein,
  carbs, fats, fiber and water intake
- Gives you a personalized Indian meal plan
- Shows BMI and body fat analysis
- Generates professional nutrition charts
- Tracks your daily progress and streaks
- Exports your plan as CSV and text file

## How to Run Locally
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py

## Tools Used
- Streamlit — web app framework
- Matplotlib — chart generation
- Pandas — data handling
- Python — core logic

## Formulas Used
- Calories  = Body weight x 24
- Protein   = Goal weight x 1.9
- Fats      = Body weight x 0.7
- Fiber     = Calories / 1000 x 14
- Carbs     = Remaining calories / 4

## Live Demo
Coming soon on Streamlit Cloud!