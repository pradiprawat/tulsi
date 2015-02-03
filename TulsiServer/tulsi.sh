
mkdir /etc/tulsi
cd tulsi/

cp -v tulsi /etc/init.d/
cp -v Tulsi.py /etc/tulsi/
cp -v tulsi.conf /etc/tulsi/
cp -v MessageEncode.py /etc/tulsi/
cp -v HostInfo.py  /etc/tulsi/
cp -v Server.py /etc/tulsi
chmod 755 /etc/tulsi/*.*
chmod 755 /etc/init.d/tulsi
echo "Tulsi Successfully installed!!!"
