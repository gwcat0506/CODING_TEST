-- 전체 직원의 최대 총 수입과, 최대 총 수입의 직원 수 

select top(1) months * salary, count(months * salary)
from employee
group by months * salary
order by months * salary desc