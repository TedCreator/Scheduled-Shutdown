ECHO off
shutdown.exe -a
CLS

:Input

SET /P UserInput="Please Enter the number of hours you want to shutdown in, q to cancel any active: "
SET /a hours = %UserInput%

IF %UserInput% == q (
	shutdown.exe -a
	pause
	EXIT
)
SET /P UserInput= "Please Enter the number of minutes you want to shutdown in: "
SET /a minutes = %UserInput%

SET /P UserInput= "Please Enter the number of seconds you want to shutdown in: "
SET /a seconds = %UserInput%

rem convert hours and mins to seconds and add. total seconds = 3600hr + 60min + sec
SET /a total = %hours% * 3600
SET /a total = %total% + (%minutes% * 60)
SET /a total = %total% + %seconds%


IF %total% GTR 0 ( rem GTR means >
	echo %total% seconds
	shutdown.exe -S -T %total%
) ELSE (
	ECHO Your total is not greater than 0.
	GOTO Input
)

pause