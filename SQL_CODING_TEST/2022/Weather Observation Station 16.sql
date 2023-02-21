-- Weather Observation Station 15와 거의 유사한 문제 

-- lat_n이 137.2345보다 작은 lat_n에 대한 가장 작은 long_w 출력하기 
-- 소숫접 4자리 까지 반올림 핮기 

select round(lat_n,4)
from station
where lat_n > 38.7780
order by lat_n 
limit 1

-- 137.2345보다 작은 lat_n 뽑아서
-- 정렬되지 않은 상태이기 때문에 lat_n을 
-- 가장 작은 수 -> 큰 수 로 정렬해준다.(asc 오름차순 정렬)
-- 그 중에 limit 1을 통해서 첫 째줄만 뽑으면 가장 작은 lat_n 만 출력되게 된다.
