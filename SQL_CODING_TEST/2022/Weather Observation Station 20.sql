-- 정말 어려웠던 문제... 
-- lat_n의 median을 소숫점 4번째 자리 수에서 반올림

-- mysql에서는 median을 직접구해야 한다.....OMG!!
SET @r = 0;
SELECT ROUND(AVG(Lat_N), 4)
FROM (SELECT (@r := @r + 1) AS r, Lat_N FROM Station ORDER BY Lat_N) Temp
WHERE
    r = (SELECT CEIL(COUNT(*) / 2) FROM Station) OR
    r = (SELECT FLOOR((COUNT(*) / 2) + 1) FROM Station)

-- mysql에서는 SET함수를 통해서 변수를 설정해줄 수 있다.
-- 그리고 변수를 설정해줄 때 @를 통해서 설정해준다.
-- 변수에 값을 할당하려면=또는:=기호를 사용할 수 있다.

-- 더 어려워서 설명을 추가해야할 듯..