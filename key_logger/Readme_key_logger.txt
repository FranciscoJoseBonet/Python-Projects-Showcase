*********************************************************
*              Program Utility Description              *
*********************************************************

This Python program functions as a keylogger.
It monitors and records keyboard input, saving it to a timestamped text file.
The recorded data is then emailed to a specified address. Key features include:

- **Key Logging**: Captures keystrokes and saves them to a text file.
- **Periodic Saving**: Automatically saves and emails the log file every 60 seconds.
- **Email Functionality**: Sends the log file as an email attachment using secure encryption.
- **Startup Integration**: Configures itself to start automatically with Windows by creating necessary batch and VBScript files.

********************************************************
*                 Library Description                  *
********************************************************

- **`datetime`**: Handling date and time operations.
- **`pynput`**: Monitoring and controlling keyboard events.
- **`cryptography`**: Implementing symmetric encryption with Fernet.
- **`email`**: Constructing and managing email content.
- **`getpass`**: Secure password input.
- **`os`**: Interacting with the operating system.
- **`smtplib`**: Sending emails using the Simple Mail Transfer Protocol (SMTP).
- **`time`**: Managing and manipulating time-related tasks.