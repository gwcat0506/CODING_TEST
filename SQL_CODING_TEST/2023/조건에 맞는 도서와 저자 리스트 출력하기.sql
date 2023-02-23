-- https://school.programmers.co.kr/learn/courses/30/lessons/144854

SELECT BOOK_ID, AUTHOR_NAME, DATE_FORMAT(PUBLISHED_DATE,'%Y-%m-%d') AS PUBLISHED_DATE 
FROM BOOK NATURAL JOIN AUTHOR 
WHERE CATEGORY='경제'
ORDER BY PUBLISHED_DATE ASC

-- natural join은 컬럼의 이름이 같을 때만 가능하다(on절 없음)