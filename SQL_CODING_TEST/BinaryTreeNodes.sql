--  오답 !! 다시 풀어서 제출해야됨


SELECT  N, CASE WHEN P IS NULL THEN 'Root' 
        WHEN N NOT IN (SElECT Distinct P FROM bst WHERE P IS NOT NULL) THEN 'Leaf'
               ELSE 'Inner' END
FROM BST
ORDER BY N
