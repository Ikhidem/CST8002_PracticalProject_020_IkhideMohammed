"""
Generates chart visualizations for emissions data.
"""
import matplotlib.pyplot as plt

def show_chart(facility_names, emissions, chart_type="bar"):
    """
    Displays a chart of emissions per facility.
    Supported types: 'bar', 'hbar', 'pie'
    """
    plt.figure(figsize=(10, 6))
    if chart_type == "bar":
        plt.bar(facility_names, emissions, color='skyblue')
        plt.ylabel("Emissions")
        plt.xlabel("Facility")
        plt.title("Top Facilities by Emissions - Vertical Bar Chart")
    elif chart_type == "hbar":
        plt.barh(facility_names, emissions, color='lightgreen')
        plt.xlabel("Emissions")
        plt.ylabel("Facility")
        plt.title("Top Facilities by Emissions - Horizontal Bar Chart")
    elif chart_type == "pie":
        plt.pie(emissions, labels=facility_names, autopct='%1.1f%%', startangle=140)
        plt.title("Top Facilities by Emissions - Pie Chart")
    else:
        print("Invalid chart type.")
        return

    plt.tight_layout()
    plt.show()