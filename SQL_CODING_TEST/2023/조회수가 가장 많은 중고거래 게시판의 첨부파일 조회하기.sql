-- oracle
-- https://school.programmers.co.kr/learn/courses/30/lessons/164671

SELECT '/home/grep/src/' || A.BOARD_ID || '/' || B.FILE_ID || B.FILE_NAME || B.FILE_EXT AS FILE_PATH
  FROM ( 
         SELECT A.BOARD_ID
                ,DENSE_RANK() OVER (ORDER BY A.VIEWS DESC) AS RN
                ,A.VIEWS
           FROM USED_GOODS_BOARD A
        ) A
        , USED_GOODS_FILE B
 WHERE A.BOARD_ID = B.BOARD_ID
   AND A.RN = 1
 ORDER BY B.FILE_ID DESC