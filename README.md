# equalexpertstest
#build the project
docker run -it equal:1
#run test for api
docker run -it equal:1  bash -c "/app/case.sh; test"

