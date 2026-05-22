import os
import random
import string
from pathlib import Path

# ==== CONFIG ====
OUTPUT_DIR = "random_repo_content-4"
NUM_FILES = 25
FILE_SIZE_MB = 1

# Different file extensions
EXTENSIONS = [
    ".txt", ".json", ".xml", ".csv", ".log",
    ".md", ".yaml", ".yml", ".js", ".py",
    ".java", ".html", ".css", ".sql", ".conf"
]

# Approximate size in bytes
FILE_SIZE_BYTES = FILE_SIZE_MB * 1024 * 1024

# Create output directory
Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)


def random_string(length=100):
    chars = string.ascii_letters + string.digits + " \n"
    return ''.join(random.choices(chars, k=length))


def create_random_file(file_path, target_size):
    with open(file_path, "w", encoding="utf-8") as f:
        written = 0

        while written < target_size:
            line = random_string(200) + "\n"
            f.write(line)
            written += len(line.encode("utf-8"))


print(f"Creating {NUM_FILES} random files...")

for i in range(NUM_FILES):
    ext = random.choice(EXTENSIONS)
    file_name = f"file_{i+1}{ext}"
    file_path = os.path.join(OUTPUT_DIR, file_name)

    create_random_file(file_path, FILE_SIZE_BYTES)

    print(f"Created: {file_path}")

print("\nDone.")
print(f"Generated {NUM_FILES} files of ~{FILE_SIZE_MB}MB each in '{OUTPUT_DIR}'")