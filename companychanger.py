import os


def update_org_in_files(folder_path, old_text, new_text):
    for subdir, dirs, files in os.walk(folder_path):
        for file_name in files:
            file_path = os.path.join(subdir, file_name)
            # Only work with .vcf files
            if file_name.endswith(".vcf"):
                with open(file_path, 'r', encoding='utf-8') as file:
                    file_content = file.read()

                # Find the index where the problematic part of the text occurs
                role_start = file_content.find("ROLE;")
                org_line = f"ORG;CHARSET=utf-8:{new_text}\n"

                if role_start != -1:
                    # Replace the old ROLE line with the new one
                    updated_content = file_content[:role_start] + org_line + file_content[role_start + len(old_text):]

                    # Write the updated content to the file
                    with open(file_path, 'w', encoding='utf-8') as file:
                        file.write(updated_content)

                    # Check for the existence of a backup file before attempting to rename it
                    backup_path = file_path + ".bak"
                    if os.path.exists(backup_path):
                        os.rename(backup_path, backup_path.replace(old_text, new_text))


if __name__ == "__main__":
    folder_path = input("Enter the path to the folder with .vcf files: ")
    old_text = "ROLE;CHARSET=utf-8:"
    new_text = "Your Company Name"

    update_org_in_files(folder_path, old_text, new_text)

    print("Completed! Text has been replaced in all .vcf files.")
