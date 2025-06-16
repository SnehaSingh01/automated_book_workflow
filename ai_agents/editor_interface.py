import os
from datetime import datetime

def human_review(text, enable_logging=True):
    """
    Simulates a human-in-the-loop editor interface.
    
    Parameters:
        text (str): The AI-generated content to review.
        enable_logging (bool): If True, saves the AI and human-edited text to a log file.
    
    Returns:
        str: Final edited version, or original text if no edits are made.
    """
    print("\n==================== AI Output ====================\n")
    print(text)
    print("\n=============== Begin Manual Edits ===============")
    print("Type your edited text line by line.")
    print("When you're done, press Enter on an empty line to finish.\n")

    edited_lines = []
    try:
        while True:
            line = input()
            if line == "":
                break
            edited_lines.append(line)
    except EOFError:
        print("\n[Input ended unexpectedly. Proceeding with current edits...]")

    final_text = "\n".join(edited_lines).strip()

    if not final_text:
        print("\n[No edits provided. Using the original AI output.]\n")
        final_text = text
    else:
        print("\n[Human edits captured. Proceeding with updated text.]\n")

    
    if enable_logging:
        save_feedback_log(text, final_text)

    return final_text

def save_feedback_log(original, edited):
    """
    Saves the AI-generated and human-edited text to a timestamped log file.
    """
    os.makedirs("output/feedback_logs", exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"output/feedback_logs/edit_log_{timestamp}.txt"

    with open(filename, "w", encoding="utf-8") as log:
        log.write("=== AI Output ===\n")
        log.write(original + "\n\n")
        log.write("=== Human Feedback ===\n")
        log.write(edited + "\n")

    print(f"[Edit log saved: {filename}]")

