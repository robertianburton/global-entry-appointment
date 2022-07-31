#Script for getting available Global Entry appointments.
#Copied from https://packetlife.net/blog/2019/aug/7/apis-real-life-snagging-global-entry-interview/

import pip._vendor.requests as requests
import time
import sys
import ctypes

APPOINTMENTS_URL = "https://ttp.cbp.dhs.gov/schedulerapi/slots?orderBy=soonest&limit=1&locationId={}&minimum=1"
LOCATION_IDS = {
    'Bowling Green NYC': 6480,
    'Jamaica JFK': 5140,
    'Newark NJ': 5444,
    #'Anchorage AK': 7540, 
}
SLEEP_TIME = 130

try:
    while True:
        for city, id in LOCATION_IDS.items():
            url = APPOINTMENTS_URL.format(id)
            appointments = requests.get(url).json()
            if appointments:
                print("{}: Found an appointment at {}!".format(city, appointments[0]['startTimestamp']))
                ctypes.windll.user32.MessageBoxW(0, "{}: Found an appointment at {}. Go to https://ttp.cbp.dhs.gov/ now!".format(city, appointments[0]['startTimestamp']), "Global Entry Appointment", 1)
            else:
                print("{}: No appointments available".format(city))
            time.sleep(1)
        time.sleep(SLEEP_TIME)
except KeyboardInterrupt:
    sys.exit(0)