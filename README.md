# Isaac's fun with data
I am trying to self some basic python and database interactions.
Having an interest in F1 i figured that's a great place to start in learning with readily available data that is interesting to me.


What am i trying to do? 

From the OpenF1 api's 
https://openf1.org. Call a selection of data including sessions, drivers and positions then put those into a database ( Postgres ) for analysis.

Creating 3 tables sessions, drivers and positions this should give me a good basis for doing some data analysis  

# TODO 
**Duplicate data**\
Upon working on this i have found that data is being duplicated unnecessarily 
EG circuit name across all sessions with the same circuit
Plan is to transform this data so instead of session to driver
Location -> session -> driver 
& positions / sessions -> driver

Currently, i have a 1-1 for session to driver EG Driver was in session 1 & 2 but on the drivers table so duplicating data. 
Thoughts are to have intermediate tables for these two usecases to reduce excess data


**Allowing of Duplicate**\
Currently, an exact duplicate record is allowed to be entered - this should be
disallowed as not great for keeping a clean set of data

**Inserting new columns**\
When added a new column i have been dropping the existing table and creating a new.
This works during trial and error build but need a way to add a new column and migrate

**Spreading out of functions**\
1 "main" file is not ideal for making changes to the API section of the program. 
Need to spread this out into different files / functions to make changes simpler