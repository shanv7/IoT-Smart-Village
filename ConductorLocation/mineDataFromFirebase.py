from firebase import firebase
import time

firebase1 = firebase.FirebaseApplication('https://location-tracking-44232.firebaseio.com/', None)

while True:

    result = firebase1.get('LocationOfConductor', None)
    k1 = sorted(result.keys())[-1]
    print('{0:.2f} minutes'.format(result[k1]["Time"]))
    time.sleep(5)
