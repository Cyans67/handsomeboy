cd packages
python-3.6.3.exe
cd ..
setx path "%path%;C:\Python27\;C:\Python27\Scripts" /m
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple