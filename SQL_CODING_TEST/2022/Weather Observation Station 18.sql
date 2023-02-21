-- P1(a,b)와 P2(c,d)의 Manhattan Distance 구하기
-- 4번째 짜리까지 반올림
-- abs()를이용하여 구해줌 

select round(abs(min(lat_n)-max(lat_n))+abs(min(long_w)-max(long_w)),4)
from station 
