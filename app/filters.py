import pytz
from datetime import datetime


def utc_timestamp_to_shanghai_datetime(value):
    """UTC 时间戳转换成上海时间"""
    utc_dt = datetime.fromtimestamp(value, pytz.utc)
    shanghai_dt = utc_dt.replace(tzinfo=pytz.utc).astimezone(
        pytz.timezone("Asia/Shanghai")
    )
    return shanghai_dt.strftime("%Y-%m-%d %H:%M:%S")
