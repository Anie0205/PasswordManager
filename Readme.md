# Password Manager

## Overview
This is a simple password manager built with Python and Flask. It securely stores passwords using encryption and provides a web-based interface for managing them.

## Features
- Add passwords for different websites
- View saved passwords
- Delete passwords when no longer needed
- Secure encryption using Fernet from the cryptography library

## Requirements
Ensure you have Python installed and then install the required dependencies:

```bash
pip install flask cryptography
```

## Project Structure
```
PasswordManager/
│── templates/
│   ├── index.html   (Frontend UI)
│── static/          (CSS & JS if needed)
│── password_manager.py  (Backend logic)
│── passwords.json  (Encrypted storage)
│── key.key  (Encryption key)
│── README.md  (Project documentation)
│── requirements.txt  (Dependencies)
```

## Running the Application
1. Clone this repository or download the files.
2. Navigate to the project directory.
3. Run the application:
   ```bash
   python password_manager.py
   ```
4. Open a web browser and go to:
   ```
   http://127.0.0.1:5000/
   ```

## Security Considerations
- The encryption key (`key.key`) is automatically generated and should not be shared.
- Do not manually edit `passwords.json`, as it is encrypted.
- Consider adding authentication to restrict access to the password manager.

## Future Enhancements
- Implement user authentication
- Improve password visibility controls
- Add support for auto-generating secure passwords

## License
This project is open-source and available under the MIT License.