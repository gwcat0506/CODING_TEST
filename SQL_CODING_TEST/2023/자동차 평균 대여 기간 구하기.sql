-- mysql 
-- https://school.programmers.co.kr/learn/courses/30/lessons/157342?language=mysql

SELECT car_id, ROUND(AVG(DATEDIFF(end_date, start_date)+1), 1) AS AVERAGE_DURATION
FROM car_rental_company_rental_history
GROUP BY car_id
HAVING AVERAGE_DURATION > 7
ORDER BY AVERAGE_DURATION DESC, car_id DESC

-- datediff 함수를 사용하여 날짜 빼기