-- 모든 city들의 population의 평균 구하기
--  정수 부분을 제외하고 반올림 하기 round(x,0)

select round(sum(population)/count(population),0)
from city