TULSI SERVER PACKAGE

Installation procedure :

Run the following command in root previlages 

1. Download the tulsi package in the swift node 

git clone https://github.com/vedgithub/tulsi.git

2. cd tulsi/TulsiServer/tulsi
	
3. Edit the host ip with Tulsi client IP in tulsi.conf

[tulsi]

host = << IP of host >>

4. Run sh tulsi.sh

5. Start the server 
 
 service tulsi start


6.Check the server status 
 
 service tulsi status 

