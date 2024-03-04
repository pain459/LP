@echo off
REM Sample batch script to echo start date and end date

REM Extract input dates from command line arguments
set start_date=%1
set end_date=%2

REM Echo the input dates
echo Start Date: %start_date%
echo End Date: %end_date%
