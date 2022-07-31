#Script for getting available Global Entry appointments.
#Copied from https://packetlife.net/blog/2019/aug/7/apis-real-life-snagging-global-entry-interview/

import pip._vendor.requests as requests
import time

APPOINTMENTS_URL = "https://ttp.cbp.dhs.gov/schedulerapi/slots?orderBy=soonest&limit=1&locationId={}&minimum=1"
LOCATION_IDS = {
    'Richmond': 7540,
    'Charlotte': 14321,
}

for city, id in LOCATION_IDS.items():
    url = APPOINTMENTS_URL.format(id)
    appointments = requests.get(url).json()
    if appointments:
        print("{}: Found an appointment at {}!".format(city, appointments[0]['startTimestamp']))
    else:
        print("{}: No appointments available".format(city))
    time.sleep(1)