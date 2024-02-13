
import os 

import cv2
#image = cv2.imread("stage_1/page_10.png")

class Crop_png(): 

    def __init__(self, input_dir="stage_1_training_png", output_dir = "puzzles_png"): 
        self.input_dir = input_dir 
        self.output_dir = output_dir 
        
        self.top_left_board = { 
        "start_from_left":0,
        "end_from_left":400,
        "start_from_top":100,
        "end_from_top":500
        }
    
        self.mid_left_board = { 
        "start_from_left":0,
        "end_from_left":400,
        "start_from_top":480,
        "end_from_top":880
        }
    
    
        self.bottom_left_board = { 
        "start_from_left":0,
        "end_from_left":400,
        "start_from_top":880,
        "end_from_top":1280  
        }
    
        self.top_right_board = { 
        "start_from_left":450,
        "end_from_left":850,
        "start_from_top":100,
        "end_from_top":500 
        }
    
        self.mid_right_board = { 
        "start_from_left":450,
        "end_from_left":850,
        "start_from_top":480,
        "end_from_top":880 
        }
    
        self.bottom_right_board = { 
        "start_from_left":450,
        "end_from_left":850,
        "start_from_top":880,
        "end_from_top":1280 
        }
        
        
    def crop_images(self): 
        puzzle_num=1
        pages = os.listdir(self.input_dir) 
        puzzle_order=[]
        for page in pages: 
            image = cv2.imread(f"{self.input_dir}/{page}")
            for board in [self.top_left_board, self.mid_left_board, self.bottom_left_board, 
                          self.top_right_board, self.mid_right_board, self.bottom_right_board]:
                crop_image = image[board["start_from_top"] : board["end_from_top"], 
                          board["start_from_left"] : board["end_from_left"]]
                #cv2.imshow("Cropped", crop_image)
                cv2.imwrite(f"{self.output_dir}/Puzzle_{puzzle_num}.png", crop_image)
                cv2.waitKey(0)
                print(f"Saved puzzle no. {puzzle_num} in {self.output_dir}") 
                puzzle_order.append(puzzle_num) 
                puzzle_num+=1 

        print(f"\n***\nPuzzle order returned from 'crop_images' = {puzzle_order}\n***\n") 
        return puzzle_order 

"""
from PIL import Image

img = Image.open('./page_10.png')
#img.show()

box = (250, 250, 750, 750)
img2 = img.crop(box)

img2.save('page_10_cropped.jpg')
#img2.show()
""" 

if __name__ == "__main__": 
    crop_obj = Crop_png( input_dir="stage_1_training_png", output_dir="puzzles_png" ) 
    puzzle_order = crop_obj.crop_images() 
    
    
    