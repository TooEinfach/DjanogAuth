from __future__ import absolute_import, unicode_literals

from celery import shared_task

@shared_task
def add(x, y):
    return x + y

### Read and convert file task
# import json
# import os

# lineByLine = []
# fileList = []

# for f in os.listdir('/home/nick/Documents/projects/jsonFiles'):
#     fileList.append(f)

# print(fileList)

# for f2 in fileList:
#     with open('/home/nick/Documents/projects/jsonFiles/' + f2) as newFile:
#         db = json.load(newFile)
#         lineByLine.append(db)

# # with open('/home/nick/Documents/projects/numeric.json') as file:
# #     db = json.load(file)
# #     lineByLine.append(db)

# for line in lineByLine:
#     print(line)

# # lineByLine_dumped = json.dumps(lineByLine)
# # print(lineByLine_dumped)
# with open('testing.json','w') as lineByLine_dumped:
#     json.dump(lineByLine, lineByLine_dumped)