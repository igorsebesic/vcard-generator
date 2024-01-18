import base64
import os
import requests

def split_full_name(full_name):
    # Split the full name into first name and last name
    names = full_name.split(' ')
    if len(names) > 1:
        first_name = names[0]
        last_name = ' '.join(names[1:])
    else:
        first_name = full_name
        last_name = ''
    return {'first_name': first_name, 'last_name': last_name, 'full_name': full_name}

def generate_photo_encoding(image_url):
    # Load the image from the given URL
    image_data = requests.get(image_url).content
    # Encode the image into Base64 format
    image_base64 = base64.b64encode(image_data).decode('utf-8')
    # Generate Photo Encoding for vCard
    return f"PHOTO;ENCODING=b:{image_base64}"

def generate_email_address(full_name):
    # Convert Serbian characters in email addresses
    email = full_name.lower().replace('č', 'c').replace('ć', 'c').replace('ž', 'z').replace('š', 's').replace(' ', '.') + "@example.com"
    return email

def generate_url(full_name, language):
    # Convert Serbian characters in URLs
    base_url = "https://www.example.com"
    if language == 'en':
        return f"{base_url}/en/people/{full_name.lower().replace('č', 'c').replace('ć', 'c').replace('ž', 'z').replace('š', 's').replace(' ', '-')}/"
    elif language == 'sr':
        return f"{base_url}/sr/nas-tim/{full_name.lower().replace('č', 'c').replace('ć', 'c').replace('ž', 'z').replace('š', 's').replace(' ', '-')}/"
    else:
        return None

def generate_vcard_file(data, photo_encoding, language):
    # Define the folder path based on the language
    folder_path = os.path.join(os.path.expanduser('~'), 'Desktop', 'example', language)
    os.makedirs(folder_path, exist_ok=True)

    # VCard content template
    vcard_content = f"""BEGIN:VCARD
VERSION:3.0
FN;;CHARSET=utf-8:{data['full_name']}
N;CHARSET=utf-8:{data['last_name']};{data['first_name']};; 
ADR;CHARSET=utf-8;ENCODING=QUOTED-PRINTABLE;WORK:;;Sample Street;Sample City;Sample Country;
TEL;WORK:+123 456 789
TEL;WORK:
EMAIL;CHARSET=utf-8; INTERNET:{data['email']}
TITLE;CHARSET=utf-8;ENCODING=QUOTED-PRINTABLE:{data['title']}
ROLE;CHARSET=utf-8:
ORG;CHARSET=utf-8:Example Organization
URL; WORK;CHARSET=utf-8:{data['url']}
{photo_encoding}
END:VCARD
"""

    # Create the path for the vCard file
    vcard_file_path = os.path.join(folder_path, f"{data['first_name']}_{data['last_name']}.vcf")

    # Write vCard content to the file
    with open(vcard_file_path, 'w', encoding='utf-8') as vcard_file:
        vcard_file.write(vcard_content)

if __name__ == "__main__":
    # User input for generic data
    full_name = input("Enter full name: ")
    title_sr = input("Enter title in Serbian: ")
    title_en = input("Enter title in English: ")
    image_url = input("Enter image URL: ")

    # Generate Photo Encoding
    photo_encoding = generate_photo_encoding(image_url)

    # Split full name into first name and last name
    name_data = split_full_name(full_name)

    # Generate email address
    email_address = generate_email_address(full_name)

    # Generate URL for Serbian and English languages
    url_sr = generate_url(full_name, 'sr')
    url_en = generate_url(full_name, 'en')

    # VCard data for Serbian
    vcard_data_sr = {
        'full_name': full_name,
        'first_name': name_data['first_name'],
        'last_name': name_data['last_name'],
        'email': email_address,
        'title': title_sr,
        'url': url_sr,
    }

    # VCard data for English
    vcard_data_en = {
        'full_name': full_name,
        'first_name': name_data['first_name'],
        'last_name': name_data['last_name'],
        'email': email_address,
        'title': title_en,
        'url': url_en,
    }

    # Generate vCard files for Serbian and English
    generate_vcard_file(vcard_data_sr, photo_encoding, 'sr')
    generate_vcard_file(vcard_data_en, photo_encoding, 'en')

    print("vCard files have been generated and saved.")
