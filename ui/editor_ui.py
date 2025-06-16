import streamlit as st
import os
from datetime import datetime

# Paths
OUTPUT_FOLDER = "output"
LOG_FOLDER = "feedback_logs"

# Ensure directories exist
os.makedirs(OUTPUT_FOLDER, exist_ok=True)
os.makedirs(LOG_FOLDER, exist_ok=True)

# Load AI-reviewed content
def load_text(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

# Save final edited version
def save_final_version(text, filename="chapter1_final.txt"):
    with open(os.path.join(OUTPUT_FOLDER, filename), "w", encoding="utf-8") as f:
        f.write(text)

# Save edit log
def save_log(original, edited):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_filename = f"edit_log_{timestamp}.txt"
    log_path = os.path.join(LOG_FOLDER, log_filename)
    with open(log_path, "w", encoding="utf-8") as f:
        f.write("=== Original ===\n")
        f.write(original)
        f.write("\n\n=== Edited ===\n")
        f.write(edited)
    return log_filename

# Streamlit UI
st.title(" Human Editing Interface")
st.markdown("Review and improve the AI-generated chapter before saving it.")

# Load input text
file_path = os.path.join(OUTPUT_FOLDER, "ai_reviewed_chapter.txt")
if os.path.exists(file_path):
    original_text = load_text(file_path)
    edited_text = st.text_area(" Edit the content below:", original_text, height=600)

    if st.button("💾 Save Final Version"):
        save_final_version(edited_text)
        log_name = save_log(original_text, edited_text)
        st.success(f" Final version saved as `chapter1_final.txt`.")
        st.info(f"📝 Edit log saved in `feedback_logs/{log_name}`")
else:
    st.error(" AI-reviewed file not found. Please run the pipeline first.")
