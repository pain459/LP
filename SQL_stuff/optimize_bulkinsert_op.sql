-- Step 1: Switch to the BULK_LOGGED recovery model
ALTER DATABASE YourDatabase SET RECOVERY BULK_LOGGED;

-- Step 2: Disable non-clustered indexes
ALTER INDEX ALL ON DestinationTable DISABLE;

-- Step 3: Disable constraints
ALTER TABLE DestinationTable NOCHECK CONSTRAINT ALL;

-- Step 4: Perform the bulk insert in batches
DECLARE @BatchSize INT = 1000;
DECLARE @LastModCounter INT = 0;

WHILE (1=1)
BEGIN
    BEGIN TRANSACTION;

    INSERT INTO DestinationTable (Column1, Column2, ..., ModCounter)
    SELECT TOP (@BatchSize) Column1, Column2, ..., ModCounter
    FROM SourceTable
    WHERE ModCounter > @LastModCounter
    ORDER BY ModCounter;

    IF @@ROWCOUNT = 0
    BEGIN
        COMMIT TRANSACTION;
        BREAK;
    END

    SET @LastModCounter = (SELECT MAX(ModCounter) FROM DestinationTable);

    COMMIT TRANSACTION;
END;

-- Step 5: Re-enable constraints
ALTER TABLE DestinationTable CHECK CONSTRAINT ALL;

-- Step 6: Rebuild indexes
ALTER INDEX ALL ON DestinationTable REBUILD;

-- Step 7: Switch back to the FULL recovery model
ALTER DATABASE YourDatabase SET RECOVERY FULL;
