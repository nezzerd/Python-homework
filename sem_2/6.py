import re

html_content = "1NoahEmma2LiamOlivia3MasonSophia4JacobIsabella5WilliamAva6EthanMia7MichaelEmily"
pattern = r"(?<=\d)([A-Za-z]+)"
data = re.findall(pattern, html_content)
print(data)