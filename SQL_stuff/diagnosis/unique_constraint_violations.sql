SELECT
    name AS UniqueConstraint
FROM
    sys.objects
WHERE
    type = 'UQ'
    AND parent_object_id = OBJECT_ID('YourTableName');
