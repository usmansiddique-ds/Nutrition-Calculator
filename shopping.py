def generate_shopping_list(meal_plan, days=7):
    """Generate shopping list from meal plan."""
    
    # Common items from meals
    items_db = {
        'Grains': {
            'Brown rice': 2,
            'Oats': 1,
            'Wheat bread': 2,
            'Roti flour': 1,
            'Quinoa': 1
        },
        'Vegetables': {
            'Spinach': 500,
            'Tomato': 1,
            'Onion': 2,
            'Cucumber': 2,
            'Broccoli': 1,
            'Carrots': 500,
            'Bell peppers': 2,
            'Mushrooms': 300
        },
        'Proteins': {
            'Chicken breast': 2,
            'Eggs': 24,
            'Paneer': 500,
            'Yogurt': 2,
            'Moong dal': 1,
            'Masoor dal': 1,
            'Fish': 1,
            'Tofu': 500
        },
        'Fruits': {
            'Banana': 7,
            'Apple': 5,
            'Orange': 5,
            'Papaya': 1,
            'Guava': 3,
            'Berries': 200
        },
        'Dairy & Oils': {
            'Milk': 2,
            'Ghee': 500,
            'Olive oil': 500,
            'Peanut butter': 300,
            'Butter': 200
        },
        'Nuts & Seeds': {
            'Almonds': 200,
            'Walnuts': 150,
            'Peanuts': 200,
            'Flaxseeds': 100,
            'Chia seeds': 100
        },
        'Spices & Condiments': {
            'Turmeric': 50,
            'Jeera': 50,
            'Ginger': 200,
            'Garlic': 100,
            'Chilli powder': 50,
            'Salt': 1,
            'Honey': 500
        }
    }
    
    # Adjust quantities based on days
    shopping_list = {}
    for category, items in items_db.items():
        shopping_list[category] = {}
        for item, qty in items.items():
            shopping_list[category][item] = qty * (days / 7)
    
    return shopping_list

def format_shopping_list(shopping_list):
    """Format shopping list for display."""
    formatted = "Shopping List\n"
    formatted += "="*40 + "\n\n"
    
    for category, items in shopping_list.items():
        formatted += f"CATEGORY: {category}\n"
        formatted += "-"*40 + "\n"
        for item, qty in items.items():
            unit = get_unit(item)
            formatted += (f"  - {item}: {qty:.0f} {unit}\n")
        formatted += "\n"
    
    return formatted

def get_unit(item):
    """Get measurement unit for item."""
    weights = [
        'rice', 'dal', 'flour', 'seeds',
        'nuts', 'oil', 'ghee', 'butter',
        'peanut', 'honey', 'turmeric',
        'jeera', 'chilli', 'salt'
    ]
    
    pieces = [
        'banana', 'apple', 'orange', 'egg',
        'onion', 'tomato', 'cucumber',
        'pepper', 'papaya', 'guava'
    ]
    
    item_lower = item.lower()
    
    for w in weights:
        if w in item_lower:
            return 'g'
    for p in pieces:
        if p in item_lower:
            return 'pcs'
    
    return 'kg'

def export_shopping_pdf(shopping_list, name):
    """Export shopping list as PDF."""
    from fpdf import FPDF
    
    pdf = FPDF()
    pdf.add_page()
    
    pdf.set_font('Helvetica', 'B', 16)
    pdf.set_text_color(34, 139, 34)
    pdf.cell(0, 15, f'Shopping List - {name}',
             align='C', new_x='LMARGIN',
             new_y='NEXT')
    pdf.ln(5)
    
    for category, items in shopping_list.items():
        pdf.set_font('Helvetica', 'B', 12)
        pdf.set_text_color(34, 139, 34)
        pdf.set_fill_color(240, 255, 240)
        pdf.cell(0, 8, f'  {category}',
                 fill=True,
                 new_x='LMARGIN',
                 new_y='NEXT')
        
        pdf.set_font('Helvetica', '', 10)
        pdf.set_text_color(60, 60, 60)
        for item, qty in items.items():
            unit = get_unit(item)
            pdf.cell(10, 7, '')
            # Remove special characters
            text = f'- {item}: {qty:.0f} {unit}'
            pdf.cell(0, 7,
                     text,
                     new_x='LMARGIN',
                     new_y='NEXT')
        pdf.ln(3)
    
    import os
    os.makedirs('data', exist_ok=True)
    filename = f'data/{name}_shopping_list.pdf'
    pdf.output(filename)
    return filename