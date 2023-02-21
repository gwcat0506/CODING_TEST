-- lat_n이 137.2345보다 작은 가장 큰 lat_n에 대한 long_w 출력하기 
-- 소숫접 4자리 까지 반올림 핮기 


SELECT ROUND(long_w, 4)
FROM station 
WHERE lat_n < 137.2345 
ORDER BY lat_n DESC
LIMIT 1;


-- 137.2345보다 작은 lat_n 뽑아서
-- 정렬되지 않은 상태이기 때문에 lat_n으로 desc 정렬해주면
-- 가장 큰수 -> 작은수 로 정렬된다.
-- 그 중에 limit 1을 통해서 첫 째줄만 뽑으면 가장 큰 lat_n 만 출력되게 된다.
