-- 분류: JOIN
-- 단계: Level 4

SELECT AI.ANIMAL_ID, AI.ANIMAL_TYPE, AI.NAME
FROM ANIMAL_INS AI
    JOIN ANIMAL_OUTS AO ON AI.ANIMAL_ID = AO.ANIMAL_ID
WHERE AI.SEX_UPON_INTAKE like 'Intact%' and (AO.SEX_UPON_OUTCOME like 'Spayed%' or AO.SEX_UPON_OUTCOME like 'Neutered%') 
ORDER BY AI.ANIMAL_ID;
