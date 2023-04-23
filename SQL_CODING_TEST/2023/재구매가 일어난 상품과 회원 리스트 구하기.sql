-- oracle
-- https://school.programmers.co.kr/learn/courses/30/lessons/131536


SELECT USER_ID,PRODUCT_ID
FROM ONLINE_SALE
GROUP BY USER_ID,PRODUCT_ID
HAVING COUNT(*) >= 2
ORDER BY USER_ID ASC, PRODUCT_ID DESC;

-- having 절에 count를 이용해서 각 group의 데이터 개수가 2개 이상일 때만 들고올 수 있다.

