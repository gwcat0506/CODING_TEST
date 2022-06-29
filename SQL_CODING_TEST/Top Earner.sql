-- 전체 직원의 최대 총 수입과, 최대 총 수입의 직원 수 
-- select 절에서 months*salary를 earning이라는 별칭으로 지정해주고
-- 지정해준 별칭으로 그룹화 해주고 정렬화 해준다.
-- limit 1으로 첫째줄만 출력해준다.

-- tip select 절에서 생성된 별칭은 group by와 order by에서 쓰일 수 있다 !
-- limit를 통해서 원하는 줄 수 만큼 출력할 수 있다. 


select (months*salary) as earning, count(*)
from employee
group by earning
order by earning desc limit 1;