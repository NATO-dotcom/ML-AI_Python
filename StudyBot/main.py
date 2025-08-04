from app.chatbot import greet_user, ask_subject, ask_difficulty, ask_mood, ask_focus
from app.planner import recommend_plan
from app.voice_utils import speak, listen

def get_input(prompt, voice_mode=False):
    if voice_mode:
        speak(prompt)
        for attempt in range(3):  # Retry up to 3 times
            try:
                response = listen()
                if response and response.strip():
                    print(f"You said: {response}")
                    return response.strip().lower()
                else:
                    print("⚠️ Didn't catch that. Trying again...")
            except Exception as e:
                print(f"❌ Voice input error: {e}")
        # Fallback to manual text input if voice fails
        return input(f"🎤 (Voice failed) {prompt}\nYou: ").strip().lower()
    else:
        return input(prompt + "\nYou: ").strip().lower()

def main():
    voice_mode = input("🗣️ Use voice mode? (yes/no)\nYou: ").strip().lower() in ['yes', 'y']

    greeting = greet_user()
    print(greeting)
    if voice_mode:
        speak(greeting)

    confirm = get_input("Ready to plan your study session?", voice_mode)

    if confirm in ['yes', 'y']:
        subject = get_input(ask_subject(), voice_mode)

        while True:
            try:
                difficulty_input = get_input(ask_difficulty(), voice_mode)
                difficulty = int(difficulty_input)
                if 1 <= difficulty <= 5:
                    break
                else:
                    print("⚠️ Please enter a number between 1 and 5.")
            except ValueError:
                print("❌ Invalid number. Try again.")

        mood = get_input(ask_mood(), voice_mode)

        while True:
            try:
                focus_input = get_input(ask_focus(), voice_mode)
                focus = int(focus_input)
                if 1 <= focus <= 5:
                    break
                else:
                    print("⚠️ Please enter a number between 1 and 5.")
            except ValueError:
                print("❌ Invalid number. Try again.")

        plan = recommend_plan(subject, difficulty, mood, focus)
        print(plan)
        if voice_mode:
            speak(plan)

        with open("study_recommendation.txt", "w", encoding="utf-8") as file:
            file.write(plan)
    else:
        goodbye = "👍 Okay, see you next time!"
        print(goodbye)
        if voice_mode:
            speak(goodbye)

if __name__ == "__main__":
    main()
