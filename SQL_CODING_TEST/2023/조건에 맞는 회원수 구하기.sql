-- https://school.programmers.co.kr/learn/courses/30/lessons/131535

SELECT COUNT(USER_ID)
FROM USER_INFO
WHERE (DATE_FORMAT(JOINED,'%Y') = '2021') and (AGE BETWEEN 20 and 29);
