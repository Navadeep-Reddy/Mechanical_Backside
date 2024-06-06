
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_mail(user_email,about_name,vehicle_type,repair_type):
    # Email content
    from_email = "rishwanth605@gmail.com"  
    from_password = "aqhb qplg qbks bqkw" # This is the app password of the mail  
    to_email = user_email

    subject = "Order Completed"
    body = f"Hello{about_name},\n\nYour{repair_type} order for your {vehicle_type} has been completed.\n\nThank you for choosing our service!\n\nBest regards,\nSK Mechanics"

    # Setup the MIME
    message = MIMEMultipart()
    message['From'] = from_email
    message['To'] = to_email
    message['Subject'] = subject

    # Attach the body with the message instance
    message.attach(MIMEText(body, 'plain'))

    # Create SMTP session
    try:
        session = smtplib.SMTP('smtp.gmail.com', 587)  # Use Gmail with port 587
        session.starttls()  # Enable security
        session.login(from_email, from_password)  
        text = message.as_string()
        session.sendmail(from_email, to_email, text)
        session.quit()
        print("Mail Sent Successfully")
    except Exception as e:
        print(f"Failed to send email: {str(e)}")

if __name__ == "__main__":
    send_mail("tomailadress@gmail.com") 
