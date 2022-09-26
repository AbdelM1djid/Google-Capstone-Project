-- unlike the rest of the data 2022_06 has a changed data type  , lets view the data 
SELECT * 
FROM "2022_06" t1 

-- the start id column is integer in ("2022_06" Data )  unlike the rest of the data , Lets convert it to VARCHAR 
ALTER TABLE t1
ALTER COLUMN 'start_station_id' VARCHAR(50);
