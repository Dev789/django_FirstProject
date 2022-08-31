aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 496215038078.dkr.ecr.us-east-1.amazonaws.com


docker pull 496215038078.dkr.ecr.us-east-1.amazonaws.com/test-repo:latest