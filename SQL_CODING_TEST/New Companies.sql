-- 회사 코드, 설립자, 각 계급별 직원 수 출력
-- 회사코드를 기준으로 오름 차순하기 

-- solution
-- 각 계급별 테이블을 모두 조인하여 
-- company_code로 그룹화 한 후 
-- 회사코드를 기준으로 order 해주기

select c.company_code, c.founder, count(distinct lm.lead_manager_code), count(distinct sm.senior_manager_code), count(distinct m.manager_code), count(distinct e.employee_code) 
from Company c, Lead_Manager lm, Senior_Manager sm, Manager m, Employee e
where c.company_code = lm.company_code and lm.lead_manager_code = sm.lead_manager_code and sm.senior_manager_code = m.senior_manager_code and m.manager_code = e.manager_code 
group by c.company_code, c.founder
order by c.company_code

--company_code가 같음을 기준으로 join
-- 계급별 직원수를 출력할 때 table 주의하기 !! (Company 테이블만 쓰는 것이 아니라 개별로 다른 테이블을 참조해야함)