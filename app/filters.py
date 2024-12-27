import time


def utc_timestamp_to_shanghai_datetime(utc_timestamp):
    """UTC 时间戳转换成上海时间"""
    timeArray = time.localtime(utc_timestamp)
    return time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
