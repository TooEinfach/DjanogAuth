from __future__ import absolute_import, unicode_literals

from celery import shared_task

import json
import os
import shutil
from datetime import datetime


# Task to merge all json files sumbitted today
@shared_task
def merge():
    lineByLine = []
    fileList = []

    for f in os.listdir('/opt/posts/files/media/json/'):
        fileList.append(f)

    print(fileList)

    for f2 in fileList:
        with open('/opt/posts/files/media/json/' + f2) as newFile:
            db = json.load(newFile)
            lineByLine.append(db)


    for line in lineByLine:
        print(line)

    with open('/opt/posts/files/media/json/daily.json','w') as lineByLine_dumped:
        json.dump(lineByLine, lineByLine_dumped)

# task to move daily.json file
@shared_task
def move():
    target = '/opt/S/USERS/FIN/Cashiers/Upload/daily.json'
    original = '/opt/posts/files/media/json/daily.json'
    shutil.move(original,target)

# task to clean up and archive daily submissions
@shared_task
def cleanup():
    today = datetime.now()
    os.mkdir('/opt/archive/files/' + today.strftime('%Y%m%d'))

    path = '/opt/archive/files/'
    dailyFolder = ''

    now = today.strftime('%Y%m%d')

    folders = os.listdir(path)

    # loop threw folders in archive dir and find todays folder
    for f in folders:
        if f == now:
            dailyFolder = os.path.join(path, f)

    original = '/opt/posts/files/media/json/'

    files = os.listdir(original)

    # move loop threw files in json directory and move them to archive daily folder
    for f in files:
        shutil.move(original + f, dailyFolder)