# [Contact an Author]
# * [Name: nho Luong]
# * [Skype](luongutnho_skype)
# * [Github](https://github.com/nholuongut/)
# * [Linkedin](https://www.linkedin.com/in/nholuong/)
# * [Email Address](luongutnho@hotmail.com)

from urllib import parse

endpoint: str = 'https://gitlab.com'
url_obj = parse.urlparse(endpoint)
print(f"scheme: {url_obj.scheme}, netloc: {url_obj.netloc}")
