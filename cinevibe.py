import google.generativeai as genai

# 1. Put your Google AI Studio API key inside the quotes
genai.configure(api_key="YOUR_API_KEY_HERE")
model = genai.GenerativeModel('gemini-1.5-flash')

# 2. Ask the user for their vibe
print("=== Welcome to CineVibe ===")
user_vibe = input("What kind of movie 'vibe' are you in the mood for? \n(e.g., 'Action', 'A funny comedy', 'Sci-fi mystery'): ")

# 3. Create the prompt
prompt = f"Recommend one great movie to watch based on this vibe: {user_vibe}. Tell me the title, the genre, and exactly why it fits this vibe."

# 4. Send it to the AI and print the answer
print("\n[ Finding the perfect movie for your vibe... ]\n")
response = model.generate_content(prompt)

print(response.text)
