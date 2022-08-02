def parse_desc():
    with open("../../utils/textColor/ansi.py", encoding="utf-8") as fp:
        content = fp.read()
    for line in content.splitlines():
        line = line.strip()
        if line and '=' in line and '#' in line:
            _, cont = line.split('=')
            code, desc = cont.split('#')
            CODE_DESC[int(code.strip())] = desc.strip()
            # print(f'{code.strip()}:"{desc.strip()}",')


def write_desc():
    with open("code_desc.py", 'w', encoding="utf-8") as fp:
        fp.write("CODE_DESC = {\n")
        for k, v in CODE_DESC.items():
            fp.write(f'    {k}: "{v}",\n')
        fp.write("}\n")


CODE_DESC = {}

if __name__ == '__main__':
    parse_desc()
    write_desc()
