


ssh -i ~/.ssh/key ubuntu@172.26.134.219

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
-p 172.26.134.219:5984:5984\
-p 172.26.134.219:4369:4369\
-p 172.26.134.219:9100-9200:9100-9200\
  --name couchdb172.26.134.219\
  --env COUCHDB_USER=${user}\
  --env COUCHDB_PASSWORD=${pass}\
  --env COUCHDB_SECRET=${cookie}\
  --env ERL_FLAGS="-setcookie \"${cookie}\" -name \"couchdb@172.26.134.219\""\
  ibmcom/couchdb3:${VERSION}




declare -a conts=(`docker ps --all | grep couchdb | cut -f1 -d' ' | xargs -n${size} -d'\n'`)

for cont in "${conts[@]}"; do docker start ${cont}; done


for node in ${othernodes} 
do
    curl -XPOST "http://${user}:${pass}@${masternode}:5984/_cluster_setup" \
      --header "Content-Type: application/json"\
      --data "{\"action\": \"enable_cluster\", \"bind_address\":\"0.0.0.0\",\
             \"username\": \"${user}\", \"password\":\"${pass}\", \"port\": \"5984\",\
             \"remote_node\": \"${node}\", \"node_count\": \"$(echo ${nodes[@]} | wc -w)\",\
             \"remote_current_user\":\"${user}\", \"remote_current_password\":\"${pass}\"}"
done


for node in ${othernodes}
do
    curl -XPOST "http://${user}:${pass}@${masternode}:5984/_cluster_setup"\
      --header "Content-Type: application/json"\
      --data "{\"action\": \"add_node\", \"host\":\"${node}\",\
             \"port\": \"5984\", \"username\": \"${user}\", \"password\":\"${pass}\"}"
done


curl -XPOST "http://${user}:${pass}@${masternode}:5984/_cluster_setup"\
    --header "Content-Type: application/json" --data "{\"action\": \"finish_cluster\"}"


for node in "${nodes[@]}"; do  curl -X GET "http://${user}:${pass}@${node}:5984/_membership"; done


curl -XPUT "http://${user}:${pass}@${masternode}:5984/twitter"
for node in "${nodes[@]}"; do  curl -X GET "http://${user}:${pass}@${node}:5984/_all_dbs"; done