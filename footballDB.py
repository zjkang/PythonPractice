#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3
import sys
from types import *

def create_schemas():
    country = [u"西班牙", u"英格兰", u"德国", u"意大利", u"法国"]
    level = [u"超级", u"甲级", u"乙级"]

    country_level = []
    for c in country:
        for l in level: 
            country_level.append(c + '_' + l)

    return country_level


def create_table_team(dbname, teamTable):
    con = sqlite3.connect(dbname)

    with con:
        cursor = con.cursor()
        cursor.execute("DROP TABLE IF EXISTS " + teamTable)
        statement = "CREATE TABLE " + teamTable + "(id INTEGER PRIMARY KEY AUTOINCREMENT, " + \
                    "name TEXT, country TEXT, level TEXT)"
        cursor.execute(statement)

def create_table_match(dbname, matchTable):
    con = sqlite3.connect(dbname)

    with con:
        cursor = con.cursor()
        cursor.execute("DROP TABLE IF EXISTS " + matchTable)
        statement = "CREATE TABLE " + matchTable + "(id INTEGER PRIMARY KEY AUTOINCREMENT, " + \
                    "match_name TEXT, home_id INTEGER, guest_id INTEGER, " + \
                    "home_score INTEGER, guest_score INTEGER, date TEXT)"
        cursor.execute(statement)

def create_table_odd(dbname, oddTable):
    con = sqlite3.connect(dbname)

    with con:
        cursor = con.cursor()
        cursor.execute("DROP TABLE IF EXISTS " + oddTable)
        statement = "CREATE TABLE " + oddTable + "(id INTEGER PRIMARY KEY AUTOINCREMENT, " + \
                    "match_id , home_id INTEGER, guest_id INTEGER, " + \
                    "home_score INTEGER, guest_score INTEGER, date TEXT)"
        print statement
        cursor.execute(statement)


def insert_table_team(dbname, teamTable):
    teams = [(u"巴萨罗那",   u"西班牙", u"甲级"),
             (u"皇家马德里", u"西班牙", u"甲级"),
             (u"马德里竞技", u"西班牙", u"甲级"),
             (u"瓦伦西亚",   u"西班牙", u"甲级"),
             (u"曼联",      u"英格兰",  u"超级"),
             (u"曼城",      u"英格兰",  u"超级"),
             (u"拜仁慕尼黑", u"德国",   u"甲级"),
             (u"多特蒙德",   u"德国",   u"甲级")]

    con = sqlite3.connect(dbname)

    with con:
        cur = con.cursor()
        cur.executemany("INSERT INTO " + teamTable + "(name, country, level) VALUES(?, ?, ?)", teams)

def insert_table_match(dbname, teamTable, matchTable):
    matches = [(u"西甲", u"巴萨罗那",    u"皇家马德里", 2, 1, "2016-10-02T03:00:00"),
               (u"西甲", u"马德里竞技",  u"瓦伦西亚",   3, 0, "2016-10-03T05:00:00"),
               (u"英超", u"曼联",       u"曼城",       1, 1, "2016-10-05T05:00:00"),
               (u"欧冠", u"拜仁慕尼黑",  u"多特蒙德",   3, 2, "2016-10-07T05:20:00"),
               (u"德甲", u"拜仁慕尼黑",  u"多特蒙德",   0, 2, "2016-10-10T20:20:00")]

    matchesId = []
    con = sqlite3.connect(dbname)

    with con:
        cur = con.cursor()

        for match in matches:
            # print match[1].encode('utf8'), match[2].encode('utf8')
            cur.execute("SELECT id, name FROM " + teamTable + " WHERE name = ?", (match[1],))
            home = cur.fetchone()
            cur.execute("SELECT id, name FROM " + teamTable + " WHERE name = ?", (match[2],))
            guest = cur.fetchone()

            matchesId.append((match[0], home[0], guest[0], match[3], match[4], match[5]))
        # print matchesId

        cur.executemany("INSERT INTO " + matchTable + "(match_name, home_id, guest_id, home_score, guest_score, date) \
                         VALUES(?, ?, ?, ?, ?, ?)", matchesId)

def select_teams_by_country(teamTable, country):
    con = sqlite3.connect(dbname)

    with con:
        cursor = con.cursor()
        statement = "SELECT id, name, country, level FROM " + teamTable + \
                    " WHERE country = ? "
        rows = cursor.execute(statement, (country,))
        return rows

def select_all_matches(teamTable, matchTable):
    con = sqlite3.connect(dbname)

    with con:
        cursor = con.cursor()
        statement = "SELECT M.id, M.match_name, T1.name AS home_name, T2.name AS guest_name, " \
                     "M.home_score, M.guest_score, M.date " \
                     "FROM " + matchTable + " as M " \
                     "LEFT JOIN " + teamTable + " as T1 on M.home_id = T1.id " \
                     "LEFT JOIN " + teamTable + " as T2 on M.guest_id = T2.id"
        print statement
        rows = cursor.execute(statement)
        return rows






# def create_table_match(country_match):
#     conn = sqlite3.connect(dbname)
    
  
    
# def drop_tables(dbname):
#     conn = sqlite3.connect(dbname)
#     cursor = conn.cursor()
#     cursor.execute('drop table ' + country)
#     conn.commit()
#     cursor.close()
#     conn.close()

# def insert(teams, country):
#     # users = (u'腾讯qq', 'qq@example.com')
#     # conn = sqlite3.connect(dbname)
#     # cursor = conn.cursor()
#     # cursor.execute("insert into userinfo(name, email) values(?, ?)", users)
#     # conn.commit()
#     # cursor.close()
#     # conn.close()

#     conn = sqlite3.connect(dbname)
#     cursor = conn.cursor()

#     for team in teams:
#         sql = 'insert into ' + country + '(id, name) values(?, ?)'
#         cursor.execute(sql, team)

#     conn.commit()
#     cursor.close()
#     conn.close()
    # teams = [(1, u'皇家马德里'), (2, u'巴萨罗那')]
    
# def select(text):
#     conn = sqlite3.connect(dbname)
#     cursor = conn.cursor()
#     print "select name from userinfo where email='%s'" % text
#     rows = cursor.execute("select * from userinfo where email= ? ", (text,))
#     print rows
#     for row in rows:
#         print row[0].encode('utf8'), row[1]

if __name__ == '__main__':
    dbname = 'football.db'

    teamTable = "team"
    matchTable = "match"
    oddInitialTable = "oddInitial"
    oddBeforeTable = "oddBefore"
    oddAfterTable = "oddAfter"

    create_table_team(dbname, teamTable)
    insert_table_team(dbname, teamTable)

    create_table_match(dbname, matchTable)
    insert_table_match(dbname, teamTable, matchTable)


    # select teams by country 
    # country = u"西班牙"
    # rows = select_teams_by_country(teamTable, country)
    # for row in rows:
    #     # print row[0], row[1].encode('utf8'), row[2].encode('utf8'), row[3].encode('utf8')
    #     print row

    # test = u"德国"
    # print test.encode('utf8')

    rows = select_all_matches(teamTable, matchTable)
    for row in rows:
        result = [r if type(r) is IntType else r.encode('utf8') for r in row]
        # print result
        for r in result:
            print r,
        print


    # select match by date

    # select match





    # try:
    #     drop_tables(dbname)
    # except:
    #     pass
    # create_tables(dbname)
    # insert(teams, country)
    # select("qq@example.com")
    # drop_tables(dbname)