import os
import random
import string
from pathlib import Path

# ==== CONFIG ====
OUTPUT_DIR = "random_repo_content-latest"
NUM_FILES = 25
FILE_SIZE_MB = 1

# Random nesting depth
MIN_DEPTH = 1
MAX_DEPTH = 5

# File extensions
EXTENSIONS = [
    ".txt", ".json", ".xml", ".csv", ".log",
    ".md", ".yaml", ".yml", ".js", ".py",
    ".java", ".html", ".css", ".sql", ".conf"
]

FILE_SIZE_BYTES = FILE_SIZE_MB * 1024 * 1024

# Create base directory
Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)


def random_name(min_len=5, max_len=15):
    length = random.randint(min_len, max_len)
    chars = string.ascii_lowercase + string.digits
    return ''.join(random.choices(chars, k=length))


def random_string(length=200):
    chars = string.ascii_letters + string.digits + " \n"
    return ''.join(random.choices(chars, k=length))


def create_random_file(file_path, target_size):
    with open(file_path, "w", encoding="utf-8") as f:
        written = 0

        while written < target_size:
            line = random_string() + "\n"
            f.write(line)
            written += len(line.encode("utf-8"))


print(f"Creating {NUM_FILES} random files...")

created_paths = set()

for _ in range(NUM_FILES):

    # Random folder depth
    depth = random.randint(MIN_DEPTH, MAX_DEPTH)

    # Random nested folders
    folders = [random_name() for _ in range(depth)]

    # Random file name
    file_name = random_name() + random.choice(EXTENSIONS)

    # Full directory path
    dir_path = os.path.join(OUTPUT_DIR, *folders)

    # Create directories
    Path(dir_path).mkdir(parents=True, exist_ok=True)

    # Full file path
    file_path = os.path.join(dir_path, file_name)

    # Avoid duplicates
    while file_path in created_paths:
        file_name = random_name() + random.choice(EXTENSIONS)
        file_path = os.path.join(dir_path, file_name)

    created_paths.add(file_path)

    # Create file
    create_random_file(file_path, FILE_SIZE_BYTES)

    print(f"Created: {file_path}")

print("\nDone.")
print(f"Generated {NUM_FILES} files of ~{FILE_SIZE_MB}MB each in '{OUTPUT_DIR}'")