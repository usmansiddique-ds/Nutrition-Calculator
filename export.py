import os
from datetime import date
from fpdf import FPDF

os.makedirs('output', exist_ok=True)

class NutritionPDF(FPDF):
    def header(self):
        self.set_font('Helvetica', 'B', 20)
        self.set_text_color(34, 139, 34)
        self.cell(0, 15, 'Personal Nutrition Plan',
                  align='C', new_x='LMARGIN',
                  new_y='NEXT')
        self.set_font('Helvetica', '', 10)
        self.set_text_color(128, 128, 128)
        self.cell(0, 8,
                  f'Generated on {date.today()}',
                  align='C', new_x='LMARGIN',
                  new_y='NEXT')
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font('Helvetica', 'I', 8)
        self.set_text_color(128, 128, 128)
        self.cell(0, 10,
                  'Personal Nutrition Calculator',
                  align='C')

    def section_title(self, title):
        self.set_font('Helvetica', 'B', 14)
        self.set_text_color(255, 255, 255)
        self.set_fill_color(34, 139, 34)
        self.cell(0, 10, f'  {title}',
                  fill=True,
                  new_x='LMARGIN',
                  new_y='NEXT')
        self.ln(3)

    def info_row(self, label, value,
                 highlight=False):
        self.set_font('Helvetica', 'B', 11)
        self.set_text_color(60, 60, 60)
        if highlight:
            self.set_fill_color(240, 255, 240)
            self.cell(80, 8, f'  {label}',
                      fill=True)
            self.set_font('Helvetica', '', 11)
            self.set_text_color(34, 139, 34)
            self.cell(0, 8, str(value),
                      fill=True,
                      new_x='LMARGIN',
                      new_y='NEXT')
        else:
            self.cell(80, 8, f'  {label}')
            self.set_font('Helvetica', '', 11)
            self.set_text_color(60, 60, 60)
            self.cell(0, 8, str(value),
                      new_x='LMARGIN',
                      new_y='NEXT')
        self.ln(1)

    def meal_section(self, title, items):
        self.set_font('Helvetica', 'B', 12)
        self.set_text_color(34, 139, 34)
        self.cell(0, 8, title,
                  new_x='LMARGIN',
                  new_y='NEXT')
        self.set_font('Helvetica', '', 10)
        self.set_text_color(60, 60, 60)
        for item in items:
            clean = item.encode(
                'ascii', 'ignore').decode('ascii')
            self.cell(10, 7, '')
            self.cell(0, 7,
                      f'- {clean}',
                      new_x='LMARGIN',
                      new_y='NEXT')
        self.ln(3)


def export_pdf(name, nutrition, bmi_data,
               body_type_data, meal_plan):
    """Export complete nutrition plan as PDF."""
    pdf = NutritionPDF()
    pdf.add_page()

    pdf.section_title(f'Hello {name}!')
    pdf.ln(3)

    pdf.section_title('Body Analysis')
    pdf.info_row('BMI',
                 f"{bmi_data['bmi']} - "
                 f"{bmi_data['category']}",
                 highlight=True)
    pdf.info_row('Body Type',
                 body_type_data['body_type'],
                 highlight=True)
    pdf.info_row('Body Fat Percentage',
                 f"{bmi_data['body_fat']}%")
    pdf.info_row('Lean Muscle Mass',
                 f"{bmi_data['lean_mass']} kg")
    pdf.info_row('Ideal Weight Range',
                 f"{bmi_data['ideal_min']} kg - "
                 f"{bmi_data['ideal_max']} kg")
    pdf.ln(5)

    pdf.section_title('Daily Nutrition Targets')
    pdf.info_row('Calories',
                 f"{nutrition['calories']} kcal",
                 highlight=True)
    pdf.info_row('Protein',
                 f"{nutrition['protein']} g",
                 highlight=True)
    pdf.info_row('Carbohydrates',
                 f"{nutrition['carbs']} g",
                 highlight=True)
    pdf.info_row('Fats',
                 f"{nutrition['fats']} g")
    pdf.info_row('Fiber',
                 f"{nutrition['fiber']} g")
    pdf.info_row('Water',
                 f"{nutrition['water']} L")
    pdf.ln(5)

    pdf.section_title('Your Motivation')
    pdf.set_font('Helvetica', 'I', 11)
    pdf.set_text_color(60, 60, 60)
    msg = bmi_data['message'].encode(
        'ascii', 'ignore').decode('ascii')
    pdf.multi_cell(0, 8, f'  {msg}')
    pdf.ln(5)

    pdf.add_page()
    pdf.section_title('Your Personalized Meal Plan')
    pdf.ln(3)

    pdf.meal_section('Breakfast',
                     meal_plan['breakfast'])
    pdf.meal_section('Lunch',
                     meal_plan['lunch'])
    pdf.meal_section('Snack',
                     meal_plan['snack'])
    pdf.meal_section('Dinner',
                     meal_plan['dinner'])
    pdf.meal_section('Bedtime',
                     meal_plan['bedtime'])

    filename = f'output/{name}_nutrition_plan.pdf'
    pdf.output(filename)
    print(f'Saved {filename}')
    return filename


def export_summary_pdf(name, nutrition,
                       bmi_data, body_type_data):
    """Export quick summary as PDF."""
    pdf = NutritionPDF()
    pdf.add_page()

    pdf.section_title(f'Quick Summary - {name}')
    pdf.ln(5)

    pdf.section_title('Body Stats')
    pdf.info_row('BMI', bmi_data['bmi'],
                 highlight=True)
    pdf.info_row('Category',
                 bmi_data['category'])
    pdf.info_row('Body Type',
                 body_type_data['body_type'],
                 highlight=True)
    pdf.info_row('Body Fat',
                 f"{bmi_data['body_fat']}%")
    pdf.info_row('Lean Mass',
                 f"{bmi_data['lean_mass']} kg")
    pdf.ln(5)

    pdf.section_title('Daily Targets')
    pdf.info_row('Calories',
                 f"{nutrition['calories']} kcal",
                 highlight=True)
    pdf.info_row('Protein',
                 f"{nutrition['protein']} g",
                 highlight=True)
    pdf.info_row('Carbs',
                 f"{nutrition['carbs']} g")
    pdf.info_row('Fats',
                 f"{nutrition['fats']} g")
    pdf.info_row('Fiber',
                 f"{nutrition['fiber']} g")
    pdf.info_row('Water',
                 f"{nutrition['water']} L")
    pdf.ln(5)

    pdf.section_title('Motivation')
    pdf.set_font('Helvetica', 'I', 11)
    pdf.set_text_color(60, 60, 60)
    msg = bmi_data['message'].encode(
        'ascii', 'ignore').decode('ascii')
    pdf.multi_cell(0, 8, f'  {msg}')

    filename = f'output/{name}_summary.pdf'
    pdf.output(filename)
    print(f'Saved {filename}')
    return filename