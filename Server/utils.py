'''
Author: wuqianying
Date: 2022-10-29 11:21:47
LastEditors: wuqianying
LastEditTime: 2022-11-04 14:43:04
'''
import hashlib
import hmac
import time

from config import APP_SECRET


def gen_signature(data):
    data['timestamp'] = str(int(time.time() * 1000))

    params = ''.join([
        data['grant_type'],
        data['client_id'],
        data['source'],
        data['timestamp'],
    ])

    data['signature'] = hmac.new(
        APP_SECRET, params.encode('utf-8'), hashlib.sha1).hexdigest()


def flatten_live_dict(d, keys=[]):
    def items():
        for key, value in d.items():
            if key in keys:
                yield key, value
            elif isinstance(value, dict):
                for subkey, subvalue in flatten_live_dict(value, keys).items():
                    if subkey != 'id' and subkey in keys:
                        yield subkey, subvalue

    return dict(items())
