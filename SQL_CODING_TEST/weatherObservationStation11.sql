-- STATION으로부터 모음(a, e, i, o, u)으로 끝나는 CITY 출력

SELECT DISTINCT CITY 
FROM STATION
WHERE LEFT(CITY, 1) NOT IN ('a','e','i','o','u') AND RIGHT(CITY, 1) NOT IN ('a','e','i','o','u')

-- 정규표현식 사용
-- 정규표현식도 두 가지의 경우를 .을 통해 묶어줄 수 있다.
SELECT DISTINCT CITY
FROM STATION
WHERE CITY REGEXP '^[^AEIOU].*[^AEIOU]$'