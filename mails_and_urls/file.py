"""
Python code to count the number of emails that have same
domain as a url

Code developed by Masino

QUESTION:
Given a list of emails and URLs, return a dictionary, where each
key is a URL and the value is how many emails have the same domain.
Note that the domains begin with  www.  whereas the emails do not
and that emails with domains not in the list of urls should be ignored.

STEP 1
Create the function and define the containers of emails
and urls"""
def mail_count():
    email_container = ['obi@gmail.com', 'kc@outlook.com', 'fide@yahoo.com',
              'neche@yahoo.com', 'sanchilo@yahoo.com', 'support@alx.com',
              'ebube@outlook.com', 'saga@outlook.com', 'team@letalk.com',
              'chisom@gmail.com', 'uche@yahoo.com', 'ada@yahoo.com',
              'obum@outlook.com', 'emmy@yahoo.com', 'nwa@outlook.com']

    url_container = ['www.outlook.com', 'www.google.com', 'www.jenkins.com',
            'www.gmail.com', 'www.yahoo.com', 'www.domain.com']
    """
    STEP 2
    Select all mails that has same domain name and put in a container
    """
    """
    STEP 2 (EDITED)
    It was supposed to be: split all mails to be able to read the
    domain names"""
    mail_number = 0
    updated_email_container = []
    for item in email_container:
        mail_number += 1
        updated_email_container.append(item.split("@"))
    print(f"The available emails are {mail_number}:\n{email_container}\n")
    """
    STEP 3
    Identify the domain names of the urls by splitting them with the split function
    """
    url_number = 0
    updated_url_container = []
    for item in url_container:
        url_number += 1
        updated_url_container.append(item.split("."))
    print(f"The given urls are {url_number}:\n{url_container}\n")
    """
    STEP 4
    Since the urls are given to us and the quantity is not much,
    let's identify their domain names singly and write a conditional
    statement to compare them to the mails domain names.
    """
    outlook = 0
    google = 0
    jenkins = 0
    gmail = 0
    yahoo = 0
    domain = 0
    for item in updated_email_container:
        if item[1] == "outlook.com":
            outlook += 1
        elif item[1] == "google.com":
            google += 1
        elif item[1] == 'jenkins.com':
            jenkins += 1
        elif item[1] == 'gmail.com':
            gmail += 1
        elif item[1] == 'yahoo.com':
            yahoo += 1
        elif item[1] == 'domain.com':
            domain += 1
        else:
            pass
    """
    STEP 5
    Define the dictionary and compare the keys and values
    """
    final_dictionary = {'www.outlook.com':outlook, 'www.google.com':google,
                        "www.jenkins.com":jenkins, "www.gmail.com":gmail,
                        "www.yahoo.com":yahoo, "www.domain.com":domain}
    print(f"Below is a dict of each url and how many mails that have the same domain name:\n{final_dictionary}\n")


if __name__ == "__main__":
    mail_count()

print("Code developed by Masino")
    

