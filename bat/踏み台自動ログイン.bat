echo off
Set USERNAME=******** #user�������
Set PASSWORD="********" #password�����
Set humidai=


echo -------------------------------------------
echo �Z�Z1 ��1
echo �Z�Z2 ��2
echo �Z�Z3 ��3
echo �Z�Z4 ��4
echo �Z�Z5 ��5
echo �Z�Z6 ��6
echo �Z�Z7 ��7
echo �Z�Z8 ��8
echo �Z�Z9 ��9
echo �Z�Z10 ��10
echo -------------------------------------------

set /p humidai="number����͂��Ă�������"
Cmdkey /generic:TERMSRV/%SERVER% /user:%USERNAME% /pass:%PASSWORD%
Start mstsc /v:�Z�Z%humidai%
Timeout 3
Cmdkey /delete:TERMSRV/%SERVER%