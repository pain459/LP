SELECT
    fk.name AS ForeignKey,
    tp.name AS ParentTable,
    tr.name AS ReferencedTable,
    tpc.name AS ParentColumn,
    trc.name AS ReferencedColumn
FROM
    sys.foreign_keys AS fk
    INNER JOIN sys.tables AS tp
        ON fk.parent_object_id = tp.object_id
    INNER JOIN sys.tables AS tr
        ON fk.referenced_object_id = tr.object_id
    INNER JOIN sys.foreign_key_columns AS fkc
        ON fk.object_id = fkc.constraint_object_id
    INNER JOIN sys.columns AS tpc
        ON fkc.parent_column_id = tpc.column_id
        AND fkc.parent_object_id = tpc.object_id
    INNER JOIN sys.columns AS trc
        ON fkc.referenced_column_id = trc.column_id
        AND fkc.referenced_object_id = trc.object_id;
