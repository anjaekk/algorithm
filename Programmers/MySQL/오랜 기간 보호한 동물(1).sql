-- 분류: JOIN
-- 단계: Level 3

SELECT
    ai.NAME,
    ai.DATETIME
FROM
    ANIMAL_INS ai
    left outer join ANIMAL_OUTS ao on ai.ANIMAL_ID = ao.ANIMAL_ID
where
    ao.SEX_UPON_OUTCOME is null
ORDER BY ai.DATETIME
LIMIT 3;
