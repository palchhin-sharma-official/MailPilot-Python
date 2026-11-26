# WHY: Import the email sending function from email_sender.py.
from email_sender import send_email


def main():

    print("\n========== GMAIL AUTOMATION SYSTEM ==========\n")

    # WHY: Collect the primary recipient's email address.
    recipient = input("Enter recipient email: ").strip()

    # WHY: Collect the email subject.
    subject = input("Enter email subject: ").strip()

    # WHY: Collect the email message.
    print("\nEnter your email message:")
    body = input("> ").strip()

    # WHY: Accept multiple CC addresses separated by commas.
    cc_input = input("\nEnter CC emails (comma separated, optional): ").strip()

    # WHY: Convert comma-separated CC input into a list.
    cc = [email.strip() for email in cc_input.split(",") if email.strip()]

    # WHY: Accept multiple BCC addresses separated by commas.
    bcc_input = input("Enter BCC emails (comma separated, optional): ").strip()

    # WHY: Convert comma-separated BCC input into a list.
    bcc = [email.strip() for email in bcc_input.split(",") if email.strip()]

    # WHY: Accept optional attachment file paths.
    attachment_input = input(
        "Enter attachment paths (comma separated, optional): "
    ).strip()

    # WHY: Convert attachment paths into a list.
    attachments = [
        path.strip().strip('"')
        for path in attachment_input.split(",")
        if path.strip()
    ]
    
    # WHY: Display email details before asking for confirmation.
    print("\n========== EMAIL PREVIEW ==========")
    print("From:", "Your configured Gmail address")
    print("To:", recipient)
    print("CC:", ", ".join(cc) if cc else "None")
    print("BCC:", "Configured (hidden from recipients)" if bcc else "None")
    print("Subject:", subject)
    print("Message:", body)
    print("Attachments:", attachments if attachments else "None")
    
    # WHY: Ask for confirmation before sending the email.
    confirmation = input("\nDo you want to send this email? (yes/no): ").strip().lower()

    if confirmation != "yes":
        print("Email sending cancelled.")
        return
    
    
    try:

        # WHY: Call the email sending function with all collected details.
        send_email(
            recipient,
            subject,
            body,
            cc=cc,
            bcc=bcc,
            attachments=attachments
        )

        print("\nEmail sent successfully!")

    except Exception as error:

        # WHY: Display an understandable error instead of crashing silently.
        print(f"\nEmail could not be sent: {error}")


# WHY: Execute main() only when this file is run directly.
if __name__ == "__main__":
    main()