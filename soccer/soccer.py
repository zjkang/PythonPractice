#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3
import sys
from types import *

dbname = "soccer.db"

country = [u"西班牙", u"英格兰", u"德国", u"意大利"]
level = [u"超级", u"甲级", u"乙级"]

teams = [(u"巴萨罗那", u"西班牙", u"甲级"),
         (u"皇家马德里", u"西班牙", u"甲级"),
         (u"马德里竞技", u"西班牙", u"甲级"),
         (u"瓦伦西亚", u"西班牙", u"甲级"),
         #
         (u"曼联", u"英格兰", u"超级"),
         (u"曼城", u"英格兰", u"超级"),
         (u"阿森纳", u"英格兰", u"超级"),
         (u"利物浦", u"英格兰", u"超级"),
         #
         (u"拜仁慕尼黑", u"德国", u"甲级"),
         (u"多特蒙德", u"德国", u"甲级"),
         (u"不莱梅", u"德国", u"甲级"),
         (u"沃尔夫斯堡", u"德国", u"甲级"),
         #
         (u"尤文图斯", u"意大利", u"甲级"),
         (u"罗马", u"意大利", u"甲级"),
         (u"AC米兰", u"意大利", u"甲级"),
         (u"国际米兰", u"意大利", u"甲级")]

matches = [("2016-10-02T03:00:00", u"西甲", u"巴萨罗那", u"皇家马德里", 2, 1,
            1.52, 4.03, 6.12, 1.50, 4.13, 6.68, 1.51, 4.12, 6.66),
            ("2016-10-03T05:00:00", u"西甲", u"马德里竞技", u"瓦伦西亚", 3, 0, 
            2.52, 5.03, 7.12, 2.50, 5.13, 7.68, 2.51, 5.12, 7.66),
            ("2016-10-05T05:00:00", u"英超", u"曼联", u"曼城", 1, 1, 
            3.52, 6.03, 8.12, 3.50, 6.13, 8.68, 3.51, 6.12, 8.66),
            ("2016-10-07T05:20:00", u"欧冠", u"拜仁慕尼黑", u"多特蒙德", 3, 2,
            4.52, 7.03, 9.12, 4.50, 7.13, 9.68, 4.51, 7.12, 9.66),
            ("2016-10-10T20:20:00", u"德甲", u"拜仁慕尼黑", u"多特蒙德", 0, 2,
            5.52, 8.03, 10.12, 5.50, 8.13, 10.68, 5.51, 8.12, 10.66)]

def util_init_teams(dbname, teams):
    con = sqlite3.connect(dbname)

    with con:
        cur = con.cursor()
        cur.executemany("INSERT INTO Teams (Name, Country, Level) VALUES(?, ?, ?)", teams)

def util_init_matches(dbname, matches):
    matchesId = []
    con = sqlite3.connect(dbname)

    with con:
        cur = con.cursor()
        for match in matches:
            # print match[2].encode('utf8'), match[3].encode('utf8')
            cur.execute("SELECT TeamId, Name FROM Teams WHERE Name = ?", (match[2],))
            home = cur.fetchone()
            cur.execute("SELECT TeamId, Name FROM Teams WHERE Name = ?", (match[3],))
            guest = cur.fetchone()

            matchesId.append(match[0:2] + (home[0], guest[0]) + match[4:])

        cur.executemany("INSERT INTO Matches (DateTime, Category, HomeId, GuestId, HomeScore, GuestScore, \
                         InitWin, InitTie, InitLose, BeforeWin, BeforeTie, BeforeLose, AfterWin, AfterTie, AfterLose) \
                         VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", matchesId)

def select_all_matches(dbname):
    con = sqlite3.connect(dbname)

    with con:
        cursor = con.cursor()
        statement = ("SELECT M.DateTime, M.Category, T1.Name AS HomeName, T2.Name AS GuestName, "
                     "M.homeScore, M.guestScore, M.InitWin, M.initTie, M.InitLose, "
                     "M.BeforeWin, M.BeforeTie, M.BeforeLose, M.AfterWin, M.AfterTie, M.AfterLose "
                     "FROM Matches as M "
                     "LEFT JOIN Teams as T1 on M.homeId = T1.TeamId "
                     "LEFT JOIN Teams as T2 on M.guestId = T2.TeamId");
        # print statement
        rows = cursor.execute(statement)
        return rows

def select_teams_by_country(teamTable, country):
    con = sqlite3.connect(dbname)

    with con:
        cursor = con.cursor()  
        statement = "SELECT id, name, country, level FROM " + teamTable + \
                    " WHERE country = ? "
        rows = cursor.execute(statement, (country,))
        return rows

if __name__ == '__main__':
    print "test"

    # initialize
    util_init_teams(dbname, teams)
    util_init_matches(dbname, matches)

    # select from all matches
    rows = select_all_matches(dbname)
    for row in rows:
        result = [r if type(r) is IntType else r.encode('utf8') for r in row]
        # print result
        for r in result:
            print r,
        print

    # select teams by country 
    # country = u"西班牙"
    # rows = select_teams_by_country(teamTable, country)
    # for row in rows:
    #     # print row[0], row[1].encode('utf8'), row[2].encode('utf8'), row[3].encode('utf8')
    #     print row
    # test = u"德国"
    # print test.encode('utf8')
