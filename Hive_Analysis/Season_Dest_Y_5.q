--DROP TABLE taxi_trips_y;
CREATE EXTERNAL TABLE IF NOT EXISTS taxi_trips_y 
( VendorID string,tpep_pickup_datetime timestamp,tpep_dropoff_datetime timestamp,
 passenger_count int,  trip_distance float,pickup_longitude float,pickup_latitude float,
 RateCodeID int, store_and_fwd_flag string,dropoff_longitude float,dropoff_latitude float,
 payment_type string, fare_amount float,extra float,mta_tax float,tip_amount float,
 tolls_amount float,improvement_surcharge float,total_amount float, pickupRgn string,
 pickupRgnMain string,dropRgn string, dropRgnMain string) 
 COMMENT 'taxi_trip_data' ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' 
 LINES TERMINATED BY '\n' STORED AS TEXTFILE LOCATION '${INPUT}/Yellow';
 
drop table if exists ssn_dest_y;

create table ssn_dest_y ROW FORMAT DELIMITED 
FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n'
LOCATION '${OUTPUT}/ssn_dest_y' 
as select season, dropRgn, dropRgnMain, count(*) cnt from
(select CASE WHEN array_contains(array(3, 4, 5) ,CAST(MONTH(tpep_pickup_datetime) as int)) THEN 'Spring'
WHEN  array_contains(array(6, 7, 8) ,CAST(MONTH(tpep_pickup_datetime) as int)) THEN 'Summer'
WHEN  array_contains(array(9, 10, 11) ,CAST(MONTH(tpep_pickup_datetime) as int)) THEN 'Fall'
WHEN  array_contains(array(12, 1, 2) ,CAST(MONTH(tpep_pickup_datetime) as int)) THEN 'Winter' 
ELSE 'Wrong Season' END as season, dropRgn, dropRgnMain from taxi_trips_y where dropRgn <> 'UNKNOWN') ssn
group by season, dropRgn, dropRgnMain
order by season, cnt desc,dropRgn, dropRgnMain;