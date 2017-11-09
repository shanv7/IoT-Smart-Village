from firebase import firebase
import time

firebase = firebase.FirebaseApplication('https://location-tracking-44232.firebaseio.com/', None)

while True:

    result = firebase.get('/LocationOfConductor', None)
    k1 = result.keys()[len(result)-2]
    print('{} minutes'.format(result[k1]["Time"]))
    time.sleep(20)
    