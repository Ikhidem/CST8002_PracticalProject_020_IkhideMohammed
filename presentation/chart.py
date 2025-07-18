
"""
Generates chart visualizations for emissions data.
"""
import matplotlib.pyplot as plt

def show_bar_chart(facility_names, emissions):
    """
    Displays a bar chart of emissions per facility.
    """
    plt.figure(figsize=(10, 6))
    plt.bar(facility_names, emissions, color='skyblue')
    plt.title("Top 5 Facilities by Emissions")
    plt.xlabel("Facility")
    plt.ylabel("Emissions")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
