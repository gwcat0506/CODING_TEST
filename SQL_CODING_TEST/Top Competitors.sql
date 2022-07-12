-- 코딩테스트 중 만점을 2번 이상 받은 참가자의 hacker_id와 name
-- 만점의 갯수만큼 정렬해주고 갯수가 같을 경우 hacker_id로 정렬 


select h.hacker_id, h.name
from submissions s
inner join challenges c on c.challenge_id = s.challenge_id
inner join difficulty d on d.difficulty_level = c.difficulty_level
inner join hackers h on h.hacker_id = s.hacker_id
where c.difficulty_level = d.difficulty_level and s.score = d.score
group by h.hacker_id, h.name
having count(h.hacker_id)>1
order by count(h.hacker_id) desc, h.hacker_id ;