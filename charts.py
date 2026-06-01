import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import os

os.makedirs('output', exist_ok=True)

def plot_macros_pie(nutrition, name):
    """Pie chart of macros."""
    print("Creating macro pie chart...")
    labels = ['Protein', 'Carbs', 'Fats']
    values = [
        nutrition['protein'] * 4,
        nutrition['carbs'] * 4,
        nutrition['fats'] * 9
    ]
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1']
    explode = (0.05, 0.05, 0.05)

    fig, ax = plt.subplots(figsize=(8, 8))
    wedges, texts, autotexts = ax.pie(
        values,
        labels=labels,
        colors=colors,
        explode=explode,
        autopct='%1.1f%%',
        startangle=90,
        textprops={'fontsize': 14}
    )
    ax.set_title(
        f'{name} — Daily Macro Split\n'
        f'Total: {nutrition["calories"]} kcal',
        fontsize=16, fontweight='bold', pad=20)
    plt.savefig('output/macro_pie.png',
                dpi=150, bbox_inches='tight')
    plt.close()
    print("Saved macro_pie.png ✅")

def plot_bmi_gauge(bmi_data, name):
    """BMI gauge chart."""
    print("Creating BMI gauge chart...")
    fig, ax = plt.subplots(figsize=(10, 6))
    categories = [
        'Underweight', 'Normal',
        'Overweight', 'Obese']
    ranges = [18.5, 24.9, 29.9, 40]
    colors = ['#3498DB', '#2ECC71',
              '#F39C12', '#E74C3C']
    starts = [10, 18.5, 25, 30]
    widths = [8.5, 6.4, 5, 10]

    for i in range(4):
        ax.barh(0, widths[i], left=starts[i],
                color=colors[i], height=0.5,
                alpha=0.7)
        ax.text(starts[i] + widths[i]/2, 0,
                categories[i],
                ha='center', va='center',
                fontsize=10, fontweight='bold')

    ax.axvline(x=bmi_data['bmi'],
               color='black', linewidth=3,
               linestyle='--')
    ax.text(bmi_data['bmi'],
            0.35,
            f"Your BMI\n{bmi_data['bmi']}",
            ha='center', fontsize=12,
            fontweight='bold')

    ax.set_xlim(10, 40)
    ax.set_ylim(-0.5, 0.8)
    ax.set_title(
        f'{name} — BMI Analysis\n'
        f'Category: {bmi_data["category"]} '
        f'{bmi_data["emoji"]}',
        fontsize=16, fontweight='bold')
    ax.axis('off')
    plt.savefig('output/bmi_gauge.png',
                dpi=150, bbox_inches='tight')
    plt.close()
    print("Saved bmi_gauge.png ✅")

def plot_transformation(predictions, name,
                        current, goal):
    """Weight transformation prediction chart."""
    print("Creating transformation chart...")
    weeks = list(predictions.keys())
    weights = list(predictions.values())

    fig, ax = plt.subplots(figsize=(12, 6))
    
    ax.plot(weeks, weights,
            color='#E74C3C', linewidth=3,
            marker='o', markersize=10,
            markerfacecolor='white',
            markeredgewidth=2.5,
            label='Predicted Weight')
    
    ax.axhline(y=goal, color='#2ECC71',
               linewidth=2.5, linestyle='--',
               label=f'Goal: {goal}kg')
    ax.axhline(y=current, color='#3498DB',
               linewidth=2.5, linestyle='--',
               label=f'Start: {current}kg')

    for i, (week, weight) in enumerate(
            zip(weeks, weights)):
        if i % 2 == 0:
            ax.annotate(
                f'{weight}kg',
                (week, weight),
                textcoords='offset points',
                xytext=(0, 12),
                ha='center', fontsize=9,
                fontweight='bold',
                color='#E74C3C')

    ax.fill_between(weeks, weights, goal,
                    alpha=0.15, color='#E74C3C')
    
    ax.set_title(
        f'{name} — 12 Week Transformation\n'
        f'From {current}kg → {goal}kg',
        fontsize=16, fontweight='bold', pad=15)
    ax.set_xlabel('Week', fontsize=12)
    ax.set_ylabel('Weight (kg)', fontsize=12)
    ax.legend(fontsize=11, loc='upper right')
    ax.grid(True, alpha=0.3)
    
    margin = abs(current - goal) * 0.3
    ax.set_ylim(
        min(goal, min(weights)) - margin,
        max(current, max(weights)) + margin)
    
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('output/transformation.png',
                dpi=150, bbox_inches='tight')
    plt.close()
    print("Saved transformation.png ✅")
    
def plot_nutrition_bars(nutrition, name):
    """Bar chart of daily nutrition targets."""
    print("Creating nutrition bar chart...")
    items = ['Protein\n(g)', 'Carbs\n(g)',
             'Fats\n(g)', 'Fiber\n(g)']
    values = [
        nutrition['protein'],
        nutrition['carbs'],
        nutrition['fats'],
        nutrition['fiber']
    ]
    colors = ['#FF6B6B', '#4ECDC4',
              '#45B7D1', '#96CEB4']

    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.bar(items, values,
                  color=colors, width=0.5,
                  edgecolor='white',
                  linewidth=1.5)

    for bar, val in zip(bars, values):
        ax.text(
            bar.get_x() + bar.get_width()/2,
            bar.get_height() + 1,
            f'{val}g',
            ha='center', va='bottom',
            fontsize=12, fontweight='bold')

    ax.set_title(
        f'{name} — Daily Nutrition Targets\n'
        f'Calories: {nutrition["calories"]} kcal',
        fontsize=16, fontweight='bold')
    ax.set_ylabel('Grams (g)', fontsize=12)
    ax.grid(True, alpha=0.3, axis='y')
    plt.tight_layout()
    plt.savefig('output/nutrition_bars.png',
                dpi=150, bbox_inches='tight')
    plt.close()
    print("Saved nutrition_bars.png ✅")

def generate_all_charts(nutrition, bmi_data,
                        predictions, name,
                        current, goal):
    """Generate all charts."""
    print("\nGenerating all charts...")
    plot_macros_pie(nutrition, name)
    plot_bmi_gauge(bmi_data, name)
    plot_transformation(predictions, name,
                        current, goal)
    plot_nutrition_bars(nutrition, name)
    print("\nAll charts saved in output/ ✅")