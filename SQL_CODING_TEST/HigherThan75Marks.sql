
-- 각 이름 의 마지막 세 문자 로 출력을 정렬하십시오 . 두 명 이상의 학생 모두 이름이 
-- 마지막 세 글자로 끝나는 동일한 이름을 가지고 있는 경우(예: Bobby, Robby 등), 오름차순 ID 로 2차 정렬합니다 .


-- mysql은  left, substring, right을 이용해서 문자열을 자를 수 있다. 
SELECT NAME
FROM STUDENTS
WHERE MARKS > 75
ORDER BY RIGHT(NAME,3), ID 