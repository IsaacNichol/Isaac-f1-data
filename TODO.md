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
disallowed as not great for keeping a clean set of data.
**After some thinking this makes sense to do after the above**

**Inserting new columns**\
When added a new column i have been dropping the existing table and creating a new.
This works during trial and error build but need a way to add a new column and migrate

**Spreading out of functions**\
1 "main" file is not ideal for making changes to the API section of the program. 
Need to spread this out into different files / functions to make changes simpler\
This is done now but required some **heavy** hand holding from CHATGPT - i am going to attempt to move the database 
translations over now based on what i have learnt 