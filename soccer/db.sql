-- Create tables of Teams, Matches, Odds
-- sqlite3 soccer.db < db.sql

BEGIN TRANSACTION;

DROP TABLE IF EXISTS Teams;
CREATE TABLE Teams (
    TeamId  INTEGER PRIMARY KEY NOT NULL, 
    Name    TEXT    NOT NULL /* 球队名字 */,
    Country TEXT    NOT NULL /* 球队国家 */, 
    Level   TEXT    NOT NULL /* 球队级别 */
    );

DROP TABLE IF EXISTS Matches;
CREATE TABLE Matches (
    MatchId    INTEGER   PRIMARY KEY NOT NULL,
    DateTime   TEXT      NOT NULL /* 比赛时间 */,
    Category   TEXT      NOT NULL /* 比赛类别 */,
    HomeId     INTEGER   NOT NULL /* 主队id */,
    GuestId    INTEGER   NOT NULL /* 客队id */,
    HomeScore  INTEGER   NOT NULL /* 主队得分 */,
    GuestScore INTEGER   NOT NULL /* 客队得分 */,
    InitWin    REAL DEFAULT 0.0 /* 初始胜利赔率 */,
    InitTie    REAL DEFAULT 0.0 /* 初始平局赔率 */,
    InitLose   REAL DEFAULT 0.0 /* 初始失利赔率 */,
    BeforeWin  REAL DEFAULT 0.0 /* 比赛开始前胜利赔率 */,
    BeforeTie  REAL DEFAULT 0.0 /* 比赛开始前平局赔率 */,
    BeforeLose REAL DEFAULT 0.0 /* 比赛开始前失利赔率 */,
    AfterWin   REAL DEFAULT 0.0 /* 比赛结束后胜利赔率 */,
    AfterTie   REAL DEFAULT 0.0 /* 比赛结束后平局赔率 */,
    AfterLose  REAL DEFAULT 0.0 /* 比赛结束后失利赔率 */,
    FOREIGN KEY(HomeId)  REFERENCES Teams(TeamId),
    FOREIGN KEY(GuestId) REFERENCES Teams(TeamId)
    );

COMMIT;


