create database hadooptest;

use hadooptest;
create table employees(
	first_name varchar(10) primary key,
	dept varchar(15),
	salary int,
	start_date date
);


describe employees;