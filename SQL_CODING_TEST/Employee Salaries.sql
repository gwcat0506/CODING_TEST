-- months가 10 이하이고
-- salary가 2000이상인 employee
-- 정렬은 employee_id로 하시오(asc)

select name
from employee
where salary > 2000 and months < 10 
order by employee_id