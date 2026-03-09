import hashlib
import os
import time

file_to_monitor = "important_file.txt"


def calculate_hash(file_path):
    sha256 = hashlib.sha256()

    with open(file_path, "rb") as f:
        while chunk := f.read(4096):
            sha256.update(chunk)

    return sha256.hexdigest()


print("Monitoring file integrity...\n")

baseline_hash = calculate_hash(file_to_monitor)

while True:
    time.sleep(5)

    current_hash = calculate_hash(file_to_monitor)

    if baseline_hash != current_hash:
        print("⚠ ALERT: File has been modified!")

        baseline_hash = current_hash