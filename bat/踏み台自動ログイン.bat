echo off
Set USERNAME=******** #user–¼‚ğ“ü—Í
Set PASSWORD="********" #password‚ğ“ü—Í
Set humidai=


echo -------------------------------------------
echo ZZ1 Ë1
echo ZZ2 Ë2
echo ZZ3 Ë3
echo ZZ4 Ë4
echo ZZ5 Ë5
echo ZZ6 Ë6
echo ZZ7 Ë7
echo ZZ8 Ë8
echo ZZ9 Ë9
echo ZZ10 Ë10
echo -------------------------------------------

set /p humidai="number‚ğ“ü—Í‚µ‚Ä‚­‚¾‚³‚¢"
Cmdkey /generic:TERMSRV/%SERVER% /user:%USERNAME% /pass:%PASSWORD%
Start mstsc /v:ZZ%humidai%
Timeout 3
Cmdkey /delete:TERMSRV/%SERVER%