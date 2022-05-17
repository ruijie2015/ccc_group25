


ssh -i ~/.ssh/key ubuntu@172.26.132.13


sudo apt-get update

sudo apt-get install \
    ca-certificates \
    curl \
    gnupg \
    lsb-release

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt-get update

sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin

y

sudo chmod 666 /var/run/docker.sock


export declare -a nodes=(172.26.134.219 172.26.132.13)
export masternode=172.26.132.13
export declare -a othernodes=`echo ${nodes[@]} | sed s/${masternode}//`
export size=${#nodes[@]}
export user='admin'
export pass='admin'
export VERSION='3.2.1'
export cookie='a192aeb9904e6590849337933b000c99'


docker create\
-p 172.26.132.13:5984:5984\
-p 172.26.132.13:4369:4369\
-p 172.26.132.13:9100-9200:9100-9200\
  --name couchdb172.26.132.13\
  --env COUCHDB_USER=${user}\
  --env COUCHDB_PASSWORD=${pass}\
  --env COUCHDB_SECRET=${cookie}\
  --env ERL_FLAGS="-setcookie \"${cookie}\" -name \"couchdb@172.26.132.13\""\
  ibmcom/couchdb3:${VERSION}



declare -a conts=(`docker ps --all | grep couchdb | cut -f1 -d' ' | xargs -n${size} -d'\n'`)



for cont in "${conts[@]}"; do docker start ${cont}; done




curl -X GET http://172.26.128.232:5984/enroll_data/_all_docs?include_docs=true > /Users/lenovo/Desktop/db.json

curl -X GET 'http://admin:admin@172.26.128.232:5984/enroll_data/_all_docs?include_docs=true' >db2.json
curl -d @db2.json  -X POST http://admin:admin@172.26.128.232:5984/test2/_bulk_docs

