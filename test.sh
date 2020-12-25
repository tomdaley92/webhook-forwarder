HOST=http://0.0.0.0:5000

curl \
-X POST \
-H "Content-Type: application/json" \
-H "User-Agent: GitHub-Hookshot/3211ebf" \
-H "X-GitHub-Delivery: b93846f0-5ff9-11ea-84d7-4363c65fe24b" \
-H "X-GitHub-Enterprise-Host: scm.starbucks.com" \
-H "X-GitHub-Enterprise-Version: 2.19.6" \
-H "X-GitHub-Event: ping" \
-d "@ping.json" $HOST/github/steelhead/ui/build-deploy

curl \
-X POST \
-H "Content-Type: application/json" \
-H "User-Agent: GitHub-Hookshot/3211ebf" \
-H "X-Hub-Signature: sha1=cfe5adcd164b6b0ff038e12d9f297061dedb1684" \
-H "X-GitHub-Delivery: b93846f0-5ff9-11ea-84d7-4363c65fe24b" \
-H "X-GitHub-Enterprise-Host: scm.starbucks.com" \
-H "X-GitHub-Enterprise-Version: 2.19.6" \
-H "X-GitHub-Event: ping" \
-d "@ping.json" $HOST/github/steelhead/ui/build-deploy

curl \
-X POST \
-H "Content-Type: application/json" \
-H "User-Agent: GitHub-Hookshot/3211ebf" \
-H "X-Hub-Signature: sha1=cfe5adcd164b6b0ff038e12d9f297061dedb1684" \
-H "X-GitHub-Delivery: b93846f0-5ff9-11ea-84d7-4363c65fe24b" \
-H "X-GitHub-Enterprise-Host: scm.starbucks.com" \
-H "X-GitHub-Enterprise-Version: 2.19.6" \
-H "X-GitHub-Event: ping" \
-d "@ping.json" $HOST/github/steelhead/api/build-deploy


curl \
-X POST \
-H "Content-Type: application/json" \
-H "User-Agent: GitHub-Hookshot/3211ebf" \
-H "X-Hub-Signature: sha1=b3616a60de6eb39dd401e86ba841d02c4bee7f17" \
-H "X-GitHub-Delivery: 61d1ddf0-60bb-11ea-929d-84dc207ae764" \
-H "X-GitHub-Enterprise-Host: scm.starbucks.com" \
-H "X-GitHub-Enterprise-Version: 2.19.6" \
-H "X-GitHub-Event: push" \
-d "@push.json" $HOST/github/steelhead/ui/build-deploy
