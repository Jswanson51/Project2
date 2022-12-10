import webcolors
#The following is starter code from https://www.youtube.com/watch?v=guWxEIqYy_I

def closest_color(RGB):
    differences = {}

    for color_hex, color_name in webcolors.CSS2_HEX_TO_NAMES.items()
        R,G,B = webcolors.hex_to_rgb(color_hex)
        differences[sum([(R-RGB[0]) **2,
                         (G-RGB[1]) **2,
                          (B-RGB[2]) **2])] = color_name

        return differences[min(differences.keys())]

color = (113, 241, 224)

try:
    cname = webcolors.rgb_to_name(color)
except ValueError:
    cname = closest_color(color)
    print(f"The color is closest to {cname}")


