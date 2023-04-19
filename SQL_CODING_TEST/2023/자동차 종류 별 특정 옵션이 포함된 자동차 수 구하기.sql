-- oracle
-- https://school.programmers.co.kr/learn/courses/30/lessons/151137


SELECT CAR_TYPE, COUNT(CAR_TYPE) AS CARS
FROM CAR_RENTAL_COMPANY_CAR
WHERE OPTIONS LIKE '%열선시트%' OR OPTIONS LIKE '%통풍시트%' OR OPTIONS LIKE '%가죽시트%'
GROUP BY CAR_TYPE
ORDER BY CAR_TYPE ASC

-- like를 사용해 문자열 비교를 할 수 있다.