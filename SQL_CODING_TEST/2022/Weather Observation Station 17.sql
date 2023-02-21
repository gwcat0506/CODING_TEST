-- Weather Observation Station 15와 거의 유사한 문제 

-- lat_n이 38.7780보다 큰 lat_n에 대해 가장 작은 long_w 출력하기 
-- 소숫접 4자리 까지 반올림 핮기 

select round(long_w,4)
from station
where lat_n > 38.7780
order by lat_n 
limit 1
