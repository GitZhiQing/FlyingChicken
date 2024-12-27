import pytz
from datetime import datetime


def utc_timestamp_to_shanghai_datetime(utc_timestamp):
    """UTC 时间戳转换成上海时间"""
    utc_dt = datetime.fromtimestamp(utc_timestamp, pytz.utc)
    shanghai_tz = pytz.timezone("Asia/Shanghai")
    shanghai_dt = utc_dt.astimezone(shanghai_tz)
    return shanghai_dt.strftime("%Y-%m-%d %H:%M:%S")
