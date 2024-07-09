Docker commands:
docker build -t user/container:tag
docker run user/container:tag

When running Flask, use command docker run -p port:port flask/app/name

If having problems pushing to Flask:
Login to docker.io
Make sure file is named user/container:tag
Then docker push user/container:tag

If have to clone AGAIN:
In debug: delete certs, delete /private, rename name to dmm-sicat

To run DMM script: cd rucio-sense-dmm > ./etc/debug.sh
To add rules: open new terminal simultaneously with debug script > 
python rucio.py --rule_id TEST_RULE --src_site T2_US_SDSC --dst_site T2_US_Caltech_Test --priority 5 add

When done testing, run this command: python tests/free_alloc.py --sitename T2_US_SDSC