-- district가 California인 population의 평균


select sum(population)/count(population) as avg
from city
where district = 'California';
