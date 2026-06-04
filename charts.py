import streamlit as st
import os

os.makedirs('output', exist_ok=True)

def generate_all_charts(nutrition, bmi_data,
                        predictions, name,
                        current, goal):
    """Generate charts using Streamlit."""
    print("Generating charts...")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📊 Daily Macros")
        macro_data = {
            'Protein': nutrition['protein'] * 4,
            'Carbs': nutrition['carbs'] * 4,
            'Fats': nutrition['fats'] * 9
        }
        st.bar_chart(macro_data)
    
    with col2:
        st.subheader("📈 Transformation Timeline")
        st.line_chart(predictions)
    
    st.subheader("💪 Body Metrics")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("BMI", bmi_data['bmi'],
                  bmi_data['category'])
    with col2:
        st.metric("Body Fat %",
                  bmi_data['body_fat'])
    with col3:
        st.metric("Lean Mass kg",
                  bmi_data['lean_mass'])
    
    print("Charts generated! ✅")