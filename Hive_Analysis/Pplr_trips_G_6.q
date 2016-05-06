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
 
drop table if exists pplr_trips_g;

create table pplr_trips_g ROW FORMAT DELIMITED 
FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n'
LOCATION '${OUTPUT}/pplr_trips_g' 
as select pickupRgn, dropRgn, cnt from
(select pickupRgn, dropRgn, count(*) as cnt from taxi_trips_g where pickupRgn <> 'UNKNOWN' and dropRgn <> 'UNKNOWN'
group by pickupRgn, dropRgn) a
order by cnt desc
limit 30;