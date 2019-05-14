### Server file for Twitter Bot Manager
###
###
import json
import time
import signal
import sys
import mysql.connector
import tweepy

def output(str):
    with open("servdirectvars.json", "r+") as f:
        data = json.load(f)
        data["Output"] = str
        f.seek(0)
        json.dump(data, f)
        f.truncate()

def sigterm_handler(signal, frame):
    output("Exiting and logging status.")
    with open("servdirectvars.json", "r+") as f:
        data = json.load(f)
        data["ServerStatus"] = "False"
        f.seek(0)
        json.dump(data, f)
        f.truncate()
        output("Terminated.")
        sys.exit(1)

class Main():
    def __init__(self):
        with open("servdirectvars.json", "r+") as f:
            data = json.load(f)
            data["ServerStatus"] = "True"
            f.seek(0)
            json.dump(data, f)
            f.truncate()
            ### Try to do Tweepy Authentication
            try:
                auth = tweepy.OAuthHandler(str(data["consumer_key"]), str(data["consumer_secret"]))
                auth.secure = True
                auth.set_access_token(str(data["acess_token"]), str(data["acess_token_secret"]))

                global api
                api = tweepy.API(auth)
                output("Sucessfully logged in as\n" + api.me().name)
            except BaseException as e:
                    output('<html><head/><body><p><span style=" font-size:14pt; color:#ff0000;">Error! Authentication</span></p><p><span style=" font-size:14pt; color:#ff0000;"> Error!</span></p></body></html>')
                    time.sleep(4)                 #Allow time for error message to be read, should implement a prettier workaround, maybe a dedicated errExit() func?
                    sigterm_handler("placeholder", "placeholder") #Anonymous function isnt working for some reason, temporary fix, lambda: sigterm_handler() is not called

            ### Try to do MySQL Authentication
            try:
                cnx = mysql.connector.connect(user=str(data["sqluser"]), password=str(data["sqlpswd"]), database='coisasceu')
                cur = cnx.cursor(buffered=True)
            except mysql.connector.Error as err:
                if err.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
                    output('<html><head/><body><p><span style=" font-size:14pt; color:#ff0000;">Error! MySQL</span></p><p><span style=" font-size:14pt; color:#ff0000;"> Authentication Error!</span></p></body></html>')
                    time.sleep(4)
                    sigterm_handler("placeholder", "placeholder")
                elif err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
                    output('<html><head/><body><p><span style=" font-size:14pt; color:#ff0000;">Error! MySQL</span></p><p><span style=" font-size:14pt; color:#ff0000;"> No DB Error!</span></p></body></html>')
                    time.sleep(4)
                    sigterm_handler("placeholder", "placeholder")
                else:
                    output(str(err))
                    time.sleep(4)
                    sigterm_handler("placeholder", "placeholder")

            self.loop(cur)

    def loop(self, cur):
        while True:
            print("doing loopy things")
            time.sleep(2)

        while 1 == 2:
            query = "SELECT * FROM dadosselenicos WHERE DATE(`date`) = CURDATE()"
            cur.execute(query)

            for (rowdate, moonRise, moonSet, moonPhase, moonBrightness, usedRise, usedSet) in cur:
                print(moonRise)

        time.sleep(2)


signal.signal(signal.SIGTERM, sigterm_handler)
Main()
lambda: sigterm_handler()
