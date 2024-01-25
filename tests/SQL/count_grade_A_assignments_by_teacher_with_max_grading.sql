-- Active: 1706125733796@@127.0.0.1@3306
-- Write query to find the number of grade A's given by the teacher who has graded the most assignments

SELECT count(*)
from assignments
WHERE
    teacher_id = (
        SELECT teacher_id
        FROM (
                SELECT teacher_id, COUNT(*) as cnt
                FROM assignments
                WHERE
                    teacher_id IS NOT NULL
                GROUP BY
                    teacher_id
                ORDER BY cnt DESC
                LIMIT 1
            )
    )
    AND grade = 'A';