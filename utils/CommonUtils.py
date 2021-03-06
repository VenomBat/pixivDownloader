# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os

import datetime


def singleton(cls, *args, **kw):
    instances = {}

    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]

    return _singleton


def get_url_param(url, param):
    import urlparse
    try:
        result = urlparse.urlparse(url)
        return urlparse.parse_qs(result.query)[param][0]
    except Exception:
        return None


def validate_date_str(date_str):
    try:
        datetime.datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False


def set_int(int_num, default_value=0):
    try:
        return int(int_num)
    except Exception:
        return default_value


def is_not_empty(val):
    return not is_empty(val)


def is_empty(val):
    if not val:
        return True
    if len(val.strip()) == 0:
        return True
    return False


def filter_dir_name(name):
    import re
    return re.sub('[\/:*?"<>.|]', '', name).strip()


def write_topic(file_path, topic):
    import codecs
    topic_file = codecs.open(file_path, 'w', encoding='utf-8')
    topic_file.write("Label = " + topic.label + "\n")
    topic_file.write("Title = " + topic.title + "\n")
    topic_file.write("Href = " + topic.href + "\n")
    topic_file.write("PubTime = " + topic.pub_time + "\n")
    tagstr = ""
    for tag in topic.tags:
        tagstr += " " + tag
    topic_file.write("Tag =" + tagstr + "\n")
    topic_file.close()


def write_topic_des(file_path, data):
    import codecs
    try:
        topic_file = codecs.open(file_path, 'a', encoding='utf-8')
        contents = ''
        if os.path.exists(file_path):
            contents = codecs.open(file_path, 'r', encoding='utf-8').read()
        # 已写入过 下载数量则跳过写入
        if contents.find("Title =") < 0:
            topic_file.write("Title = " + data["title"] + "\n")
        if contents.find("Href =") < 0:
            topic_file.write("Href = " + str(data["url"]) + "\n")
        if contents.find("Description =") < 0:
            topic_file.write("Description = " + data["description"] + "\n")
        if contents.find("IlluNum =") < 0:
            topic_file.write("IlluNum = " + str(data["size"]) + "\n")
    except Exception as e:
        print("Write Topic Description Fail")
        print(e)


# 构建回掉通知消息
def build_callback_msg(path, id=None, url=None, keywords=None):
    if id:
        show = "Id"
        show1 = id
    elif url:
        show = "Url"
        show1 = url
    elif keywords:
        show = 'Keywords'
        show1 = keywords
    if path:
        show2 = path
    else:
        show2 = "Download Fail"
    msg = "%s:%s\nFile:%s\n\n"
    return msg % (show, show1, show2)


def format_bool(bool_value):
    if type(bool_value) == bool:
        return 'true' if bool_value else 'false'
    if bool_value in ['true', 'True']:
        return 'true'
    else:
        return 'false'
