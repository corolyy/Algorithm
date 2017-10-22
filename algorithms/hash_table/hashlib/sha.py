# -*- coding: utf-8 -*-
import hashlib

test_str = 'a test string'

print hashlib.sha1(test_str).digest() # --> -�]��Tx�B��w $҂��
print hashlib.sha1(test_str).hexdigest() # --> 2da75da5c85478df42df0f917700241ed282f599
print hashlib.sha1(test_str).hexdigest() # str
print hex(16)
print int('10', 16)
print bin(15)