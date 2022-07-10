-- city와 country 테이블이 있다. 
-- city.countrycode = country.code 일 때

-- continent 별로 population의 평균을 구하시오
-- 평균은 소숫점 내림으로 출력한다. -> floor() 이용

select ct.continent, FLOOR(sum(c.population)/count(c.population)) as avg
from city c, country ct
where c.countrycode = ct.code
group by ct.continent

-- equi-join을 join 명령어를 사용하지 않고 where절에서 동등 조건을 통해 구현하였다.
-- 소숫점 내림은 floor()을 이용했다. 