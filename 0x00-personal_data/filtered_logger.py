#!/usr/bin/env python3
'''filtered_logger module'''
import re
import logging
from typing import List


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

    def __init__(self, fields: List[str] = None) -> None:
        '''Constructor'''
        self.fields = fields
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        '''filter values in incoming log records using filter_datum'''
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)
