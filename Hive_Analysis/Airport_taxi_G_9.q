add file ${INPUT}/Script/findairport.py;

--DROP TABLE taxi_trips_g;
CREATE EXTERNAL TABLE IF NOT EXISTS taxi_trips_g 
( VendorID string,tpep_pickup_datetime timestamp,tpep_dropoff_datetime timestamp,
 passenger_count int,  trip_distance float,pickup_longitude float,pickup_latitude float,
 RateCodeID int, store_and_fwd_flag string,dropoff_longitude float,dropoff_latitude float,
 payment_type string, fare_amount float,extra float,mta_tax float,tip_amount float,
 tolls_amount float,improvement_surcharge float,total_amount float, pickupRgn string,
 pickupRgnMain string,dropRgn string, dropRgnMain string) 
 COMMENT 'taxi_trip_data' ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' 
 LINES TERMINATED BY '\n' STORED AS TEXTFILE LOCATION '${INPUT}/Green';
 
 CREATE TABLE IF NOT EXISTS airport (
loc string,
 cnt bigint
);

INSERT OVERWRITE TABLE airport
select loc, count(*) as cnt from
(select TRANSFORM(pickup_longitude, pickup_latitude) USING 'python findairport.py' AS (loc) from taxi_trips_g) arpt
group by loc;

 drop table if exists airport_g;
 
create table airport_g ROW FORMAT DELIMITED 
FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n'
LOCATION '${OUTPUT}/airport_g' as
select loc, (arpt_cnt/ ttl_cnt)*100 percent from
(select SUM(cnt) ttl_cnt from
airport ) ttl, (select loc, sum(cnt) arpt_cnt from airport where loc = 'JFK' OR loc = 'LaGuardia' group by loc) arpt;