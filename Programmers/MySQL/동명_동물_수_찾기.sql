-- 분류: GROUP BY
-- 단계: Level 2

SELECT NAME, COUNT(NAME) AS COUNT FROM ANIMAL_INS 
GROUP BY NAME HAVING COUNT>1 ORDER BY NAME ;
