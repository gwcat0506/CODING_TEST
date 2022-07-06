-- City, Country 테이블에서 모든 도시의 인구의 합계를 구하라
-- Continent = 'Asia'


-- city와 country를 countrycode를 통해서 join 해준다.
-- JOIN ON 이용하기 
SELECT SUM(CITY.POPULATION)
FROM CITY
JOIN COUNTRY ON COUNTRY.Code = CITY.CountryCode
WHERE COUNTRY.CONTINENT = 'Asia'