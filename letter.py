sample = """

[12/01/2017 12:03:53 a.m.] Roman: genial
[12/01/2017 12:04:15 a.m.] Max te voy a pasar unos links con informacion acerca del concurso
[12/01/2017 12:04:19 a.m.] Max para que los revises
[12/01/2017 12:04:25 a.m.] Roman: ok
[12/01/2017 12:04:54 a.m.] Max  Este es el video oficial para publicitar el concurso
[12/01/2017 12:04:58 a.m.] Max https://www.youtube.com/watch?v=7LCBADvwMyk
"""




proof = """
sdt1dddddddddddddddddd
dsddt1dddddddddddddddd
dsdddt1ddddddddddddddddd
"""

sample = list(proof)

print(sample)

d = False
for c in proof:
    if c == "s":
        d = True
    if c == "t":
        d = False
        sample.remove(c)
    if d:
        sample.remove(c)

chat = ""
for c in sample:
    chat += c

print(chat)
