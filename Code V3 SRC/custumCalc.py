import math
import base64
import calendar
import datetime
import random
import json
import string
import ast

def get_minimum(*values):
    val=int(values[0])
    for i in values:
        i=int(i)
        val = min(val,i)
    return val

def get_maximum(*values):
    val=int(values[0])
    for i in values:
        i=int(i)
        val = max(val,i)
    return val

def get_json_value(jsonStr,key):
    jsonBody=json.loads(jsonStr)
    keys=key.split("/")
    keys = [k for k in keys if k!=""]
    val="fakeValue"
    for key in keys:
        val=jsonBody[key]
        jsonBody=val
    if val=="fakeValue":
        print("Key Passed is not present in the Json Body, Please check the arguments Values")
    return val

def central_time_to_utc_hours(date):
    c = calendar.Calendar(firstweekday=calendar.SUNDAY)
    now = datetime.datetime.now()
    date=datetime.datetime.strptime(date, "%Y-%m-%d").date()
    print(c)
    year=date.year
    month= 3
    monthcal = c.monthdatescalendar(year,month)

    date1 = [day for week in monthcal for day in week if \
             day.weekday() == calendar.SUNDAY and \
             day.month == month][1]
    print(date1)

    month= 11
    monthcal = c.monthdatescalendar(year,month)

    date2 = [day for week in monthcal for day in week if \
             day.weekday() == calendar.SUNDAY and \
             day.month == month][0]
    print(date2)
    hours=6
    if date>=date1 and date<date2:
        hours=5
    return   hours

def generate_random_number(n):
    val=random.randint(0,n)
    return val

def get_basic_key(clientKey,clientSecret):
    message = clientKey + ':' + clientSecret
    message_bytes = message.encode('utf-8')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('utf-8')
    return base64_message

def get_decoded_key(qurl):
    mfaqurl = qurl
    base64_mfaqurl = base64.b64decode(mfaqurl)
    base64_msg = base64_mfaqurl.decode('utf-8')
    return base64_msg

def check_range(value, a, b, strict=False):
    """Check that a value lies in a given range
    :param value: value to test
    :param a: lower bound
    :param b: upper bound
    :return: nothing
    """
    if strict is True:
        if value <= a:
            raise ValueError(" {} must be greater (or equal) than {}".format(value, a))
        if value >= b:
            raise ValueError(" {} must be less (or less) than {}".format(value, b))
    elif strict is False:
        if value < a:
            raise ValueError(" {} must be greater than {}".format(value, a))
        if value > b:
            raise ValueError(" {} must be less than {}".format(value, b))


def rgb2hex(r, g, b):
    """Convert RGB to hexadecimal color
    :param: can be a tuple/list/set of 3 values (R,G,B)
    :return: a hex vesion ofthe RGB 3-tuple
    """
    check_range(r, 0, 255)
    check_range(g, 0, 255)
    check_range(b, 0, 255)
    return '#%02X%02X%02X' % (r, g, b)


def rgb_to_hex(rgb):
    try:
        rgb = ast.literal_eval(rgb)
        return rgb2hex(rgb[0],rgb[1],rgb[2])
    except:
        return None