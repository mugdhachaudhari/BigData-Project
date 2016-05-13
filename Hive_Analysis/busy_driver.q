--DROP TABLE taxi_trips_data;
CREATE EXTERNAL TABLE IF NOT EXISTS taxi_trips_data
( medallion string,hack_license string,vendor_id string,rate_code string,store_and_fwd_flag string,pickup_datetime timestamp,dropoff_datetime timestamp,passenger_count int,trip_time_in_secs int,trip_distance float,pickup_longitude float,pickup_latitude float,dropoff_longitude float,dropoff_latitude float) 
 COMMENT 'taxi_trip_data_license' ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' 
 LINES TERMINATED BY '\n' STORED AS TEXTFILE LOCATION '${INPUT}/' tblproperties ("skip.header.line.count"="1");
 
CREATE TABLE IF NOT EXISTS shift_duration (
  hack_license string,
dt date,
shift string,
 ttl_time float
);


INSERT OVERWRITE TABLE shift_duration 
select hack_license, dt, shift, SUM(trip_time_in_secs) ttl_time from
(select hack_license, DATE(pickup_datetime) dt,
CASE WHEN  HOUR(pickup_datetime) >= 16 OR (HOUR(pickup_datetime) >= 0 AND HOUR(pickup_datetime) < 4)  THEN 'S'
WHEN  HOUR(pickup_datetime) >= 4 AND HOUR(pickup_datetime) < 16 THEN 'F'
ELSE 'O' END as shift, trip_time_in_secs from taxi_trips_data where trip_time_in_secs < 7000) a
group by hack_license, dt, shift;


drop table if exists busy_driver_s;

create table busy_driver_s ROW FORMAT DELIMITED 
FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n'
LOCATION '${OUTPUT}/busy_driver_s' 
as select hack_license, ttl_time_s  from
(select hack_license, avg(ttl_time) ttl_time_s from shift_duration where shift = 'S'
group by hack_license) c
order by ttl_time_s desc limit 30;

drop table if exists busy_driver_f;

create table busy_driver_f ROW FORMAT DELIMITED 
FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n'
LOCATION '${OUTPUT}/busy_driver_f' 
as select hack_license, ttl_time_f  from
(select hack_license, avg(ttl_time) ttl_time_f from shift_duration where shift = 'F'
group by hack_license) c
order by ttl_time_f desc limit 30;