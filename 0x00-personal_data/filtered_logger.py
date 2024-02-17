#!/usr/bin/env python3
'''filtered_logger module'''
import re
import logging
from typing import List
import csv

def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    '''returns the log message obfuscated'''
    for field in fields:
        message = re.sub(rf'{field}=(.*?){separator}',
                         f'{field}={redaction}{separator}', message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """
    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        '''Constructor'''
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        '''filter values in incoming log records using filter_datum'''
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)

def get_logger() -> logging.Logger:
    '''get looger'''
    user_data = logging
    user_data.basicConfig(level=logging.INFO)
    user_data.StreamHandler(RedactingFormatter)
    with open('user_data.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
    return reader
PII_FIELDS = ['name', 'email', 'phone', 'password', 'ip']
