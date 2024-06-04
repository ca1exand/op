#colour-detect

from PIL import Image

path2file=""
im = Image.open(path2file)

pix = im.load()

def isgrayscale(pix, size):
    for j in range(size[0]):
            for k in range(size[1]):
                if type(pix[j,k]) is not int:
                    if pix[j,k][0] != pix[j,k][1] != pix[j,k][2]:
                        print(pix[j,k])
                        return False
    else:
        return True


def checkedges(pix):
    size = im.size
    c00 = pix[0,0]
    print(c00)
    if c00 != 0 and c00 != 255 and c00 != (0,0,0) and c00 != (255,255,255):
        return False
    for j in range(size[0]):
        if j == 0 or j == size[0]-1:
            for k in range(size[1]):
                print(pix[j,k])
                if pix[j,k] != c00:
                    return False
        else:
            print(pix[j,0],pix[j,size[1]-1])
            if pix[j,0] != c00 or pix[j,size[1]-1] != c00:
                return False
    return True



print(checkedges(pix))
print(isgrayscale(pix,im.size))
