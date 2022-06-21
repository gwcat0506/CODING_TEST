-- 삼각형 테이블을 비교하여 
-- 세 개의 길이를 비교하여 삼각형의 종류 출력하기 
--  1. 세 변의 길이가 모두 같은 삼각형 -> Equilateral
--  2. 두 변의 길이가 같은 삼각형- > Isosceles
--  3. 세 변의 길이가 모두 다른 삼각형 -> Scalene
--  4. 세 변의 길이로 삼각형이 형성되지 않는 경우 -> 주어진 3개변의 길이로 삼각형이 형성되지 않는 경우 - Not A Triangle

-- 삼각형이 형성 되지 않으려면 A > B+C 가 되면 된다. 
-- CASE문을 활용하여 문제 풀기
-- CASE문을 쓰면 SELECT에 따로 표시를 하지 않아도 된다. 
SELECT 
CASE 
WHEN A = B AND B = C THEN 'Equilateral'
WHEN A+B <= C OR A+C <= B OR B+C <= A THEN 'Not A Triangle'
WHEN A = B OR B = C OR A = C THEN 'Isosceles'
ELSE 'Scalene' END
FROM TRIANGLES