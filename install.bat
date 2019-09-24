python -m virtualenv wenv 
call wenv\scripts\activate

REM Upgrade pip in virtual env
python -m pip install --upgrade pip
pip install -r requirements.txt

REM Windows Wheel Binary installer
REM pip install https://download.lfd.uci.edu/pythonlibs/g5apjq5m/lxml-4.4.1-cp37-cp37m-win_amd64.whl


REM Pelican Themes local
REM git clone https://github.com/getpelican/pelican-themes.git themes --recursive
REm USe D:\Projects\Blogs\Pelican\themes

