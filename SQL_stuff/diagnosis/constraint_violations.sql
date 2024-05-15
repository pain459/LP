SELECT
    name AS CheckConstraint,
    definition AS CheckConstraintDefinition
FROM
    sys.check_constraints
WHERE
    parent_object_id = OBJECT_ID('YourTableName');
