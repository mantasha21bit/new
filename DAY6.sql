USE empdb;
CREATE TABLE emp2(
       id int,
       Ename varchar(255),
       adres varchar(255),
       age int,
       sal int
	);
    
INSERT INTO emp2 VALUES (2, 'TOFU','DELHI',21 , 17000),
         (3,'GOFU' ,'HYDERABAD' ,31, 18000),
         (4, 'SUFO' ,'KOLKATA',41, 30000),
         (8, 'MUFO' ,'KOLKATA',42, 20000),
         (5, 'ZUFO' ,'KOLKATA',41, 60000),
         (11, 'PUFO' ,'KOLKATA',31, 40000),
         (9, 'DUFO' ,'KOLKATA',22, 10000),
         (7, 'YUFO' ,'KOLKATA',24, 20000);

select * from emp2;

START TRANSACTION;

INSERT INTO emp2 VALUES ( 12, 'TOFU','DELHI',27 , 37000);
savepoint SP1;
INSERT INTO emp2 VALUES ( 14, 'MOFU','DELHI',37 , 57000);
savepoint SP2;
INSERT INTO emp2 VALUES ( 18, 'LOFU','DELHI',29 , 47000);
savepoint SP3;
rollback TO SP2;
release savepoint SP2;

