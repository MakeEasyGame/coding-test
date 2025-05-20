# 파일명 정렬

import re

def get_filename(filename):
    match = re.match(r'([^\d]+)(\d{1,5})', filename)
    head = match.group(1)
    number = match.group(2)
    return head, number

def solution(files):
    parsed = []
    for i, file in enumerate(files):
        head, number = get_filename(file)
        parsed.append((head.lower(), int(number), i, file))
    parsed.sort(key=lambda x: (x[0], x[1], x[2]))
    return [item[3] for item in parsed]