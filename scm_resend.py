# -*- coding: utf-8 -*-
import json

import requests
import traceback


def do_resend_scm(log_file):
    try:
        with open(log_file, 'r', encoding='windows-1252') as f:
            for line in f:
                if line.find('sync returned info to scm, epcs = ') < 0:
                    continue

                operate_time = line.split('[')[1].split(']')[0].split(',')[0]
                epcs = line.split('=')[1].replace("\'", '"')
                body = {
                    'operate_time': operate_time,
                    'epcs': json.loads(epcs)
                }

                requests.delete('http://127.0.0.1:11000/returnconfirm', json=body)
    except Exception as err:
        print("err = {} - {}".format(err, traceback.format_exc()))


if __name__ == '__main__':
    files = ['rfid_server.log.2020-12-27']

    for one_log_file in files:
        do_resend_scm(one_log_file)

