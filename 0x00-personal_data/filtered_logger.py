#!/usr/bin/env python3
'''filtered_logger module'''
import re


def filter_datum(fields: list, redaction: str,
                 message: list, separator: str) -> str:
    '''returns the log message obfuscated'''
    for field in fields:
        message = re.sub(rf'{field}=(.*?){separator}',
                         f'{field}={redaction}{separator}', message)
    return message
