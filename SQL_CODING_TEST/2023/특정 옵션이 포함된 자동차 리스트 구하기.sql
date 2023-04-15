-- oracle

-- https://school.programmers.co.kr/learn/courses/30/lessons/157343
SELECT CAR_ID,CAR_TYPE,DAILY_FEE,OPTIONS
FROM CAR_RENTAL_COMPANY_CAR
WHERE OPTIONS LIKE '%네비게이션%'
ORDER BY CAR_ID DESC

-- LIKE를 통해 문자열이 해당 컬럼에 속해있는지 확인할 수 있다. 