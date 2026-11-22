import cv2
img = cv2.imread("encrypt_img.jpg", cv2.IMREAD_GRAYSCALE)

msg = input("Enter the secret message : ")

shape = img.shape

if((len(msg) + 1) * 8 >= shape[0] * shape[1]):
    print("Message can't be encrypted. Enter a shorted message.")
    quit()


bin_str = ""

for ch in msg:
    bin_str += bin(ord(ch))[2 : ].zfill(8)
bin_str += bin(ord("\0"))[2 : ].zfill(8)

break_mem = False
x = 0
for i in range(len(img)):
    for j in range(len(img[0])):
        
        
        if(bin_str[x] == "0"):
            img[i][j] &= 254
        else:
            img[i][j] |= 1
        
        x += 1

        if(x == len(bin_str)):
            break_mem = True
            break
    
    if(break_mem):
        break


cv2.imwrite("secret.png", img)        