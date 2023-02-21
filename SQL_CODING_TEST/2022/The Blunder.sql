-- 모든 직원들의 평균월급을 구함
-- 그러나 사만다의 숫자 0이 고장나서 0이 없을 때와 있을 때의 오차 구하기
-- 올림해서 출력 CEIL() 사용

SELECT CEIL(AVG(salary) - AVG(replace(salary,0,'')))
FROM employees