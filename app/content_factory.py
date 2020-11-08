from app import content

import random
import re

def generate_paragraph(content_id):
    phrases = content.TXT
    header = phrases[content_id]["title"]
    exp = '{.*?}'
    to_randomize = re.findall(exp, phrases[content_id]["content"])
    result = [random.choice(x[1:-1].split(";")) for x in to_randomize]
    paragraph = " ".join(result)
    return [header, paragraph]

if __name__ == "__main__":
    for _ in range(5):
        print(generate_paragraph("green_general"))
    