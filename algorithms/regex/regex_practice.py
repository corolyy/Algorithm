# -*- coding: utf-8 -*-
import re


email = 'lyy@163.com'
no_email_1 = '@'
no_email_2 = 'lyy@'
no_email_3 = 'lyy.163.com'
no_email_4 = 'lyy@163 com'
candidates = [email, no_email_1, no_email_2, no_email_3, no_email_4]

def is_email(candidate):
    r = r'[0-9a-zA-z\_]+@[0-9a-zA-z\_]+\.[0-9a-zA-z\_]+'
    if re.match(r, candidate):
        print '\'{}\'\t is a email'.format(candidate)
    else:
        print '\'{}\'\t is not a email'.format(candidate)

map(is_email, candidates)