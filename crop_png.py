
import os 

import cv2
#image = cv2.imread("stage_1/page_10.png")


top_left_board = { 
    "start_from_left":0,
    "end_from_left":400,
    "start_from_top":100,
    "end_from_top":500
    }
    
mid_left_board = { 
    "start_from_left":0,
    "end_from_left":400,
    "start_from_top":480,
    "end_from_top":880
    }
    
    
bottom_left_board = { 
    "start_from_left":0,
    "end_from_left":400,
    "start_from_top":880,
    "end_from_top":1280  
    }
    
top_right_board = { 
    "start_from_left":450,
    "end_from_left":850,
    "start_from_top":100,
    "end_from_top":500 
    }
    
mid_right_board = { 
    "start_from_left":450,
    "end_from_left":850,
    "start_from_top":480,
    "end_from_top":880 
    }
    
bottom_right_board = { 
    "start_from_left":450,
    "end_from_left":850,
    "start_from_top":880,
    "end_from_top":1280 
    }
puzzle_num=1

pages = os.listdir("stage_1") 
for page in pages: 
    image = cv2.imread(f"stage_1/{page}")
    for board in [top_left_board, mid_left_board, bottom_left_board, 
                  top_right_board, mid_right_board, bottom_right_board]:
        crop_image = image[board["start_from_top"] : board["end_from_top"], 
                          board["start_from_left"] : board["end_from_left"]]
        #cv2.imshow("Cropped", crop_image)
        cv2.imwrite(f"puzzles/Puzzle_{puzzle_num}.png", crop_image)
        cv2.waitKey(0)
        print(f"Finished puzzle number {puzzle_num}") 
        puzzle_num+=1 
     

exit() 

from PIL import Image

img = Image.open('./page_10.png')
#img.show()

box = (250, 250, 750, 750)
img2 = img.crop(box)

img2.save('page_10_cropped.jpg')
#img2.show()
