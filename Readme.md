**Important Notes**

1.There can be multiple reason for no data generation for the date:-
a.) website is not responding.
b.) Internet connection has problem
c.) This day was holiday.
d.) Data for this day is not generated yet.

2. only zip files data is handled in the code which is for this specific website.

3. If files are already present for one date and the same request is sent again then the old data only will be replaced.

4. After the code runs successfully the output is also stored in the same directory where the zip files are stored.

5. Final excel name is final_data.xlsx.

***************
How to run
***************
a.) It requires python installed in the system with the following modules:-
1. datetime
2. os
3. requests
4. pandas

b.) Run through terminal with command:
python stock_data.py

**************************************************************
Code is written in python3.8, tested in python 3.6 as well,
Should work in older versions.
**************************************************************
