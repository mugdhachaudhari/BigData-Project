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
 
CREATE TABLE IF NOT EXISTS hrRgnCnt (
 hr int,
 pickupRgn string,
 cnt bigint
);

INSERT OVERWRITE TABLE hrRgnCnt
select hr, pickupRgn, count(*) as cnt from
(select CAST(hour(tpep_pickup_datetime) as int) hr, pickupRgn from taxi_trips_g where pickupRgn <> 'UNKNOWN' ) hr_rgn
group by hr, pickupRgn;


 drop table if exists high_densty_rgn_g; 
 
create table high_densty_rgn_g ROW FORMAT DELIMITED 
FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n'
LOCATION '${OUTPUT}/HighDensityRgn_g' as
 select pickupRgn, count(1) as cnt from
(select hr, pickupRgn, ttl_cnt from
(select hr_avg.hr, hr_avg.pickupRgn, hr_avg.cnt as ttl_cnt, avg.hr_av as avg_cnt from
hrRgnCnt hr_avg JOIN 
(select hr, avg(cnt) hr_av from
hrRgnCnt hr_avg
group by hr) avg
ON (hr_avg.hr = avg.hr)) cmp_avg
where ttl_cnt > avg_cnt) final
group by pickupRgn having count(1) > 20;


