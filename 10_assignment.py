import cv2
import numpy as np
import matplotlib.pyplot as plt

class ComponentsIdentifier:

    def __init__(self):
        self.pixel_grid = []
        self.visited = set()
        self.components = []

    def get_exit_points(self, i, j):
        
        exit_points = []
        
        if((i - 1, j) not in self.visited and i - 1 >= 0 and self.pixel_grid[i - 1][j] != 255):
            exit_points.append((i - 1, j))
        
        if((i, j - 1) not in self.visited and j - 1 >= 0 and self.pixel_grid[i][j - 1] != 255):
            exit_points.append((i, j - 1))
        
        if((i, j + 1) not in self.visited and j + 1 < len(self.pixel_grid[0]) and self.pixel_grid[i][j + 1] != 255):
            exit_points.append((i, j + 1))
        
        if((i + 1, j) not in self.visited and i + 1 < len(self.pixel_grid) and self.pixel_grid[i + 1][j] != 255):
            exit_points.append((i + 1, j))

        if((i - 1, j - 1) not in self.visited and i - 1 >= 0 and j - 1 >= 0 and self.pixel_grid[i - 1][j - 1] != 255):
            exit_points.append((i - 1, j - 1))
        
        if((i - 1, j + 1) not in self.visited and i - 1 >= 0 and j + 1 < len(self.pixel_grid[0]) and self.pixel_grid[i - 1][j + 1] != 255):
            exit_points.append((i - 1, j + 1))
        
        if((i + 1, j - 1) not in self.visited and i + 1 < len(self.pixel_grid) and j - 1 >= 0 and self.pixel_grid[i + 1][j - 1] != 255):
            exit_points.append((i + 1, j - 1))
        
        if((i + 1, j + 1) not in self.visited and i + 1 < len(self.pixel_grid) and j + 1 < len(self.pixel_grid[0]) and self.pixel_grid[i + 1][j + 1] != 255):
            exit_points.append((i + 1, j + 1))
        
        return exit_points
    
    def identify_component(self) -> bool:

        comp = set()
        
        break_mem = False
        for i in range(len(self.pixel_grid)):
            for j in range(len(self.pixel_grid[0])):
                if(self.pixel_grid[i][j] != 255 and (i, j) not in self.visited):
                    break_mem = True
                    break
            if(break_mem):
                break
        
        if(not break_mem):
            return False
        
        stack = []
    
        while(True):
            
            self.visited.add((i, j))
            comp.add((i, j))
            
            exit_points = self.get_exit_points(i, j)

            if(len(exit_points) == 0):
                try:
                    checkpoint = stack.pop()
                except:
                    self.components.append(comp)
                    return True
                
                i = checkpoint[0]
                j = checkpoint[1]
                continue

            elif(len(exit_points) != 1):
                stack.append((i, j))
            
            i = exit_points[0][0]
            j = exit_points[0][1]
    
    def process(self, grid):

        self.pixel_grid = grid
        

        while(self.identify_component()):
            pass
        
        return self.components

img = cv2.imread("10_assignment.png", cv2.IMREAD_GRAYSCALE)   
img_color = np.stack((img, img, img), axis = -1)

for i in range(len(img)):
    for j in range(len(img[0])):
        if(img[i][j] <= 127):
            img[i][j] = 0
        else:
            img[i][j] = 255


plt.subplot(2, 2, 1)
plt.title("Original")
plt.imshow(img, cmap="gray", vmin=0, vmax=255)


obj = ComponentsIdentifier()
components = obj.process(img)

colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 0, 255), (128, 0, 128)]

for comp in components:
    color = colors.pop(0)
    for px in comp:
        img_color[px[0]][px[1]][0] = color[0]
        img_color[px[0]][px[1]][1] = color[1]
        img_color[px[0]][px[1]][2] = color[2]

plt.subplot(2, 2, 2)
plt.title("Labelling")
plt.imshow(img_color)

def calc_distance(x1, y1, x2, y2):
    
    dist = (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5
    return dist

i = 0
while(i < len(components)):
    
    components[i] = list(components[i])
    i += 1


closest_pixels = []
i = 0
while(i < len(components) - 1):
    j = i + 1
    while(j < len(components)):
        
        comp1 = components[i]
        comp2 = components[j]
        min_dist = int(2 ** 31)
        px1 = comp1[0]
        px2 = comp2[0]

        for x in comp1:
            for y in comp2:

                dist = calc_distance(x[0], x[1], y[0], y[1])
                if(dist < min_dist):
                    min_dist = dist
                    px1 = x
                    px2 = y
        
        if(calc_distance(px1[0], px1[1], px2[0], px2[1]) < 10):
            closest_pixels.append([px1, px2])

        j += 1
    i += 1

# print(closest_pixels)

for pixels in closest_pixels:
    cv2.line(img, (pixels[0][1], pixels[0][0]), (pixels[1][1], pixels[1][0]), color=(0, 0, 0), thickness = 5)

plt.subplot(2, 2, 3)
plt.title("Joined")
plt.imshow(img, cmap="gray", vmin=0, vmax=255)

plt.show()