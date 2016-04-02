from PIL import Image

def cropPic(infile):
    src = Image.open(infile)
    
    width, height = src.size
    # must be even number to work, odd number should adjust
    boxScale = 57
    box = (width/2-boxScale+1, height/2-boxScale+1, width/2+boxScale, height/2+boxScale)
    
    dest = src.crop(box)
    dest.save(infile)


def genPhoto(folderIndex):
    for i in xrange(30):
        cropPic("../gradPhoto/"+str(folderIndex)+"/"+str(i)+".jpg")
    
    l = 113
    dest = Image.new("RGBA", (l*5, l*6))
    for i in xrange(6):
        for j in xrange(5):       
            src = Image.open("../gradPhoto/"+str(folderIndex)+"/"+str(i*5+j)+".jpg")
            dest.paste(src, (j*l,i*l))
    dest = dest.crop((0,0,l*5-72,l*6-36))
    dest.save("../gradPhoto/merge"+str(folderIndex)+".jpg")


if __name__ == "__main__":
    for i in xrange(10001, 10003):
        genPhoto(i)
        
    for i in xrange(20003, 20014):
        genPhoto(i) 

