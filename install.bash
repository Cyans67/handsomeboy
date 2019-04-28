#!/usr/bin/env bash
cd packages
python-3.6.3.exe
cd ..
#setx path "%path%;C:\Python27\;C:\Python27\Scripts" /m
% reg add KEY  /v path /t REG_SZ /d ";C:\Python36\;C:\Python36\Scripts"
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple