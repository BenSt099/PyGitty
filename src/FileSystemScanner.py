import os

# generated using ChatGPT
def get_files_with_path(path):
    result = {}
    for root, dirs, files in os.walk(path):
        if ".git" in dirs:
            dirs.remove(".git")  # exclude the '.git' directory
        if ".pygitty" in dirs:
            dirs.remove(".pygitty") # exclude the '.pygitty' directory
        for file in files:
            file_path = os.path.join(root, file)
            result[file] = file_path
    return result