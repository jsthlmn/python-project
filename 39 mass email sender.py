import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Function to send an email to multiple recipients
def send_mass_email(sender_email, sender_password, subject, body, recipients):
    # Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_email
    message['Subject'] = subject

    # Attach the body with the msg instance
    message.attach(MIMEText(body, 'plain'))

    # Connect to the Gmail SMTP server and send the email
    try:
        # Create a session
        server = smtplib.SMTP('smtp.gmail.com', 587) # For Gmail
        server.starttls()  # Enable security
        server.login(sender_email, sender_password)  # Login to your email

        # Send email to each recipient
        for recipient in recipients:
            message['To'] = recipient
            server.sendmail(sender_email, recipient, message.as_string())
            print(f"Email sent to {recipient}")

        server.quit()  # Close the server
        print("All emails sent successfully!")
    except Exception as e:
        print(f"Error: {e}")

# Sender's email and password
sender_email = "your_email@gmail.com"
sender_password = "your_password"

# Email subject and body
subject = "Your Subject Here"
body = "Your email body content here."

# List of recipients
recipients = ["recipient1@example.com", "recipient2@example.com", "recipient3@example.com"]

# Send the emails
send_mass_email(sender_email, sender_password, subject, body, recipients)
