import os      # This is like telling Python: "I need the keys to open folders."
import shutil  # This is like telling Python: "I need a copy-paste machine."
import hashlib # The "Digital Scale" tool
print("Detective Tool Started...")

os.mkdir("Evidence_Folder")

source_folder = "C:\\Windows\\Prefetch"

shutil.copytree(source_folder, "Evidence_Folder\\Prefetch_Data")

browser_file = "C:\\Users\\Amit\\AppData\\Local\\Microsoft\\Edge\\User Data\\Default\\History"
shutil.copy(browser_file, "Evidence_Folder")

copied_history_path = "Evidence_Folder\\History"

# Open the file in "rb" (Read Binary) mode to weigh the 1s and 0s
with open(copied_history_path, "rb") as f:
    file_data = f.read()
    # Calculate the SHA-256 Fingerprint
    history_hash = hashlib.sha256(file_data).hexdigest()

# --- NEW: THE REPORTING LOGIC (The Receipt) ---

# Create a new text file inside the folder
report = open("Evidence_Folder\\evidence_report.txt", "w")

# Write the information into the file
report.write("FORENSIC EVIDENCE REPORT\n")
report.write("------------------------\n")
report.write("File Name: History\n")
report.write("Digital Fingerprint (SHA-256): " + history_hash + "\n")

# Close the file to save it
report.close()

print("Extraction Complete! Clues are in the Evidence Folder.")
