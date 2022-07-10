-- 꽤나 어려웠던 문제
-- Students와 Grades 테이블이 있다. 
-- Grades.Min_Mark < Students.marks < Grades.Max_Mark 범위 사이에 해당하는 grade를 찾아 ID, Marks와 함께 출력해주면 된다. 

-- 주의
-- 1. grade가 8 이하인 경우 ID를 Null로 표시해준다.
-- 2. 등급이 높은 순으로 정렬하고, 등급이 같을 경우 이름의 알파벳순으로(abcd..) 정렬한다. 

select IF(g.grade < 8, 'NULL', s.name), g.grade, s.marks
from students s inner join grades g on s.marks between g.min_mark and g.max_mark
order by g.grade desc, s.name;

-- 등급이 8이하일 때 name을 null을 출력해야 한다는 조건에서 case문을 써야하나 고민했었는데(할 순 있을 듯 BUT 길어짐), 단순하게 IF문을 이용하여 출력할 수 있었다. 

-- 알게된 것
-- 1. select에 if문 쓸 수 있다. if(조건,True일때,False일때) 
-- 2. inner join을 할 때 꼭 같다(equl) 조건으로 동일 컬럼을 찾지 않아도 된다 ! 그냥 비교하는 용도로 inner join 해도 됨.=
-- 해당 문제도 students와 grades에 같은 컬럼이 있지 않았는데, inner join의 조건으로 s.marks between g.min_mark and g.max_mark를 쓰면서 학생이 해당하는 등급을 찾을 수 있었다. 
-- 3. order by 할 때
-- order by 첫 번째 order조건 order방법, 두번째 order조건, order 방법(asc는 생략가능) 으로 표시한다. 

 