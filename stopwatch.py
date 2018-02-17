#!/usr/bin/python2
"""
Simple stopwatch, state is saved to SQLite database.
Usage: ./stopwatch.py [optional: start/stop]

Without params: Counts down and displays time when the state is equal to "running"
start: Start stopwatch, each time the script is executed substract 1 second
stop: Stop stopwatch, reset time to default (5400 seconds)
"""

import argparse
import re
import sys
import sqlite3
from os.path import abspath,dirname

# Shorthand functions
def select(sql,params=()):
    cursor = db.cursor()
    cursor.execute(sql,params)
    return cursor.fetchall()

def insert(sql,params=()):
    cursor = db.cursor()
    cursor.execute(sql,params)
    db.commit()

# Setup + connect to database
create_script="""
CREATE TABLE IF NOT EXISTS game_settings (game_time_seconds INTEGER);
CREATE TABLE IF NOT EXISTS game_state (state VARCHAR255,game_time_seconds INTEGER);
"""
cdir = abspath(dirname(__file__))
database = "%s/data/stopwatch.sqlite" % cdir
db = sqlite3.connect(database)
cursor = db.cursor()
for line in create_script.strip().split("\n"):
    insert(line)

## Setup > default settings
if len(select("SELECT * FROM game_settings")) == 0:
    insert("INSERT INTO game_settings(game_time_seconds) VALUES(?)",(5400,)) # default 90 minutes time

## Setup > default state
if len(select("SELECT * FROM game_state")) == 0:
    insert("INSERT INTO game_state(state,game_time_seconds) VALUES(?,?)",('stopped',5400)) # default 90 minutes time


# Load data
rows = select("SELECT * FROM game_settings")
for row in rows:
    gametime = int(row[0])

rows = select("SELECT * FROM game_state")
for row in rows:
    state = row[0]
    seconds_left = int(row[1])

# Print for testing
#print("settings_seconds: %d" % gametime)
#print("state: %s" % state)
#print("seconds_left: %d" % seconds_left)

if state == "running" and seconds_left != 0:
    m, s = divmod(seconds_left, 60)
    h, m = divmod(m, 60)
    print "%d:%02d:%02d" % (h, m, s)
    seconds_left -= 1
    insert("UPDATE game_state set game_time_seconds = ?",(seconds_left,))

if len(sys.argv) == 2:
    cmd = sys.argv[1]
    if cmd == "start":
        insert("UPDATE game_state set state = ?",("running",))
    if cmd == "stop":
        insert("UPDATE game_state set state=?, game_time_seconds = ?",("stopped",gametime))

# Disconnect database
cursor.close()
db.close()
