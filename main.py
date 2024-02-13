import os
import glob


def find_files(root_directory, filename, exclude_for=None):
    # Use glob to find all build.gradle files recursively
    files = glob.glob(os.path.join(root_directory, '**', filename), recursive=True)
    result = []

    if exclude_for:
        for file in files:
            find = False
            for exclude in exclude_for:
                if exclude.lower() in file.lower():
                    find = True
                    break

            if not find:
                result.append(file)

    return result


def get_file_where_text_in_file(files, texts):
    result = []
    for file_path in files:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
            file_content = file.read()

            if len(file_content) < 1:
                continue

            for text in texts:
                if text.lower() in file_content.lower():
                    result.append(file_path)
            file.close()

    return result


def pair_file_with_code_owner(codeowner_path, files):
    result = [[]]

    with open(codeowner_path, 'r', encoding='utf-8', errors='ignore') as owner_file:
        for line in owner_file.readlines():
            if len(line.strip()) < 1:
                continue

            splits = line.split()
            if len(splits) < 1:
                continue

            module = splits[0]
            owner = splits[1]

            for file in files:
                if module in file:
                    result.append([file, owner])

        owner_file.close()

    return result


if __name__ == '__main__':
    android_project_directory = ""
    code_owner_directory = android_project_directory + "/"

    exclude = ["build"]
    kts = find_files(android_project_directory, "*.kt", exclude)
    xml = find_files(android_project_directory, "*.xml", exclude)
    files = kts + xml

    files = get_file_where_text_in_file(
        files,
        [

        ]
    )

    files = pair_file_with_code_owner(code_owner_directory, files)

    for path in files:
        if len(path)< 1:
            print(path)
            continue
        print(path[0].replace("/Users/yovi.putra/AndroidStudioProjects/", ""))

    print("\n\n")

    for path in files:
        if len(path)< 1:
            print(path)
            continue
        print(path[1].replace("/", ""))
