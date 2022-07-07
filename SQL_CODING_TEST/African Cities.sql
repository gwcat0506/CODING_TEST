
-- Given the CITY and COUNTRY tables, query the names of all cities where the CONTINENT is 'Africa'.

-- Note: CITY.CountryCode and COUNTRY.Code are matching key columns.

-- city와 country 테이블을 조인해준다. 
-- country에서 continent컬럼이 Africa인 조건을 걸어주고
-- city의 name만 출력해준다. -> country의 name이 안 되는 이유?
select city.name
from city
join country on city.countrycode = country.code
where country.continent = 'Africa'
