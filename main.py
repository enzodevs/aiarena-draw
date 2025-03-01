from openai import OpenAI
import os
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

# Client
api_key = os.environ.get("DEEPSEEK_API_KEY")
client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")

# Load CSV
print("Loading CSV file...")
try:
    df = pd.read_csv('followers/data.csv')
    print("CSV file loaded successfully.")
except FileNotFoundError:
    print("Error: The file 'followers/data.csv' was not found.")
    exit()

# Extract usernames
usernames = df['username'].tolist()
print(f"Usernames extracted successfully")

# System Prompt
system_prompt = """You are an assistant who only chooses a single random winner from a list of usernames.
Once you've chosen, give a brief justification for your choice. The justification should be funny and creative.
Just choose whatever comes to mind from the extensive number of possibilities."""

# User Prompt
prompt = f"Choose a random winner from the following usernames: {usernames}"

# API Call
response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": prompt}
    ],
    max_tokens=64,
    temperature=1.5,
    stream=False
)

# Output
vencedor = response.choices[0].message.content
print(f"The winner is: {vencedor}")