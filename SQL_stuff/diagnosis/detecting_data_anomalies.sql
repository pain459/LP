SELECT
    Column1, Column2, COUNT(*)
FROM
    YourTableName
GROUP BY
    Column1, Column2
HAVING
    COUNT(*) > 1;
