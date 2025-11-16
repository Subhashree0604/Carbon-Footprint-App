def get_recommendations(transport_emission, electricity_emission, total_emission):
    suggestions = []

    # Transportation rule
    if transport_emission > 0.5 * total_emission:
        suggestions.append("Your transport emissions are high. Try public transport, carpooling, cycling, or walking more.")

    # Electricity rule
    if electricity_emission > 0.4 * total_emission:
        suggestions.append("Your electricity usage is high. Use LED lights, reduce AC usage, unplug devices, and choose energy-efficient appliances.")

    # General suggestion
    if total_emission > 3000:
        suggestions.append("Your overall carbon footprint is high. Consider reducing meat consumption and switching to renewable energy sources.")

    if len(suggestions) == 0:
        suggestions.append("Great job! Your emissions are well-balanced. Keep maintaining your eco-friendly habits.")

    return suggestions


# TEST the function:
if __name__ == "__main__":
    recs = get_recommendations(
        transport_emission=1500,
        electricity_emission=800,
        total_emission=2300
    )

    for r in recs:
        print("👉", r)
