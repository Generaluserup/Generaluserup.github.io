import os
def domain():
    os.system('apt-get update')
    os.system('apt-get upgrade')
    os.system('apt-get install curl net-tools bash-completion wget lsof nano')
    os.system('echo order hosts,bind>letclhost.conf')
    os.system('echo multi on>>/etcl/host.conf')
    os.system('hostnamectl set-hostname mail.honorovich.com')
    os.system('echo 10.0.2.15 honorovich.com mail.honorovich.com>>/etc/hosts')
    input('\n Computer will reboot, start script again after reboot to install postfix.\n Press ENTER to continue...\n')
    os.system('init 6')

    def postfix():
        os.system('apt install postfix')
        os.system('cp /etc/postfix/main.cf{,.backup}')
        os.system('cp -f main.cf /etc/postfix/main.cf')
        os.system('systemctl restart postfix')


        def dovecot():
            os.system('apt install dovecot-core dovecot-imapa')
            os.system('cp -f dovecit.conf /etc/dovecot/dovecot.conf')
            os.system('cp -f 10-auth.conf /etc/dovecot/conf.d/10-auth.conf')
            os.system('cp -f 10-mail.conf /etc/dovecot/conf.d/10-mail.conf')
            os.system('cp -f 10-master.conf /etc/dovecot/conf.d/10-master.conf')
            os.system('systemclt restart dovecot.service')
            os.system('echo export MAIL=$HOME/Maildir>>/etc/profile')
            print('Congratulations')

def webmail():
    os.system('apt install apache2.php7.0 libapache2-mod.php7.0 php7.0-curl php7.0-xml')
    os.system('cd /var/www/html')
    os.system('rm /var/www/html/index.html')
    os.system('cd /var/www/html && curl -sL https://repository.rainloop.net/installer.php\php')
    print('Congratulations')

    def adduser():
        username=input('Print user name please')
        os.system('adduser'+username)
        print('user:'+username+'@honorovich.com added.')

        def status():
            while True:
                try:
                    i=int(input('1-Install Postfix; 2-Dovecot installer; 0-exit'))
                    if i==1:
                        os.system('systemctl status postfix')
                    elif i==2:
                            os.system('systemctl status doveecot')
                    elif i==0:
                                break
                    else:
                        print('Please choose number again.')
                except Exception:
                            print('There is no such option, please press 1,2 or 0.')

        while True:
             try: 
                 key=input(input('PostFix & WebMail installer.\n1 - Configure Domain. \n2-install & configure PostFix.\n3-install& configure dovecot.\n4-Install WebMail.\n5-Add account.\n6-Check status.\n0-Exit.'))

                 if key==1:
                     domain()
                 elif key==2:
                     postfix()
                 elif key==3:
                     dovecot()
                 elif key==4:
                     webmail()
                 elif key==5:
                     adduser()
                 elif key==6:
                     status()
                 elif key==0:
                     break
                 else:
                      print('\nThere is no such option.Try again.\nTip: choose number in menu.\n')
                                                                
             except Exception:
                 print('\nThere is no such option.Try again.\nOhh: choose number in menu.\n') 
