-- P1(a,b)와 P2(c,d)의 Euclidean Distance 구하기
-- 4번째 짜리까지 반올림

-- POW 함수 활용 !
-- pow 함수는 앞의 수를 뒤의 수만큼 제곱한 값을 반환하는 함수

-- sqrt는 제곱근을 구해주는 함수
-- sqrt(pow((a-c),2)+pow((b-d),2))로 구하기 !!

-- POW와 SQRT함수 기억하기


select round(sqrt(pow(min(lat_n)-max(lat_n),2)+pow(min(long_w)-max(long_w),2)),4)
from station 
