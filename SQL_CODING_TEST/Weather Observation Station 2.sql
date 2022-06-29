-- LAT_N의 합계와 LONG_W의 합계를 각각 반올림하여 출력하시오
-- 둘다 소숫점 둘째자리까지 반올림하기


SELECT ROUND(SUM(LAT_N),2), ROUND(SUM(LONG_W),2)
FROM STATION ;