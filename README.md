# Gmail Automation System

A Python-based Gmail Automation System that allows users to send emails through Gmail using SMTP.

## Features

- Send emails using Gmail SMTP
- Multiple recipients support
- CC and BCC support
- Email subject and body
- File attachments
- Basic email address validation
- Secure credential management using environment variables
- Error handling
- Email preview and sending confirmation

## Technologies Used

- Python
- SMTP
- python-dotenv
- EmailMessage

## Project Structure

Gmail-Automation/

│

├── main.py

├── email_sender.py

├── requirements.txt

├── .env.example

├── .gitignore

└── README.md

## Installation

1. Clone the repository.

   git clone https://github.com/palchhin-sharma-official/MailPilot-Python.git

2. Open the project folder.

3. Install dependencies.

   pip install -r requirements.txt

## Configuration

1. Create a `.env` file in the project directory.
2. Add your Gmail address and Gmail App Password:

   GMAIL_ADDRESS=your_email@gmail.com
   GMAIL_APP_PASSWORD=your_app_password

3. Never upload your `.env` file to GitHub.

## Usage

Run the application:

python main.py

Enter the recipient, subject, message, CC, BCC and optional attachment paths.

Review the email preview and confirm before sending.

## Security

- Credentials are stored in a local `.env` file.
- The `.env` file is excluded through `.gitignore`.
- Use a Gmail App Password where supported.
- Never share your credentials publicly.

## Author

Palchhin Sharma!
