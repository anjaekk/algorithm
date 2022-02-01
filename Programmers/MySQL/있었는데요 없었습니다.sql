-- 분류: JOIN
-- 단계: Level 3

SELECT
    ai.ANIMAL_ID,
    ai.NAME
FROM
    ANIMAL_INS ai
    left join ANIMAL_OUTS ao on ai.ANIMAL_ID = ao.ANIMAL_ID
WHERE
    ai.DATETIME > ao.DATETIME
ORDER BY ai.DATETIME
