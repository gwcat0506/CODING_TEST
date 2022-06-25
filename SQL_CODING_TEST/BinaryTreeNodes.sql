-- 나에게 꽤나 어려웠던 문제,,
-- BST 테이블에서 P 컬럼은 부모의 노드를 나타내는데
-- 그래서 우선 P가 null인 것은 Root 노드 밖에 없으니 첫 번째 케이스 문으로 처리해주고
-- P컬럼에서 Root 노드를 제외한 컬럼을 distinct 후에 Inner로 처리해주고
-- 나머지 친구들을 Leaf 노드로 처리해주면 된다.
-- 푸니깐 또 별거 없네,, CASE문을 활용한 문제가 많이 나와서 CASE문을 따로 공부해야겠다 !!


-- 그리고 NULL을 비교할 땐 if null이 아닌 IS NULL 이라는 것 꼭 기억하기 !!
SELECT N,
    CASE
        WHEN P IS NULL THEN 'Root'
        WHEN N IN (SELECT DISTINCT P FROM BST) THEN 'Inner'
        ELSE 'Leaf'
    END
FROM BST
ORDER BY N;