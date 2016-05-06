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
 
drop table if exists payment_y;

create table payment_y ROW FORMAT DELIMITED 
FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n'
LOCATION '${OUTPUT}/payment_y' 
as select yr, credit/cnt*100 credit_p, cash/cnt*100 cash_p from
(select yr, SUM(if (pay_type = 'Credit', 1, 0)) credit,
 SUM(if (pay_type = 'Cash', 1, 0)) cash, count(*) cnt from
(select year(tpep_pickup_datetime) yr, CASE WHEN payment_type = '1' OR payment_type = 'CRD' THEN 'Credit'
WHEN payment_type = '2' OR payment_type = 'CSH' THEN 'Cash'
else 'Other' END as pay_type
from taxi_trips_y where payment_type is not null and payment_type <> '') pay
group by yr) a
order by yr desc;