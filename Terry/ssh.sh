cd C:\Users\dunim\source\repos\Terry\Terry

eval $(ssh-agent -s)

ssh-add ~/.ssh/vss

ssh -T git@github.com
