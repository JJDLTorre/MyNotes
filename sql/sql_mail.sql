SELECT
    email_address
FROM
    (
        SELECT
            email_address,
            ROWNUM rnum
        FROM
            (
                SELECT
                    *
                FROM
                    Some_table
                ORDER BY
                    email_address
            )
    )
WHERE
        rnum >= 0
    AND rnum < 1000
;


