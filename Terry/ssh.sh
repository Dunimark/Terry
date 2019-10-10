eval $(ssh-agent -s)

ssh-add ~/.ssh/vss

ssh -T git@github.com
