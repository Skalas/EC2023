create table flights(
    year int,
    month int,
    day int,
    dep_time int,
    sched_dep_time int,
    dep_delay int,
    arr_time int,
    sched_arr_time int,
    arr_delay int,
    carrier varchar(80),
    flight int,
    tailnum varchar(80),
    origin varchar(80),
    dest varchar(80),
    air_time int,
    distance int,
    hour int,
    minute int,
    time_hour timestamp
);
COPY flights
FROM '/data/flights.csv' 
DELIMITER ',' 
CSV HEADER
NULL as 'NA';
create table users (id serial Primary key, name varchar, lastname varchar, age integer);
insert into users (name, lastname,age) values ('Miguel', 'Escalante', '32');
