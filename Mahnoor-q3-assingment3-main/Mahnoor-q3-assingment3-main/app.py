import streamlit as st
import pandas as pd
import plotly.express as px
import random
import string

def generate_password(length=12, use_digits=True, use_specials=True, use_uppercase=True):
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_specials:
        characters += string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def check_password_strength(password):
    conditions = {
        "Length > 8": len(password) > 8,
        "Contains Uppercase": any(char.isupper() for char in password),
        "Contains Numbers": any(char.isdigit() for char in password),
        "Contains Special Characters": any(char in string.punctuation for char in password)
    }
    score = sum(conditions.values())
    strength_levels = ["Weak", "Medium", "Strong", "Very Strong"]
    strength = strength_levels[min(score, len(strength_levels) - 1)]
    return strength, conditions

st.set_page_config(page_title="Password Generator", layout="wide")
st.title("🔑 Simple Password Generator")
st.markdown("### Generate a strong password and check its strength")

length = st.slider("Select Password Length", min_value=6, max_value=32, value=12)
use_digits = st.checkbox("Include Numbers", True)
use_specials = st.checkbox("Include Special Characters", True)
use_uppercase = st.checkbox("Include Uppercase Letters", True)

generated_password = generate_password(length, use_digits, use_specials, use_uppercase)
strength, conditions = check_password_strength(generated_password)

st.subheader("Generated Password")
st.code(generated_password, language="")

st.subheader("Password Strength")
st.write(f"**Strength Level:** {strength}")

df = pd.DataFrame(list(conditions.items()), columns=["Condition", "Met"])
fig = px.bar(df, x="Condition", y="Met", color="Met", text="Met", title="Password Strength Breakdown")
st.plotly_chart(fig, use_container_width=True)

st.markdown("---")
st.markdown("### Made by **MUSSA** 🔒")