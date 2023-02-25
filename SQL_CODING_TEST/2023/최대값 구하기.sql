-- https://school.programmers.co.kr/learn/courses/30/lessons/151136?language=mysql

SELECT floor(avg(DAILY_FEE)) as AVERAGE_FEE
FROM CAR_RENTAL_COMPANY_CAR
WHERE CAR_TYPE = 'SUV';