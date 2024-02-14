
from pdf2png  import pdf2png 
from crop_png import Crop_png 
import cv2
import imageio
from mk_video import mk_video 

input_file_path = "1a_book//1a manual chess combinations.pdf"
output_dir="pages_png"

pdf2png(input_file_path, output_dir)

crop_obj = Crop_png( input_dir="stage_1_training_png", output_dir="puzzles_png" ) 
puzzle_order = crop_obj.crop_images() 
print(f"puzzle_order = {puzzle_order}")
 
video_name = 'video.avi'
thedir = "puzzles_png"  

# mk_video( thedir, video_name, puzzle_order ) 

big_image = "puzzles_png/cover_page.png"
def resize_images(big_image, small_image_order ): 
    cover_page = cv2.imread( big_image )
    height_cover_page, width_cover_page, layers_cover_page = cover_page.shape
    print(f"\nCover Page:\nHeight = {height_cover_page}\nWidth = {width_cover_page}\nLayers = {layers_cover_page}") 

    for puzzle_number in small_image_order: 
        puzzle = f"puzzles_png/Puzzle_{puzzle_number}.png" 
        puzzle = cv2.imread( puzzle ) 
        height_puzzle, width_puzzle, layers_puzzle = puzzle.shape
        print(f"\nPuzzle:\nHeight = {height_puzzle}\nWidth = {width_puzzle}\nLayers = {layers_puzzle}") 

        vertical_extra   =  height_cover_page - height_puzzle
        horizontal_extra =  width_cover_page  - width_puzzle  
    
        top_extra       = vertical_extra // 2 
        bottom_extra    = vertical_extra -  top_extra
        left_extra      = horizontal_extra // 2  
        right_extra     = horizontal_extra - left_extra 

        padded_image = cv2.copyMakeBorder(puzzle, top_extra, bottom_extra, left_extra, right_extra, cv2.BORDER_CONSTANT)
        cv2.imwrite(f"puzzles_png/Puzzle_{puzzle_number}_PADDED.png", padded_image) 
        print(f"Finished puzzles_png/Puzzle_{puzzle_number}_PADDED.png") 
    return 
resize_images(big_image, puzzle_order) 


images = []
for puzzle_number in puzzle_order: 
    cover_p = "puzzles_png/cover_page.png"
    images.append(imageio.imread(cover_p))
    file = f"puzzles_png/Puzzle_{puzzle_number}_PADDED.png" 
    images.append(imageio.imread(file))
    print(f"Appended puzzle no. {puzzle_number} to the video") 
imageio.mimwrite('./movie.gif', images , duration=2.0  )

exit() 

with imageio.get_writer('/movie.gif', mode='I') as writer:
    for filename in filenames:
        image = imageio.imread(filename)
        writer.append_data(image)
        

# In the end I think the key point is that OpenCV is not designed to be a video capture library - 
# it doesn't even support sound. VideoWriter is useful, but 99% of the time you're better off saving 
# all your images into a folder and using ffmpeg to turn them into a useful video.
