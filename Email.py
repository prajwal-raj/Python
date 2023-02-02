import smtplib

def send_email(subject, message, from_addr, to_addr,
               password, smtp_server='smtp.gmail.com', smtp_port=587):
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.ehlo()
        server.starttls()
        server.login(from_addr, password)
        message = 'Subject: {}\n\n{}'.format(subject, message)
        server.sendmail(from_addr, to_addr, message)
        print('Email sent successfully!')
    except Exception as e:
        print('Failed to send email:', e)
    finally:
        server.quit()

if __name__ == '__main__':
    subject = input('Subject: ')
    message = input('Message: ')
    from_addr = input('From: ')
    to_addr = input('To: ')
    password = input('Password: ')
    send_email(subject, message, from_addr, to_addr, password)
