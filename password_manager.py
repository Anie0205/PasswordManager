import os
import json
from cryptography.fernet import Fernet
from flask import Flask, request, render_template, redirect, url_for

# Constants
FILE_PATH = "passwords.json"
KEY_FILE = "key.key"

# Flask App
app = Flask(__name__)

# Generate or load encryption key
def load_or_create_key():
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as key_file:
            key_file.write(key)
    else:
        with open(KEY_FILE, "rb") as key_file:
            key = key_file.read()
    return Fernet(key)

def load_passwords():
    if not os.path.exists(FILE_PATH):
        return {}
    with open(FILE_PATH, "rb") as file:
        encrypted_data = file.read()
    if not encrypted_data:
        return {}
    decrypted_data = cipher.decrypt(encrypted_data).decode()
    return json.loads(decrypted_data)

def save_passwords(passwords):
    encrypted_data = cipher.encrypt(json.dumps(passwords).encode())
    with open(FILE_PATH, "wb") as file:
        file.write(encrypted_data)

@app.route('/')
def home():
    passwords = load_passwords()
    return render_template("index.html", passwords=passwords)

@app.route('/add', methods=['POST'])
def add_password():
    site = request.form['site']
    password = request.form['password']
    passwords = load_passwords()
    passwords[site] = password
    save_passwords(passwords)
    return redirect(url_for('home'))

@app.route('/delete/<site>')
def delete_password(site):
    passwords = load_passwords()
    if site in passwords:
        del passwords[site]
        save_passwords(passwords)
    return redirect(url_for('home'))

if __name__ == "__main__":
    cipher = load_or_create_key()
    app.run(debug=True)