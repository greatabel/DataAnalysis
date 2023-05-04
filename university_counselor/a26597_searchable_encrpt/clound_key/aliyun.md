ssh -i mysecret.pem root@60.205.169.203

tmux attach -t 0

http://60.205.169.203:5000/home

# 拷贝
scp -r -i clound_key/mysecret.pem   .  root@60.205.169.203:/root/a26597_searchable_encrpt

