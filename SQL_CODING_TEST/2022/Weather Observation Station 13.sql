-- STATION에서 값이 38.7880보다 크고 137.2345보다 작은 LAT_N 합계
-- 소수점 4자리까지만 출력하기


-- truncate함수를 통해서 소숫점 4번째 자리 수 까지 자를 수 있다. 
select truncate (sum(lat_n) ,4)
from station
where lat_n>38.7880 and lat_n<137.2345

-- 다른 사람들의 정답을 보니format(sum(lat_n),'#.0000')
-- 을 이용하여 푼 사람도 있었다 !! 