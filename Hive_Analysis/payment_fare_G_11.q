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
 
drop table if exists payment_fare_g;

create table payment_fare_g ROW FORMAT DELIMITED 
FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n'
LOCATION '${OUTPUT}/payment_fare_g' 
as select fare_rng, credit/cnt*100 credit_p, cash/cnt*100 cash_p from
(select fare_rng, 
SUM(if (pay_type = 'Credit', 1, 0)) credit,
SUM(if (pay_type = 'Cash', 1, 0)) cash,
count(*) cnt
from
(select CASE WHEN fare_amount > 0 and fare_amount <= 10 THEN '0-10'
WHEN fare_amount > 10 and fare_amount <= 20 THEN '10-20'
WHEN fare_amount > 20 and fare_amount <= 30 THEN '20-30'
WHEN fare_amount > 30 and fare_amount <= 40 THEN '30-40'
WHEN fare_amount > 40 and fare_amount <= 50 THEN '40-50'
WHEN fare_amount > 50 and fare_amount <= 60 THEN '50-60'
WHEN fare_amount > 60 and fare_amount <= 70 THEN '60-70'
WHEN fare_amount > 70 and fare_amount <= 80 THEN '70-80'
WHEN fare_amount > 80 and fare_amount <= 90 THEN '80-90'
WHEN fare_amount > 90 THEN '90-'
else fare_amount END as fare_rng,
CASE WHEN payment_type = '1' OR payment_type = 'CRD' THEN 'Credit'
WHEN payment_type = '2' OR payment_type = 'CSH' THEN 'Cash'
else payment_type END as pay_type
from taxi_trips_g where  
payment_type IN ('1', '2', 'CSH', 'CRD') and fare_amount > 0) pay
group by fare_rng) a
order by fare_rng;