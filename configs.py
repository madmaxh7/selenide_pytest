"""
Configs file
"""
import random
import time

web_driver_platform = 'chrome'
base_url_web = "https://www.wikipedia.org/"


def unique_id():
    """
    Return unique random ID
    """
    rand_s = str(random.randint(1, 999))
    rand_s = ("0" * (3 - len(rand_s))) + rand_s
    return time.strftime("%Y%m%d%H%M%S", time.gmtime()) + rand_s
