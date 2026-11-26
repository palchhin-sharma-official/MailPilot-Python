
# WHY: Connect to Gmail's SMTP server.
import smtplib

# WHY: Work with environment variables and file paths.
import os

# WHY: Identify attachment file types.
import mimetypes

# WHY: Validate basic email address formats.
import re

# WHY: Load credentials from the .env file.
from dotenv import load_dotenv

# WHY: Create structured email messages.
from email.message import EmailMessage


# WHY: Load credentials stored in the .env file.
load_dotenv()

# WHY: Read Gmail credentials without hardcoding sensitive information.
GMAIL_ADDRESS = os.getenv("GMAIL_ADDRESS")
GMAIL_APP_PASSWORD = os.getenv("GMAIL_APP_PASSWORD")


# WHY: Check whether an email address has a basic valid format.
def validate_email(email):

    # WHY: Define a pattern for basic email format validation.
    pattern = r"^[\w.+-]+@[\w-]+\.[\w.-]+$"

    # WHY: Return True if the email matches the pattern; otherwise, False.
    return re.match(pattern, email) is not None


# WHY: Send an email with optional CC, BCC, and attachments.
def send_email(recipient, subject, body, cc=None, bcc=None, attachments=None):

    # WHY: Check whether Gmail credentials are available.
    if not GMAIL_ADDRESS or not GMAIL_APP_PASSWORD:
        raise ValueError("Gmail credentials are missing from the .env file.")

    # WHY: Convert optional values into empty lists.
    cc = cc or []
    bcc = bcc or []
    attachments = attachments or []

    # WHY: Combine all recipient addresses for validation.
    all_recipients = [recipient] + cc + bcc

    # WHY: Validate every recipient email address.
    for address in all_recipients:
        if not validate_email(address):
            raise ValueError(f"Invalid email address: {address}")

    # WHY: Create an email object to store message details.
    message = EmailMessage()

    # WHY: Set the sender, recipient, and subject.
    message["From"] = GMAIL_ADDRESS
    message["To"] = recipient
    message["Subject"] = subject

    # WHY: Add CC recipients to the visible email headers.
    if cc:
        message["Cc"] = ", ".join(cc)

    # WHY: Add the main email body.
    message.set_content(body)

    # WHY: Process every file provided as an attachment.
    for file_path in attachments:

        # WHY: Check whether the attachment file exists.
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"Attachment not found: {file_path}")

        # WHY: Detect the file's MIME type.
        mime_type, _ = mimetypes.guess_type(file_path)

        # WHY: Set the correct content type for the attachment.
        if mime_type:
            maintype, subtype = mime_type.split("/", 1)
        else:
            maintype, subtype = "application", "octet-stream"

        # WHY: Read the file in binary mode.
        with open(file_path, "rb") as file:
            message.add_attachment(
                file.read(),
                maintype=maintype,
                subtype=subtype,
                filename=os.path.basename(file_path)
            )

    # WHY: Include To, CC, and BCC addresses in the delivery list.
    recipients = all_recipients

    # WHY: Establish a secure SSL connection with Gmail's SMTP server.
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:

        # WHY: Authenticate using credentials loaded from the .env file.
        server.login(GMAIL_ADDRESS, GMAIL_APP_PASSWORD)

        # WHY: Send the prepared email to all recipients.
        server.send_message(message, to_addrs=recipients)

    # WHY: Confirm successful completion.
    return True
