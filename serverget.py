### ServerGet module for Twitter Bot Manager
###
###
import json
import subprocess

def ServerStatus():
    with open('servdirectvars.json', 'r') as f:
        return json.load(f)["ServerStatus"]

def tweetsMade():
    with open('servdirectvars.json', 'r') as f:
        return json.load(f)["TweetsMade"]

def errOutput():
    with open('servdirectvars.json', 'r') as f:
        return json.load(f)["Output"]

def latestTweet():
    with open('servdirectvars.json', 'r') as f:
        return json.load(f)["LatestTweet"]

def nextTweet():
    with open('servdirectvars.json', 'r') as f:
        return json.load(f)["NextTweet"]

def toggleStatus():
    if ServerStatus() == "False":
        global p
        p = subprocess.Popen(["python", "server.py"])
    elif ServerStatus() == "True":
        try:
            p.terminate()
        except:
            with open("servdirectvars.json", "r+") as f:
                data = json.load(f)
                data["ServerStatus"] = "False"
                f.seek(0)
                json.dump(data, f)
                f.truncate()

def consumer_key():
    with open('servdirectvars.json', 'r') as f:
        return json.load(f)["consumer_key"]

def consumer_secret():
    with open('servdirectvars.json', 'r') as f:
        return json.load(f)["consumer_secret"]

def acess_token():
    with open('servdirectvars.json', 'r') as f:
        return json.load(f)["acess_token"]

def acess_token_secret():
    with open('servdirectvars.json', 'r') as f:
        return json.load(f)["acess_token_secret"]

def update_consumer_key(key):
    print(key)
    with open("servdirectvars.json", "r+") as f:
        data = json.load(f)
        data["consumer_key"] = key
        f.seek(0)
        json.dump(data, f)
        f.truncate()

def update_consumer_secret(key):
    with open("servdirectvars.json", "r+") as f:
        data = json.load(f)
        data["consumer_secret"] = key
        f.seek(0)
        json.dump(data, f)
        f.truncate()

def update_acess_token(key):
    with open("servdirectvars.json", "r+") as f:
        data = json.load(f)
        data["acess_token"] = key
        f.seek(0)
        json.dump(data, f)
        f.truncate()

def update_acess_token_secret(key):
    with open("servdirectvars.json", "r+") as f:
        data = json.load(f)
        data["acess_token_secret"] = key
        f.seek(0)
        json.dump(data, f)
        f.truncate()

def sql_user():
    with open('servdirectvars.json', 'r') as f:
        return json.load(f)["sqluser"]

def sql_pswd():
    with open('servdirectvars.json', 'r') as f:
        return json.load(f)["sqlpswd"]


def update_sql_user(user):
    with open("servdirectvars.json", "r+") as f:
        data = json.load(f)
        data["sqluser"] = user
        f.seek(0)
        json.dump(data, f)
        f.truncate()

def update_sql_pswd(pswd):
    with open("servdirectvars.json", "r+") as f:
        data = json.load(f)
        data["sqlpswd"] = pswd
        f.seek(0)
        json.dump(data, f)
        f.truncate()
