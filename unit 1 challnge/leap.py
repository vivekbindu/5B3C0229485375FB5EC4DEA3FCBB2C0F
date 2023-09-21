Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def isleapYear(year):
...     if (year % 4==0 and year % 100 != 0) or year % 400 == 0:
...         return True
...     else:
...         return False
... year = int(input)
SyntaxError: invalid syntax
>>> if isleap(year):
...     print('{} is a leap year.'.format(year))
... else:
