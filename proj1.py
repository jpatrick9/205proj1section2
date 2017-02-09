from PIL import Image

######################################################
############### MEDIAN-CALCULATION BLOCK #############

def medianOdd(myList):                  #prepares list data to be sorted, sorts it, then                          
        listLength = len(imgList)       #returns the median value of the sorted list
        sortedValues = sorted(imgList)
        middleIndex = (((listLength+1)/2) - 1)
        return sortedValues[middleIndex]
        
######################################################
######## OBJECT DECLARATION AND IMAGE LOADING ########

imgList = []    #list for storing the 9 images to be blended

imgList.append(Image.open("1.png"))     #places each image into imgList
imgList.append(Image.open("2.png"))
imgList.append(Image.open("3.png"))
imgList.append(Image.open("4.png"))
imgList.append(Image.open("5.png"))
imgList.append(Image.open("6.png"))
imgList.append(Image.open("7.png"))
imgList.append(Image.open("8.png"))
imgList.append(Image.open("9.png"))

rList = []      #lists for holding RGB values of each pixel
gList = []
bList= []

canvas = Image.new("RGB", (495,557), "white") #Image.new("component",(width,height), "background")

#######################################################
### FOR-LOOP WITH RGB RECORDING AND PIXEL DRAWING #####

for x in range(0,495):          #x represents width
        for y in range(0,557):          # y represents height
                for myImage in imgList:         #will run once per pixel to record its RGB value
                        
                        myRed, myGreen, myBlue = myImage.getpixel((x,y))  #records the RGB values from the current position
                        
                        rList.append(myRed)     #places each R,G, and B value into the appropriate list
                        gList.append(myGreen)
                        bList.append(myBlue)
                        
                r = sorted(rList)       #sorts each list from lowest R value to highest R value (same for G and B)
                g = sorted(gList)
                b = sorted(bList)
                
                rHold = r[5]    #temporary variables for holding the median value of each color component (median between 0 and 9 is 5)
                gHold = g[5]
                bHold = b[5]
                
                canvas.putpixel((x, y), (rHold, gHold, bHold)) #colors the specified position with the specified color (R,G,B)
                
                rList = []      #clears each list to simplify future uses of .append
                gList = []
                bList = []

#########################################################
########### SAVING FINAL RESULT AS A .png ###############

canvas.save("houdini.png")




