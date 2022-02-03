-- 분류: JOIN
-- 단계: Level 3

SELECT
    ao.ANIMAL_ID,
    ao.NAME
FROM
    ANIMAL_INS ai
    right outer join ANIMAL_OUTS ao on ai.ANIMAL_ID = ao.ANIMAL_ID
WHERE
    ai.NAME is null and ao.NAME is not null
ORDER BY ao.ANIMAL_ID;
