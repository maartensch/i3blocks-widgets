#!/usr/bin/python2
"""
Simple stopwatch, state is saved to SQLite database.
Usage: ./stopwatch.py [optional: start/stop]

Without params: Counts down and displays time when the state is equal to "running"
start: Start stopwatch, each time the script is executed substract 1 second
stop: Stop stopwatch, reset time to default (5400 seconds)
"""

import os
import sys
import sqlite3
from os.path import abspath,dirname,isfile

db = None
default_time_seconds = 5400
cdir = abspath(dirname(__file__))
runfile = "%s/data/stopwatch.running" % cdir
database = "%s/data/stopwatch.sqlite" % cdir

# Shorthand functions
def select(sql,params=()):
    cursor = db.cursor()
    cursor.execute(sql,params)
    return cursor.fetchall()

def insert(sql,params=()):
    cursor = db.cursor()
    cursor.execute(sql,params)
    db.commit()

if len(sys.argv) == 2:
    db = sqlite3.connect(database)
    cursor = db.cursor()
    cmd = sys.argv[1]
    if cmd == "start":
        insert("UPDATE game_state set game_time_seconds = ?",(default_time_seconds,))
        with open(runfile,'w+') as f:
            f.write("")
        print("started")
    if cmd == "stop":
        os.remove(runfile)
        print("stopped")
    exit(0)

# Setup + connect to database
create_script="""
CREATE TABLE IF NOT EXISTS game_settings (game_time_seconds INTEGER);
CREATE TABLE IF NOT EXISTS game_state (game_time_seconds INTEGER);
"""
db = sqlite3.connect(database)
cursor = db.cursor()
for line in create_script.strip().split("\n"):
    insert(line)

## Setup > default settings
if len(select("SELECT * FROM game_settings")) == 0:
    insert("INSERT INTO game_settings(game_time_seconds) VALUES(?)",(default_time_seconds,)) # default 90 minutes time

## Setup > default state
if len(select("SELECT * FROM game_state")) == 0:
    insert("INSERT INTO game_state(game_time_seconds) VALUES(?)",(default_time_seconds,)) # default 90 minutes time


# Load data
rows = select("SELECT * FROM game_settings")
for row in rows:
    gametime = int(row[0])

rows = select("SELECT * FROM game_state")
for row in rows:
    seconds_left = int(row[0])

# Print for testing
#print("settings_seconds: %d" % gametime)
#print("state: %s" % state)
#print("seconds_left: %d" % seconds_left)

if isfile(runfile) and seconds_left != 0:
    m, s = divmod(seconds_left, 60)
    h, m = divmod(m, 60)
    print "%d:%02d:%02d" % (h, m, s)
    seconds_left -= 1
    insert("UPDATE game_state set game_time_seconds = ?",(seconds_left,))


# Disconnect database
if db is not None:
    cursor.close()
    db.close()
