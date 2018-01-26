set -x
set -e

mkdir ~/.aws
touch ~/.aws/config
chmod 600 ~/.aws/config
echo "[profile eb-cli]" > ~/.aws/config
echo "aws_access_key_id=$AWS_ACCESS_KEY_ID" >> ~/.aws/config
echo "aws_secret_access_key=$AWS_SECRET_ACCESS_KEY" >> ~/.aws/config