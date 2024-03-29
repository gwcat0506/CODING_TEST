-- https://school.programmers.co.kr/learn/courses/30/lessons/131537
-- 어렵군
-- 코드를 입력하세요
SELECT DATE_FORMAT(T.SALES_DATE,'%Y-%m-%d') AS SALES_DATE, T.PRODUCT_ID, T.USER_ID, T.SALES_AMOUNT
FROM(SELECT SALES_DATE, PRODUCT_ID, USER_ID, SALES_AMOUNT
    FROM ONLINE_SALE 
    UNION ALL 
    SELECT SALES_DATE, PRODUCT_ID, NULL, SALES_AMOUNT
    FROM OFFLINE_SALE ) AS T
WHERE DATE_FORMAT(T.SALES_DATE,'%Y-%m')='2022-03'
ORDER BY SALES_DATE ASC, PRODUCT_ID ASC, USER_ID ASC