-- 분류: GROUP BY
-- 단계: Level 2

SElECT ANIMAL_TYPE, COUNT(ANIMAL_TYPE) AS count FROM ANIMAL_INS GROUP BY ANIMAL_TYPE ORDER BY ANIMAL_TYPE;
