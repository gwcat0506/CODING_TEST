-- https://school.programmers.co.kr/learn/courses/30/lessons/164673?language=oracle
-- oracle 풀이

SELECT UGB.TITLE, UGB.BOARD_ID, UGR.REPLY_ID, UGR.WRITER_ID, UGR.CONTENTS, TO_CHAR(UGR.CREATED_DATE,'YYYY-MM-DD') CREATED_DATE
FROM USED_GOODS_BOARD UGB INNER JOIN USED_GOODS_REPLY UGR ON
UGB.BOARD_ID = UGR.BOARD_ID 
WHERE TO_CHAR(UGB.CREATED_DATE,'YYYY-MM') = '2022-10'
ORDER BY CREATED_DATE, UGB.TITLE;

-- tip
-- ORACLE의 날짜 함수는 TO_CHAR함수를 통해 해결할 수 있다. 
-- TABLE의 alias는 AS라는 문법없이 띄어쓰기 하면 된다.
