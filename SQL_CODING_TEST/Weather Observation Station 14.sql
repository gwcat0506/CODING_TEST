-- station이 137.2345보다 작은 것중 가장 큰 수 
-- 소숫점 4번째 자리에서 버리기 ->truncate 이용!


select truncate (max(lat_n), 4 )
from station
where lat_n<137.2345