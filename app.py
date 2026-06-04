import streamlit as st
from calculator import calculate_nutrition, calculate_bmr, calculate_tdee, predict_transformation
from bmi import full_bmi_analysis
from body_type import full_body_type_analysis
from meal_plan import get_meal_plan, get_water_timing, get_superfoods
from charts import generate_all_charts
from tracker import save_entry, get_streak, get_achievements
from export import export_pdf, export_summary_pdf
st.set_page_config(
    page_title="Nutrition Calculator",
    page_icon="💪",
    layout="wide"
)

st.title("💪 Personal Nutrition Calculator")
st.subheader("Your personalized health and diet plan")

with st.sidebar:
    st.header("Enter Your Details")
    name = st.text_input("Full Name", "")
    age = st.number_input("Age", 10, 100, 21)
    gender = st.selectbox(
        "Gender", ["male", "female"])
    current_weight = st.number_input(
        "Current Weight (kg)", 30.0, 200.0, 75.0)
    goal_weight = st.number_input(
        "Goal Weight (kg)", 30.0, 200.0, 70.0)
    height = st.number_input(
        "Height (cm)", 100.0, 250.0, 175.0)
    wrist = st.number_input(
        "Wrist Size (cm)", 10.0, 30.0, 17.0)
    activity = st.selectbox(
        "Activity Level", [
            "sedentary",
            "light",
            "moderate",
            "active",
            "very_active"
        ])
    goal = st.selectbox(
        "Your Goal", [
            "Weight Loss",
            "Weight Gain",
            "Muscle Building",
            "Maintenance"
        ])
    calculate = st.button(
        "Calculate My Plan 🚀",
        use_container_width=True)

if calculate and name:
    st.success(f"Welcome {name}! Here is your personalized plan!")

    nutrition = calculate_nutrition(
        current_weight, goal_weight)
    bmi_data = full_bmi_analysis(
        current_weight, height, age, gender)
    body_type_data = full_body_type_analysis(
        current_weight, height, wrist, gender)
    bmr = calculate_bmr(
        current_weight, height, age, gender)
    tdee = calculate_tdee(bmr, activity)
    predictions = predict_transformation(
        current_weight, goal_weight,
        nutrition['calories'])
    meal_plan = get_meal_plan(
        body_type_data['body_type'], goal)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("BMI", bmi_data['bmi'],
                  bmi_data['category'])
    with col2:
        st.metric("Body Type",
                  body_type_data['body_type'],
                  body_type_data['emoji'])
    with col3:
        st.metric("Daily Calories",
                  f"{nutrition['calories']} kcal")

    st.info(f"💬 {bmi_data['message']}")
    st.info(f"💡 {body_type_data['tip']}")

    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📊 Nutrition",
        "🍽️ Meal Plan",
        "📈 Charts",
        "🏆 Progress",
        "💾 Export"
    ])

    with tab1:
        st.header("Your Daily Nutrition Targets")
        c1, c2, c3 = st.columns(3)
        with c1:
            st.metric("Calories",
                      f"{nutrition['calories']} kcal")
            st.metric("Protein",
                      f"{nutrition['protein']}g")
        with c2:
            st.metric("Carbs",
                      f"{nutrition['carbs']}g")
            st.metric("Fats",
                      f"{nutrition['fats']}g")
        with c3:
            st.metric("Fiber",
                      f"{nutrition['fiber']}g")
            st.metric("Water",
                      f"{nutrition['water']}L")

        st.subheader("Body Analysis")
        c1, c2 = st.columns(2)
        with c1:
            st.write(f"**BMR:** {bmr} kcal")
            st.write(f"**TDEE:** {tdee} kcal")
            st.write(f"**Body Fat:** "
                     f"{bmi_data['body_fat']}%")
        with c2:
            st.write(f"**Lean Mass:** "
                     f"{bmi_data['lean_mass']}kg")
            st.write(f"**Ideal Weight:** "
                     f"{bmi_data['ideal_min']} - "
                     f"{bmi_data['ideal_max']}kg")
            st.write(f"**Metabolism:** "
                     f"{body_type_data['metabolism']}")

    with tab2:
        st.header(f"Your Meal Plan")
        st.subheader(
            f"Body Type: {body_type_data['body_type']} "
            f"{body_type_data['emoji']}")

        st.info("🔄 Click Calculate again for a different meal variation!")

        col1, col2 = st.columns(2)
        with col1:
            st.subheader("🌅 Breakfast")
            for item in meal_plan['breakfast']:
                st.write(f"{item}")
            st.divider()
            st.subheader("🌞 Lunch")
            for item in meal_plan['lunch']:
                st.write(f"{item}")
            st.divider()
            st.subheader("🍎 Snack")
            for item in meal_plan['snack']:
                st.write(f"{item}")
        with col2:
            st.subheader("🌆 Dinner")
            for item in meal_plan['dinner']:
                st.write(f"{item}")
            st.divider()
            st.subheader("🌙 Bedtime")
            for item in meal_plan['bedtime']:
                st.write(f"{item}")
            st.divider()
            st.subheader("💧 Water Schedule")
            for item in get_water_timing():
                st.write(item)

        st.divider()
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("🌿 Superfoods For You")
            for food in get_superfoods(
                    body_type_data['body_type']):
                st.write(f"✅ {food}")
        with col2:
            st.subheader("🚫 Foods to Avoid")
            from meal_plan import get_foods_to_avoid
            for food in get_foods_to_avoid(
                    body_type_data['body_type']):
                st.write(food)
    with tab3:
        st.header("Your Charts")
        generate_all_charts(
            nutrition, bmi_data,
            predictions, name,
            current_weight, goal_weight)
    with tab4:
        st.header("Progress Tracker")
        save_entry(name, current_weight,
                   nutrition, bmi_data)
        streak = get_streak(name)
        achievements = get_achievements(streak)
        st.metric("Current Streak",
                  f"{streak} days")
        st.subheader("Transformation Prediction")
        for week, weight in predictions.items():
            st.write(f"**{week}:** {weight}kg")
        st.subheader("Your Achievements")
        if achievements:
            for a in achievements:
                st.success(a)
        else:
            st.info("Keep going! Achievements "
                    "unlock as you progress!")

    with tab5:
        st.header("Export Your Plan")
        st.write("Download your complete "
                 "nutrition plan as PDF!")

        from export import (export_pdf,
                            export_summary_pdf)

        pdf_file = export_pdf(
            name, nutrition, bmi_data,
            body_type_data, meal_plan)

        summary_file = export_summary_pdf(
            name, nutrition, bmi_data,
            body_type_data)

        col1, col2 = st.columns(2)
        with col1:
            with open(pdf_file, 'rb') as f:
                st.download_button(
                    label="📄 Download Full Plan PDF",
                    data=f,
                    file_name=f"{name}_nutrition_plan.pdf",
                    mime='application/pdf',
                    use_container_width=True)
            st.caption("Includes body analysis, "
                       "nutrition targets "
                       "and full meal plan")

        with col2:
            with open(summary_file, 'rb') as f:
                st.download_button(
                    label="📋 Download Summary PDF",
                    data=f,
                    file_name=f"{name}_summary.pdf",
                    mime='application/pdf',
                    use_container_width=True)
            st.caption("Quick reference card "
                       "with daily targets")