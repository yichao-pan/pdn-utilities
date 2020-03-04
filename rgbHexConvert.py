from PIL import ImageColor

def rgba_to_hex(rgba, pdn=False):
    """
    Converts rgba to hex color code.
    Set pdn to True to have alpha before rgb (paint.net format)
    """
    if(not pdn):
        return '#{:02x}{:02x}{:02x}{:02x}'.format(rgba[0], rgba[1], rgba[2], rgba[3])
    else:
        return '#{:02x}{:02x}{:02x}{:02x}'.format(rgba[3], rgba[0], rgba[1], rgba[2])

def hex_to_rgba(hex_code, pdn=False):
    """
    Converts hex color code to rgba code.
    Set pdn to True to have alpha before rgb (paint.net format)
    """
    if(not hex_code.startswith('#')):
        hex_code = '#'+hex_code
    if (not pdn):
        return ImageColor.getrgb(hex_code)
    else:
        rgba = ImageColor.getrgb(hex_code)
        return rgba[1], rgba[2], rgba[3], rgba[0]
