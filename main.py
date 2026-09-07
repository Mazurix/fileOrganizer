from pathlib import Path
import shutil

import json

with open("config.json", "r") as file:
    config = json.load(file)
planned_moves = {}
basePath = "C:/Users/mazur/Downloads"
destination_folder = None
files = list(Path(basePath).iterdir())
for file in files:
    if file.is_file():
        file_extension = file.suffix.lower()
        for folder, extensions in config.items():
            if file_extension in extensions:
                destination_folder = Path(basePath) / folder
                destination_folder.mkdir(exist_ok=True)
                # if not (destination_folder / file.name).exists():
                #     shutil.move(str(file), str(destination_folder / file.name))
                # else:
                #     print(f"File {file.name} already exists in {destination_folder}. renmaming the file.")
                #     filename, file_extension = file.stem, file.suffix
                #     file.rename(destination_folder / f"{filename}_copy{file_extension}")
                # break

            if destination_folder is None:
                destination_folder = Path(basePath) / "Other"
                destination_folder.mkdir(exist_ok=True)
            
            counter = 1
            new_path = destination_folder / file.name
            while (new_path).exists():
                if not file.exists():
                    continue
                filename, file_extension = file.stem, file.suffix
                new_filename = f"{filename}_copy{counter}{file_extension}"
                new_path = destination_folder / new_filename
                counter += 1
            planned_moves[file] = new_path
            

print("Planned Moves:")
for source, destination in planned_moves.items():
    print(f"{source} -> {destination}")
confirmation = input("Do you want to proceed with the moves? (y/n): ")
if confirmation.lower() == 'y' or confirmation.lower() == 'yes':
    for source, destination in planned_moves.items():
        shutil.move(str(source), str(destination))
    print("Files moved successfully.")