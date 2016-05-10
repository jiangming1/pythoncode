mkdir ~/test/lcba
cd ~/test
appium&
echo $! > appium.pid
#emulator @test800&
#echo $! > 800.pid
emulator @test240&
echo $! > 240.pid
sleep 30s
emulator @test720& 
echo $! > 720.pid
sleep 30s
emulator @test768&
echo $! > 768.pid
sleep 30s

python lcba.py
kill `cat 240.pid`
sed -i '' "s/a 240 /a 720 /g" lcba.py
python lcba.py
kill `cat 720.pid`
sed -i '' "s/a 720 /a 768 /g" lcba.py
python lcba.py
kill `cat 768.pid`
sed -i '' "s/a 240 /a 720 /g" lcba.py
python lcba.py
kill `cat 1080.pid`
sed -i '' "s/a 720 /a 1080 /g" lcba.py
sed -i '' "s/a 1080 /a 240 /g" lcba.py
ssh root@120.27.145.189 'mkdir -p /opt/pic_test/`date "+%Y_%m_%d"`/ '
scp ~/test/lcb/* root@120.27.145.189:/opt/pic_test/`date "+%Y_%m_%d"`

ssh root@www.caiwuhao.com 'mkdir -p /alidata/www/app/`date "+%Y_%m_%d"`/ '
scp ~/test/lcb/* root@www.caiwuhao.com:/alidata/www/app/`date "+%Y_%m_%d"`
kill `cat appium.pid`
