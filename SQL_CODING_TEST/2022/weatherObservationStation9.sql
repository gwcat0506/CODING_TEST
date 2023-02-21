-- 모음으로 시작하지 않는 city이름 출력하기
-- 중복은 없어야 함. 

-- 포함하지 않는것은 NOT을 붙여 간단하게 해결
select distinct city 
from station
where not (city like 'A%' or city like 'E%' 
or city like 'I%' or city like 'O%' or city like 'U%');


-- 정규표현식을 사용하여 해결하기
select distinct city 
from station
where regexp_like(city,'^[^AEIOU]');
