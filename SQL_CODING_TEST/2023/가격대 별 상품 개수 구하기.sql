-- oracle
-- https://school.programmers.co.kr/learn/courses/30/lessons/131530


SELECT 
SUBSTR(PRICE,1,1)*10000 AS PRICE_GROUP,
COUNT(*) AS RPODUCTS
FROM PRODUCT
GROUP BY SUBSTR(PRICE,1,1)*10000
ORDER BY SUBSTR(PRICE,1,1)*10000