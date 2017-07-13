# Data Analysis - Lahman Baseball Data

## Project Overview

Analyze the Lahman Baseball Dataset using and Python libraries NumPy, Pandas, and Matplotlib than communicate interesting findings about the data.

## What do I need to install?
You will need an installation of Python, plus the following libraries:

* pandas
* numpy
* matplotlib
* csv

Installing Anaconda is recommended, which comes with all of the necessary packages, as well as IPython notebook.

## Introduction

Conduct data analysis and share findings on baseball data. 

Baseball Data - A data set containing complete batting and pitching statistics from 1871 to 2014, plus fielding statistics, standings, team stats, managerial records, post-season data, and more. This dataset contains many files, but you can choose to analyze only the one(s) you are most interested in.

## Intersting Questions to Analyze

1) Which University did All Stars attend most?

2) How has Total Salary Spend changed each Year? 

3) What is the mean Salary of All Stars VS. the mean salary of all players in 2016?

## Files
 
 * Baseball_Data-Analysis.ipynb - IPython notebook that contains the analysis and write up
 * AllstarFull.csv - List of AllStar Players
 * CollegePlaying.csv - List of Players and their Colleges
 * Salaries.csv - List of Players and their Salaries
 * Schools.csv - List of Players and their School ID's

## Licenses
Baseball Databank is a compilation of historical baseball data in a
convenient, tidy format, distributed under Open Data terms.

This work is licensed under a Creative Commons Attribution-ShareAlike
3.0 Unported License.  For details see:
http://creativecommons.org/licenses/by-sa/3.0/

Person identification and demographics data are provided by
Chadwick Baseball Bureau (http://www.chadwick-bureau.com),
from its Register of baseball personnel.

Player performance data for 1871 through 2014 is based on the
Lahman Baseball Database, version 2015-01-24, which is 
Copyright (C) 1996-2015 by Sean Lahman.


## The Lahman Baseball Database

2014 Version
Release Date: January 24, 2015

----------------------------------------------------------------------

README CONTENTS
0.1 Copyright Notice
0.2 Contact Information

1.0 Release Contents
1.1 Introduction
1.2 What's New
1.3 Acknowledgements
1.4 Using this Database
1.5 Revision History

2.0 Data Tables
2.5 All-Star table
2.15 Salaries table
2.23 Schools table
2.24 SchoolsPlayers table


----------------------------------------------------------------------

0.1 Copyright Notice & Limited Use License

This database is copyright 1996-2015 by Sean Lahman. 

This work is licensed under a Creative Commons Attribution-ShareAlike 3.0 Unported License. For details see: http://creativecommons.org/licenses/by-sa/3.0/


For licensing information or further information, contact Sean Lahman
at: seanlahman@gmail.com

----------------------------------------------------------------------

0.2 Contact Information

Web site: http://www.baseball1.com
E-Mail : seanlahman@gmail.com

If you're interested in contributing to the maintenance of this 
database or making suggestions for improvement, please consider
joining our mailinglist at:

    http://groups.yahoo.com/group/baseball-databank/

If you are interested in similar databases for other sports, please
vist the Open Source Sports website at http://OpenSourceSports.com

----------------------------------------------------------------------
1.0  Release Contents

This release of the database can be downloaded in several formats. The
contents of each version are listed below.

MS Access Versions:
      lahman2014.mdb 
      2014readme.txt 

SQL version
      lahman2043.sql
      lahman2014_tables.sql
      2014readme.txt 
	  
Comma Delimited Version:
      AllStarFull.csv
      CollegePlaying.csv
      Salaries.csv
      Schools.csv

----------------------------------------------------------------------
1.1 Introduction

This database contains pitching, hitting, and fielding statistics for
Major League Baseball from 1871 through 2014.  It includes data from
the two current leagues (American and National), the four other "major" 
leagues (American Association, Union Association, Players League, and
Federal League), and the National Association of 1871-1875. 

This database was created by Sean Lahman, who pioneered the effort to
make baseball statistics freely available to the general public. What
started as a one man effort in 1994 has grown tremendously, and now a
team of researchers have collected their efforts to make this the
largest and most accurate source for baseball statistics available
anywhere. (See Acknowledgements below for a list of the key
contributors to this project.)

None of what we have done would have been possible without the
pioneering work of Hy Turkin, S.C. Thompson, David Neft, and Pete
Palmer (among others).  All baseball fans owe a debt of gratitude
to the people who have worked so hard to build the tremendous set
of data that we have today.  Our thanks also to the many members of
the Society for American Baseball Research who have helped us over
the years.  We strongly urge you to support and join their efforts.
Please vist their website (www.sabr.org).

If you have any problems or find any errors, please let us know.  Any 
feedback is appreciated

----------------------------------------------------------------------
1.2 What's New in 2014

Player stats have been updated through 2014 season.

Removed two deprecated fields from the batting table. The G_batting and
G_old fields were rendered obsolete when we created the appearances table.
They've beenremoved from the batting table starting with this version

SchoolsPlayers has been replaced with a new table called CollegePlaying.
This reflects advances in the compilation of this data, largely led by
Ted Turocy. The old table reported college attendance for major league
players by listing a start date and end date.  The new version has a 
separate record for each year that a player attended.  This allows
us to better account for players who attended multiple colleges or
skipped a season, as well as to identify teammates.


----------------------------------------------------------------------
1.3 Acknowledgements

Much of the raw data contained in this database comes from the work of
Pete Palmer, the legendary statistician, who has had a hand in most 
of the baseball encylopedias published since 1974. He is largely 
responsible for bringing the batting, pitching, and fielding data out
of the dark ages and into the computer era.  Without him, none of this
would be possible.  For more on Pete's work, please read his own 
account at: http://sabr.org/cmsfiles/PalmerDatabaseHistory.pdf

Three people have been key contributors to the work that followed, first 
by taking the raw data and creating a relational database, and later 
by extending the database to make it more accesible to researchers.

Sean Lahman launched the Baseball Archive's website back before 
most people had heard of the world wide web.  Frustrated by the
lack of sports data available, he led the effort to build a 
baseball database that everyone could use. Baseball researchers 
everywhere owe him a debt of gratitude.  Lahman served as an associate
editor for three editions of Total Baseball and contributed to five
editions of The ESPN Baseball Encyclopedia. He has also been active in
developing databases for other sports.

The work of Sean Forman to create and maintain an online encyclopedia
at "baseball-reference.com" has been remarkable. Recognized as the 
premier online reference source, Forman's site provides an oustanding
interface to the raw data. His efforts to help streamline the database
have been extremely helpful. Most importantly, Forman has spearheaded
the effort to provide standards that enable several different baseball
databases to be used together. He was also instrumental in launching
the Baseball Databank, a forum for researchers to gather and share
their work.

Since 2001, these two Seans have led a group of researchers
who volunteered to maintain and update the database. 

Ted Turocy has done the lion's share of the work to updating the main
data tables since 2012, including significant imporvements to the
demographic data in the master table. In his role as SABR data czar,
he led the effort to document college playing stints for all
major league players. Turocy also spearheads the Chadwick Baseball
Bureau. For more details on his tools and services, visit:
http://chadwick.sourceforge.net/doc/index.html  

A handful of researchers have made substantial contributions to 
maintain this database over years. Listed alphabetically, they 
are: Derek Adair, Mike Crain, Kevin Johnson, Rod Nelson, Tom Tango,
and Paul Wendt. These folks did much of the heavy lifting, and are 
largely responsible for the improvements made since 2000.

Others who made important contributions include: Dvd Avins, 
Clifford Blau, Bill Burgess, Clem Comly, Jeff Burk, Randy Cox, 
Mitch Dickerman, Paul DuBois, Mike Emeigh, F.X. Flinn, Bill Hickman,
Jerry Hoffman, Dan Holmes, Micke Hovmoller, Peter Kreutzer, 
Danile Levine, Bruce Macleod, Ken Matinale, Michael Mavrogiannis,
Cliff Otto, Alberto Perdomo, Dave Quinn, John Rickert, Tom Ruane,
Theron Skyles, Hans Van Slooten, Michael Westbay, and Rob Wood.

Many other people have made significant contributions to the database
over the years.  The contribution of Tom Ruane's effort to the overall
quality of the underlying data has been tremendous. His work at
retrosheet.org integrates the yearly data with the day-by-day data,
creating a reference source of startling depth. It is unlikely than 
any individual has contributed as much to the field of baseball 
research in the past five years as Ruane has.

Sean Holtz helped with a major overhaul and redesign before the
2000 season. Keith Woolner was instrumental in helping turn
a huge collection of stats into a relational database in the mid-1990s.
Clifford Otto & Ted Nye also helped provide guidance to the early 
versions. Lee Sinnis, John Northey & Erik Greenwood helped supply key
pieces of data. Many others have written in with corrections and 
suggestions that made each subsequent version even better than what
preceded it. 

The work of the SABR Baseball Records Committee, led by Lyle Spatz
has been invaluable.  So has the work of Bill Carle and the SABR 
Biographical Committee. David Vincent, keeper of the Home Run Log and
other bits of hard to find info, has always been helpful. The recent
addition of colleges to player bios is the result of much research by
members of SABR's Collegiate Baseball committee.

Salary data was first supplied by Doug Pappas, who passed away during
the summer of 2004. He was the leading authority on many subjects, 
most significantly the financial history of Major League Baseball. 
We are grateful that he allowed us to include some of the data he 
compiled.  His work has been continued by the SABR Business of 
Baseball committee.  

Thanks is also due to the staff at the National Baseball Library
in Cooperstown who have been so helpful over the years, including
Tim Wiles, Jim Gates, Bruce Markusen, and the rest of the staff.  

A special debt of gratitude is owed to Dave Smith and the folks at
Retrosheet. There is no other group working so hard to compile and
share baseball data.  Their website (www.retrosheet.org) will give
you a taste of the wealth of information Dave and the gang have collected.

Thanks to all contributors great and small. What you have created is
a wonderful thing.

----------------------------------------------------------------------
1.4 Using this Database

This version of the database is available in Microsoft Access
format, SQL files or in a generic, comma delimited format. Because this is a
relational database, you will not be able to use the data in a
flat-database application. 

Please note that this is not a stand alone application.  It requires
a database application or some other application designed specifically
to interact with the database.

If you are unable to import the data directly, you should download the
database in the delimted text format.  Then use the documentation
in sections 2.1 through 2.22 of this document to import the data into
your database application. 

----------------------------------------------------------------------
1.5 Revision History

     Version      Date            Comments
       1.0      December 1992     Database ported from dBase
       1.1      May 1993          Becomes fully relational
       1.2      July 1993         Corrections made to full database
       1.21     December 1993     1993 statistics added            
       1.3      July 1994         Pre-1900 data added 
       1.31     February 1995     1994 Statistics added
       1.32     August 1995       Statistics added for other leagues
       1.4      September 1995    Fielding Data added 
       1.41     November 1995     1995 statistics added
       1.42     March 1996        HOF/All-Star tables added
       1.5-MS   October 1996      1st public release - MS Access format
       1.5-GV   October 1996      Released generic comma-delimted files
       1.6-MS   December 1996     Updated with 1996 stats, some corrections
       1.61-MS  December 1996     Corrected error in MASTER table
       1.62     February 1997     Corrected 1914-1915 batters data and updated
       2.0      February 1998     Major Revisions-added teams & managers
       2.1      October 1998      Interim release w/1998 stats
       2.2      January 1999      New release w/post-season stats & awards added
       3.0	November 1999	  Major release - fixed errors and 1999 statistics added
       4.0      May 2001	  Major release - proofed & redesigned tables
       4.5      March 2002        Updated with 2001 stats and added new biographical data
       5.0      December 2002     Major revision - new tables and data
       5.1      January 2004      Updated with 2003 data, and new pitching categories
       5.2      November 2004     Updated with 2004 season statistics.
       5.3      December 2005     Updated with 2005 season statistics.
       5.4      December 2006     Updated with 2006 season statistics.
       5.5      December 2007     Updated with 2007 season statistics.
       5.6      December 2008     Updated with 2008 season statistics.
       5.7      December 2009     Updated for 2009 and added several tables.
       5.8      December 2010     Updated with 2010 season statistics.
       5.9      December 2011     Updated for 2011 and removed obsolete tables.
       2012     December 2012     Updated with 2012 season statistics
       2013     December 2013     Updated with 2013 season statistics
       2014     December 2014     Updated with 2013 season statistics

	   

------------------------------------------------------------------------------
2.0 Data Tables

The design follows these general principles.  Each player is assigned a
unique number (playerID).  All of the information relating to that player
is tagged with his playerID.  The playerIDs are linked to names and 
birthdates in the MASTER table:

  AllStarFull - All-Star appearances
  Salaries - player salary data
  Schools - list of colleges that players attended
  CollegePlaying - list of players and the colleges they attended


This document describe each of the tables in
detail and the fields that each contains.

------------------------------------------------------------------------------
2.5  AllstarFull table

playerID       Player ID code
YearID         Year
gameNum        Game number (zero if only one All-Star game played that season)
gameID         Retrosheet ID for the game idea
teamID         Team
lgID           League
GP             1 if Played in the game
startingPos    If player was game starter, the position played

------------------------------------------------------------------------------
2.15 Salaries table

yearID         Year
teamID         Team
lgID           League
playerID       Player ID code
salary         Salary


------------------------------------------------------------------------------
2.23 Schools table
schoolID       school ID code
schoolName     school name
schoolCity     city where school is located
schoolState    state where school's city is located
schoolNick     nickname for school's baseball team


------------------------------------------------------------------------------
2.24 CollegePlaying table
playerid       Player ID code
schoolID       school ID code
year           year
