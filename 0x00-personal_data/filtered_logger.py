#!/usr/bin/env python3
'''filtered log'''
import re


def filter_datum(fields, redaction, message, separator):
    '''filter'''
    for field in fields:
        message = re.sub(rf'{field}=(.*?){separator}',
                         f'{field}={redaction}{separator}', message)
    return message