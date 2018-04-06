def Email(EmailAdress, NewPassword = None, VerifyNum = None):
    import smtplib

    gmail_user = 'LoginAccess3.0@gmail.com'  
    gmail_password = 'Cake1234'

    sent_from = gmail_user  
    to = [EmailAdress]  
    #subject = 'OMG Super Important Message'  
    #body = "Hey, what's up?\n\n- You"

    if NewPassword:
        email_text = """
        Hello LoginAccess user!

        You requested for your password to be reset. Your new password is 
        {NewPassword}
        It is recommened you change this password when you next login!
        Have fun and thanks for using the LoginAccess systems



        -This is an automated email: if you do not know why you are getting this please ignore it
        -Do not reply to this adress
        """.format(NewPassword = NewPassword)
    elif VerifyNum:
        email_text = """
        Hello LoginAccess user!

        An account wanted to link with this email adress: Please type in the following code on the LoginAccess system 
        {VerifyNum}
        This number will only work once!



        -This is an automated email: if you do not know why you are getting this please ignore it
        -Do not reply to this adress
        """.format(VerifyNum = VerifyNum)

    try:  
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, email_text)
        server.close()

        return True
    except Exception as Identifier:
        print(Identifier)  
        return False