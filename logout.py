#!/usr/bin/env python3


from requests import get


def logout():
    res = get('http://phc.prontonetworks.com/cgi-bin/authlogout?')
    if res.status_code:
        print('Logged out')
    else:
        print('Unable to Logout')


logout()
