import RPi.GPIO as GPIO
import time
import os
from datetime import datetime
import smtplib
from smtplib import SMTP
from smtplib import SMTPException
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

pinLED = 7
pinSWITCH = 8


GPIO.setmode(GPIO.BOARD)
GPIO.setup(pinLED, GPIO.OUT)
GPIO.setup(pinSWITCH, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    input_state = GPIO.input(pinSWITCH)
    if input_state == False:
        os.system('fswebcam -r 1024x720 -S 20 --jpeg 50 --save /home/pi/Završni/photo.jpg')
        print('Netko zvoni')
        
        #send mail
        f_time = datetime.now().strftime('%a %d %b @ %H:%M')

        toaddr = 'kf181004@gmail.com'    # redacted
        me = 'kfraspberry@gmail.com' # redacted
        subject = 'Netko zvoni ' + f_time

        msg = MIMEMultipart()
        msg['Subject'] = subject
        msg['From'] = me
        msg['To'] = toaddr
        msg.preamble = "Photo @ " + f_time

        fp = open('photo.jpg', 'rb')
        img = MIMEImage(fp.read())
        fp.close()
        msg.attach(img)

        try:
           s = smtplib.SMTP('smtp.gmail.com',587)
           s.ehlo()
           s.starttls()
           s.ehlo()
           s.login(user = 'kfraspberry@gmail.com',password = 'a4d919ea')
           
           s.sendmail(me, toaddr, msg.as_string())
           s.quit()

        except SMTPException as error:
              print ("Error: unable to send email :  {err}".format(err=error))

    
        time.sleep(0.2)

    if input_state == True:
        GPIO.output(pinLED, GPIO.LOW)
        time.sleep(0.2)
GPIO.cleanup()
        
