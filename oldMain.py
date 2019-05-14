# IMPORT
import mysql.connector
from mysql.connector import errorcode
import tweepy
from datetime import datetime
import json
import time

consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

# GLOBAL VARIABLES (IF ANY)
moonPhasesTable = ("lua nova", "lua cheia", "lua minguante", "lua crescente")


# CLASSES
def emoji(brightness, cur):
    query = ("SELECT * FROM dadosemojis ORDER BY id DESC LIMIT 0, 1")
    cur.execute(query)
    for(id, lastMoonPhase) in cur:
        if brightness <= 5:
            return "🌑"
        elif brightness >= 6 or brightness <= 45:
            if int(lastMoonPhase) == 1:
                return "🌒"
            else:
                return "🌖"
        elif brightness >= 46 or brightness <= 55:
            if int(lastMoonPhase) == 1:
                return "🌓"
            else:
                return "🌗"
        elif brightness >= 56 or brightness <= 95:
            if int(lastMoonPhase) == 1:
                return"🌔"
            else:
                return "🌘"
        elif brightness >= 96:
            return "🌕"
        else:
            print("mano how the fuck é que chegaste aqui ahahahahahaaahhafoda se juro")


class Main:
    def __init__(self):
        try:
            auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
            auth.secure = True
            auth.set_access_token(access_token, access_token_secret)

            global api
            api = tweepy.API(auth)

            print("Logged onto: " + api.me().name)
            Main.databaseMain(self)
        except BaseException as e:
            print("Error in main()", e)
            exit(1)

    def databaseMain(self):
        try:
            cnx = mysql.connector.connect(user='root', password='root', database='updateselenicos')
            cur = cnx.cursor(buffered=True)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
                print("Goodbye.")
                exit(1)
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
                print("Goodbye.")
                exit(1)
            else:
                print(err)
                print("Goodbye.")
                exit(1)

        Main.mainTryLoop(self, cur)

    def mainTryLoop(self, cur):
        while True:
            query = "SELECT * FROM data WHERE DATE(`rowdate`) = CURDATE()"
            cur.execute(query)

            for (id, rowdate, moonRise, moonSet, moonPhase, moonBrightness, usedRise, usedSet) in cur:
                # print("Id " + str(id),"Date " + str(rowdate),"Rise Time " + str(moonRise),"Moon Set " + str(
                # moonSet),"Moon Phase " + str(moonPhase),"Moon Brightness " + str(moonBrightness))

                # converts xx:xx:xx to xxxxxx
                convertedRise, convertedSet = str(moonRise).replace(":", ""), str(moonSet).replace(":", "")

                if len(convertedRise) == 5:
                    convertedRise2 = "0" + convertedRise[:-2]

                else:
                    convertedRise2 = convertedRise[:-2]

                if len(convertedSet) == 5:
                    convertedSet2 = "0" + convertedSet[:-2]

                else:
                    convertedSet2 = convertedSet[:-2]

                #if Rise entry is in the last hour
                if int(convertedRise2) - 100 == int(datetime.now().strftime('%H%M')):
                    if int(usedRise) == 1:
                        break
                    convertedRise3 = convertedRise2[:2] + ":" + convertedRise2[2:]
                    with open('my_data.json', 'w') as out_f:
                        json.dump('a lua vai nascer às %s\né %s %s\nestá a %s%% da sua luminosidade total' % (
                        convertedRise3, moonPhasesTable[int(moonPhase)], emoji(moonBrightness), moonBrightness), out_f)

                    with open('my_data.json', 'r') as in_f:
                        api.update_status(json.load(in_f))
                        print("Tweeted! " + json.load(in_f))
                        query = ("UPDATE dadosselenicos SET usedRise = 1 WHERE date = CURDATE()")
                        cur.execute(query)
                        if int(moonPhase) == 1:
                            query = ("INSERT INTO dadosemojis (lastMoonPhase) VALUES ('1')")
                            cur.execute(query)

                        elif int(moonPhase) == 2:
                            query= ("INSERT INTO dadosemojis (lastMoonPhase) VALUES ('2')")


                if int(convertedSet2) - 100 == int(datetime.now().strftime('%H%M')):
                    if int(usedSet) == 1:
                        break
                    convertedSet3 = convertedSet2[:2] + ":" + convertedSet2[2:]
                    with open('my_data.json', 'w') as out_f:
                        json.dump('a lua vai nascer às %s\né %s %s\nestá a %s%% da sua luminosidade total' % (
                            convertedSet3, moonPhasesTable[int(moonPhase)], emoji(moonBrightness, cur), moonBrightness),
                                  out_f)

                    with open('my_data.json', 'r') as in_f:
                        api.update_status(json.load(in_f))
                        print("Tweeted! " + json.load(in_f))
                        query = ("UPDATE dadosselenicos SET usedSet = 1 WHERE date = CURDATE()")
                        cur.execute(query)
                        if int(moonPhase) == 1:
                            query = ("INSERT INTO dadosemojis (lastMoonPhase) VALUES ('1')")
                            cur.execute(query)

                        elif int(moonPhase) == 2:
                            query= ("INSERT INTO dadosemojis (lastMoonPhase) VALUES ('2')")
                time.sleep(10)

Main()
print("Exiting.")
