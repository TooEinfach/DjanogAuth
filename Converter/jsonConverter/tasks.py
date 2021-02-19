from __future__ import absolute_import, unicode_literals

from celery import shared_task

import json
import os
import shutil

@shared_task
def add(x, y):
    return x + y


@shared_task
def merge():
    ## Read and convert file task
    
    lineByLine = []
    fileList = []

    for f in os.listdir('/opt/posts/files/media/json/'):
        fileList.append(f)

    print(fileList)

    for f2 in fileList:
        with open('/opt/posts/files/media/json/' + f2) as newFile:
            db = json.load(newFile)
            lineByLine.append(db)

    # with open('/home/nick/Documents/projects/numeric.json') as file:
    #     db = json.load(file)
    #     lineByLine.append(db)

    for line in lineByLine:
        print(line)

    # lineByLine_dumped = json.dumps(lineByLine)
    # print(lineByLine_dumped)
    with open('/opt/posts/files/media/json/daily.json','w') as lineByLine_dumped:
        json.dump(lineByLine, lineByLine_dumped)

@shared_task
def move():
    target = '/opt/S/USERS/FIN/Cashiers/Upload/daily.json'
    original = '/opt/posts/files/media/json/daily.json'
    shutil.move(original,target)

@shared_task
def cleanup():
    target = '/opt/archive/files/'
    original = '/opt/posts/files/media/json/'

    files = os.listdir(original)

    for f in files:
        shutil.move(original + f, target)