-- 일본사람들의 populations를 모두 더하시오 

select sum(population)
from city
where countrycode = 'JPN'