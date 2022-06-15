
-- city이름이 a,e,i,o,u로 끝나는 도시 찾기
-- 도시들은 중복이 없어야 함. 
SELECT DISTINCT CITY
FROM STATION
WHERE (CITY LIKE '%A' OR CITY LIKE '%E' OR CITY LIKE '%I' 
OR CITY LIKE '%O' OR CITY LIKE '%U')