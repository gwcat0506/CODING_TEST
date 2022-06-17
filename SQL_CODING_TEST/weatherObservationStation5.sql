
-- city에서 가장 짧은 이름과 긴 이름 출력하기 

-- 가장 짧은 이름
SELECT city, LENGTH(city)
FROM station
ORDER BY length(city), city limit 1;
-- 가장 긴 이름
SELECT city, LENGTH(city)
FROM station
ORDER BY length(city) desc, city limit 1;

-- order by 에서 길이로 정렬 -> 도시이름(city)로 정렬해주면
-- asc(오름차순) 자동정렬되고 limit 1을 통해 행이 하나만 출력 되면서
--  가장 짧은 길이의 도시이름을 구할 수 있다.

-- 그 반대는 desc만 추가해주면 된다.

-- 여기서 중요한 부분은 order by 에서 정렬 기준을 두 가지를 쓴 것이다 length(city)와 city 
