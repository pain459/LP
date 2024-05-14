-- Disable indexes if possible
ALTER INDEX ALL ON DestinationTable DISABLE;

DECLARE @BatchSize INT = 1000;
DECLARE @Offset INT = 0;

WHILE (1=1)
BEGIN
    INSERT INTO DestinationTable (Column1, Column2, ...)
    SELECT TOP (@BatchSize) Column1, Column2, ...
    FROM SourceTable
    WHERE KeyColumn > @Offset
    ORDER BY KeyColumn;

    SET @Offset = @Offset + @BatchSize;

    IF @@ROWCOUNT < @BatchSize BREAK;
END;

-- Rebuild indexes
ALTER INDEX ALL ON DestinationTable REBUILD;
