# [Contact an Author]
# * [Name: nho Luong]
# * [Skype](luongutnho_skype)
# * [Github](https://github.com/nholuongut/)
# * [Linkedin](https://www.linkedin.com/in/nholuong/)
# * [Email Address](luongutnho@hotmail.com)

#!/bin/bash

cd "$(dirname "$0")"
cd ..

docker system prune -a -f --volumes
sudo rm -f -r vols
