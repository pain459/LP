SELECT
    dbschemas.[name] AS 'Schema',
    dbtables.[name] AS 'Table',
    dbindexes.[name] AS 'Index',
    indexstats.avg_fragmentation_in_percent
FROM
    sys.dm_db_index_physical_stats(DB_ID(), NULL, NULL, NULL, 'DETAILED') AS indexstats
    INNER JOIN sys.tables AS dbtables
        ON dbtables.[object_id] = indexstats.[object_id]
    INNER JOIN sys.schemas AS dbschemas
        ON dbtables.[schema_id] = dbschemas.[schema_id]
    INNER JOIN sys.indexes AS dbindexes
        ON dbindexes.[object_id] = indexstats.[object_id]
        AND indexstats.index_id = dbindexes.index_id
WHERE
    dbtables.[name] = 'YourTableName'
ORDER BY
    indexstats.avg_fragmentation_in_percent DESC;
