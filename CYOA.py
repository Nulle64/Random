from openai import OpenAI


# LM Studio connection start

client = OpenAI(base_url="fill in your own ip for lm studio here", api_key="not-needed")
MODEL_NAME = "google/gemma-3n-e4b"  

# Player state

progress = "start"
dragon_defeated = False


# AI query function

def query_ai(prompt):
    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[{"role": "user", "content": prompt}],
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print("AI connection error:", e)
        return "The AI is not responding."


# Clean AI output

def clean_ai_output(text):
    """
    Remove Markdown code block markers if present.
    """
    if text.startswith("```") and text.endswith("```"):
        lines = text.splitlines()
        return "\n".join(lines[1:-1])
    return text


# Main game loop

def main():
    global progress, dragon_defeated

    print("You spawned in Minecraft! Your goal is to defeat the Ender Dragon.\n")

    while not dragon_defeated:
        # Step 1: Ask AI for 3 options
        prompt_options = f"""
You are the game master of a Minecraft RPG.
Current progress: {progress}
Give the player 3 meaningful actions they can take.
Return as plain text only.
Do NOT return JSON, code blocks, or structured formatting.
One action per line no JSON!!!!!!.
"""
        options_text = clean_ai_output(query_ai(prompt_options))
        options = [line.strip() for line in options_text.splitlines() if line.strip()]
        if len(options) < 3:
            options = ["Explore the cave", "Gather wood", "Build a shelter"]
        options = options[:3]

        print("\nChoose an action:")
        for i, opt in enumerate(options, 1):
            print(f"{i}. {opt}")

        choice = input("> ")
        try:
            action = options[int(choice) - 1]
        except Exception:
            action = options[0]

        # Step 2: Ask AI what happens next
        prompt_result = f"""
Player chose: {action}
Current progress: {progress}
Describe what happens next in Minecraft.
Return as plain text only.
Do NOT return JSON, code blocks, or structured formatting no JSON!!!!.
"""
        result_text = clean_ai_output(query_ai(prompt_result))
        print("\n" + result_text)

        # Step 3: Update state
        progress = action
        if "ender dragon" in result_text.lower() and ("defeat" in result_text.lower() or "killed" in result_text.lower()):
            dragon_defeated = True

    print("\nYou defeated the Ender Dragon! You just wasted a few hours of your life go play real Minecraft.")


# Run the game

if __name__ == "__main__":
    main()

