# 2016 Lahman Baseball Database for PostgreSQL

## Background

This repo stores the PostgreSQL schema for the 2016 Version of Lahman's Baseball Database, originally published for MySQL.

I have uploaded the CSV files as a courtesy here because the GIDP column in the PitchingPost table is set up to be an integer, but the raw CSV data hosted on Sean Lahman's website tabulated some GIDP values as floats (e.g. 0.0, 1.0, 2.0). Also fixed were some data irregularities noted [here](https://github.com/chadwickbureau/baseballdatabank/issues/60) and [here](https://github.com/chadwickbureau/baseballdatabank/issues/58), but not all of them--the majority are in the Master.csv file (please see below Importing section for more details), related to last names like "O'\*", and remain unfixed (for now).

## Importing

1. Download the files in this repo
2. Create a database in PostgreSQL
3. Import the schema file into the database via the command line ($ psql [database_name] < lahman_2016_schema.sql)
4. Update the lahman_2016_import.csv file to include the filepath of the .csv files in the csv folder.
5. Import the CSV files into the database via the command line ($ psql [database_name] < lahman_2016_import.sql)

You can find the source of the CSV files hosted on [Sean Lahman's website](http://www.seanlahman.com/baseball-archive/statistics). There are also ongoing updates to the files made by Ted Turocy on Github [here](https://github.com/chadwickbureau/baseballdatabank).

As mentioned in the background, there is some erroneous data owing to an issue with the script used to generate the data. I will be keeping an eye on the repo and updating the data as fixes come in.

## Acknowledgements

[Kris Eberwein](https://github.com/keberwein/Postgres_Lahman_Baseball) and [Brett Nycum](https://github.com/brentnycum/lahman-postgres) for their very resourceful repos I discovered when searching for PostgreSQL implementations of Lahman's Baseball Database.

## Copyright Notice & Limited Use License

Baseball Databank is a compilation of historical baseball data in a convenient, tidy format, distributed under Open Data terms.

This work is licensed under a Creative Commons Attribution-ShareAlike 3.0 Unported License.  For details see: http://creativecommons.org/licenses/by-sa/3.0/

Person identification and demographics data are provided by Chadwick Baseball Bureau (http://www.chadwick-bureau.com), from its Register of baseball personnel.

Player performance data for 1871 through 2016 is based on the Lahman Baseball Database, version 2017-02-26, which is  Copyright (C) 1996-2017 by Sean Lahman.

The tables Parks.csv and HomeGames.csv are based on the game logs and park code table published by Retrosheet.

This information is available free of charge from and is copyrighted by Retrosheet.  Interested parties may contact Retrosheet at  http://www.retrosheet.org.
