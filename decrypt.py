import cv2
img = cv2.imread("secret.png", cv2.IMREAD_GRAYSCALE)

message = ""
temp = ""
break_mem = False
for i in range(len(img)):
    for j in range(len(img[0])):
        
        bit = str(img[i][j] & 1)
        temp += bit

        
        if(len(temp) == 8):
            ch = chr(int(temp, 2))
            temp = ""
            
            if(ch != "\0"):
                message += ch
            else:
                break_mem = True
                break

    if(break_mem):
        break

print(message)