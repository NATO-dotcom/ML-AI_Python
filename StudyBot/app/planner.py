def recommend_plan(subject, difficulty, mood, focus):
    plan = f"\n✅ Got it! Based on your input:\n"
    plan += f"- Subject: {subject}\n"
    plan += f"- Difficulty: {difficulty}\n"
    plan += f"- Mood: {mood}\n"
    plan += f"- Focus Level: {focus}\n\n"

    if mood.lower() == "tired" or focus <= 2:
        minutes = 25
        method = "passive methods (watch a video, review notes)"
    elif difficulty >= 4 and focus >= 3:
        minutes = 45
        method = "active recall or practice problems"
    else:
        minutes = 35
        method = "mixed methods (read + flashcards)"

    plan += f"📘 Recommendation: Study for {minutes} minutes using {method}.\n"
    plan += "📅 I suggest reviewing this again tomorrow.\n"
    return plan
