"""杂项工具功能"""


def render_str(str,**args):
    for item,content in args.items():
        str = str.replace("{"+item+"}", content)
    return str

