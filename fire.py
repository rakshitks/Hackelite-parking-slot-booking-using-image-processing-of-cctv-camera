## FIREBASE SYNC
import pyrebase

##config={
##    "apiKey": "AIzaSyDdt61vRgDGERxSzSTmqcEZ5dSEBFp1wME",
##    "authDomain": "hackelite1-e28fd.firebaseapp.com",
##    "databaseURL":"https://hackelite1-e28fd.firebaseio.com",
##    "storageBucket":"hackelite1-e28fd.appspot.com"
##    }
##firebase=pyrebase.initialize_app(config)
##auth=firebase.auth()
##user=auth.sign_in_with_email_and_password("prateek44@gmail.com","1234567")
##db=firebase.database()
####arr = []
##for i in range(8):
##    arr.append(int(db.child('basketball').child(f'slot_{i+1}').get().val()))
##
##print(arr)
##nz=len(arr)-sum(arr)
##print(nz)

class FirebaseSync:
    def __init__(self):
        self.config={
        "apiKey": "AIzaSyDdt61vRgDGERxSzSTmqcEZ5dSEBFp1wME",
        "authDomain": "hackelite1-e28fd.firebaseapp.com",
        "databaseURL":"https://hackelite1-e28fd.firebaseio.com",
        "storageBucket":"hackelite1-e28fd.appspot.com"
        }
        self.firebase=pyrebase.initialize_app(self.config)
        self.auth=self.firebase.auth()
        self.user=self.auth.sign_in_with_email_and_password("prateek44@gmail.com","1234567")
        self.db=self.firebase.database()

    def get_slots(self):
        arr = []
        for i in range(8):
            arr.append(int(self.db.child('basketball').child(f'slot_{i+1}').get().val()))
        return arr

    def set_slot(self,x,state):
        self.db.child('basketball').child(f'slot_{x+1}').set(str(state))

    @staticmethod
    def get_free(arr):
        return len(arr)-sum(arr)

    @staticmethod
    def get_free_slots(arr):
        return [i for i,j in enumerate(arr) if j==0]
