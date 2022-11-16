#!/usr/bin/env python

import random

print "Content-Type: text/plain"
print

temp = str(random.randint(99999, 99999999))
temp = temp - (temp % 1546)
print "Random value is " + temp;
