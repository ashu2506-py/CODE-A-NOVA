# Email Sender CLI

A simple Python-based Email Sender application that sends emails using Gmail SMTP.

## Features

* Send emails directly from the command line
* Custom receiver email input
* Custom subject input
* Custom message input
* SMTP authentication using Gmail App Password
* Error handling using try-except

## Technologies Used

* Python
* smtplib
* EmailMessage

## Project Structure

```text
Email-Services/
│
├── emailServices.py
├── logs.txt
├── README.md
└── .gitignore
```

## How It Works

1. User enters receiver email.
2. User enters email subject.
3. User enters email message.
4. Program connects to Gmail SMTP server.
5. User is authenticated using App Password.
6. Email is sent successfully.

## Requirements

* Python 3.x
* Gmail Account
* Gmail App Password

## Run

```bash
python emailServices.py
```

## Future Improvements

* Email Logging
* Bulk Email Support
* File Attachments
* Contact Management
* GUI Version

```
```
