-- oracle
-- https://school.programmers.co.kr/learn/courses/30/lessons/131529

SELECT SUBSTR(PRODUCT_CODE,0,2) AS CATEGORY, COUNT(*) AS PRODUCT 
FROM PRODUCT 
GROUP BY SUBSTR(PRODUCT_CODE,0,2) 
ORDER BY CATEGORY;
