docker run \
-p 5000:5000 \
--mount type=bind,source=$(PWD)/config.yaml,target=/root/config.yaml \
--mount type=bind,source=$REQUESTS_CA_BUNDLE,target=/etc/ssl/certs/ca-certificates.crt \
-e REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt \
hooks-receiver:development-latest
