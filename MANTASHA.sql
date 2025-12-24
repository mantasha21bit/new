show databases; 
CREATE DATABASE empdb;
USE empdb;
CREATE TABLE emp(
       id int,
       name varchar(255),
       adres varchar(255)
	);
SELECT * FROM emp;

ALTER TABLE emp 
 MODIFY id INT NOT NULL;

ALTER TABLE emp 
 ADD unique (id);
 
ALTER TABLE emp 
 ADD age INT ;
 
ALTER TABLE emp 
 ADD check (age >=18);

ALTER TABLE emp 
 ALTER adres set default 'INDIA';
 
 CREATE TABLE emp1(
       id int,
       Ename varchar(255),
       adres varchar(255),
       age int
	);
 
CREATE TABLE STU(
        ID int,
        SNAME varchar(255),
        ROLL int,
       age int
	);

select * FROM STU;

INSERT INTO STU VALUES (1, 'MOFU', 11 , 18);

INSERT INTO STU VALUES (2, 'TOFU', 12 , 17),
         (3,'GOFU' ,13, 18),
         (4, 'SUFO' ,14, 16);
         
INSERT INTO STU VALUES (5, 'ZOFU', 16 , 18);

SET SQL_SAFE_UPDATES= 0;

update STU 
 SET age = 19 
 where ID =1 ;
 
 delete FROM STU WHERE ID = 5;
 
select * FROM STU;

INSERT INTO STU VALUES (12, 'TOFU', 17 , 17),
         (31,'GOFU' ,19, 18),
         (14, 'SUFO' ,24, 16);
         
SELECT SNAME, ROLL FROM STU;

SELECT distinct SNAME FROM STU;
SELECT SNAME ,ID , ROLL , AGE FROM STU WHERE ID =2;
SELECT SNAME ,ID , ROLL , AGE FROM STU WHERE AGE >= 17;
SELECT SNAME ,ID , ROLL , AGE FROM STU WHERE ID between 3 AND 20;
SELECT SNAME ,ID , ROLL , AGE FROM STU WHERE SNAME IN ('TOFU' , 'MOFU' );
SELECT SNAME ,ID , ROLL , AGE FROM STU WHERE SNAME LIKE 'T%';
SELECT SNAME ,ID , ROLL , AGE FROM STU WHERE NOT SNAME ='TOFU';
SELECT SNAME AS STUDENTS ,ID , ROLL , AGE FROM STU WHERE AGE >= 17;
SELECT SNAME ,ID , ROLL , AGE FROM STU ORDER BY AGE ;
SELECT AVG(AGE) FROM STU ;
SELECT AGE, count(*) FROM STU group by AGE;
SELECT SNAME ,ID , ROLL , AGE FROM STU WHERE AGE >= 17 LIMIT 3;


CREATE TABLE TEACH(
        ID int,
        TNAME varchar(255)
	);

INSERT INTO TEACH VALUES (2, 'TACCO'),
         (3,'MACCO' ),
         (4, 'RACCO' );

SELECT * FROM TEACH;

SELECT S.SNAME , T.TNAME FROM STU S INNER JOIN TEACH T ON S.ID = T.ID;
SELECT S.SNAME , T.TNAME FROM STU S RIGHT JOIN TEACH T ON S.ID = T.ID;
SELECT S.SNAME , T.TNAME FROM STU S LEFT JOIN TEACH T ON S.ID = T.ID;




 
 
