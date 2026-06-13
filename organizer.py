import os
import shutil

folder_path = input("Enter folder path: ")

file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".pptx", ".xlsx"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".7z"],
    "Python": [".py"]
}

for folder in file_types:
    os.makedirs(os.path.join(folder_path, folder), exist_ok=True)

for file in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file)

    if os.path.isfile(file_path):
        extension = os.path.splitext(file)[1].lower()

        for category, extensions in file_types.items():
            if extension in extensions:
                destination = os.path.join(folder_path, category, file)

                if not os.path.exists(destination):
                    shutil.move(file_path, destination)

                print(f"Moved: {file} -> {category}")
                break

print("Organization Complete!")
