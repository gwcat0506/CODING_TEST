-- district가 California인 population의 합계

select sum(population)
from city
where district = 'California';