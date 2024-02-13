
import os 

import cv2



def mk_video(thedir, video_name, puzzle_order): 
    images = [im for im in os.listdir(thedir) if im.endswith(".png")]
    images = [im for im in images if "black" not in im ]
    images = [im for im in images if "page" not in im ]

    print(f"images = {images}") 
    ## frame = cv2.imread(os.path.join(image_folder, images[0]))
    frame = cv2.imread( thedir + "//" + images[0])

    height, width, layers = frame.shape

    video = cv2.VideoWriter(video_name, 0, 1, (width,height))
    page_0 = cv2.imread( thedir + "//" + "cover_page.png")
    #cv2.imwrite( thedir + "//" + "TEST.png", page_0 )

    page_0 = cv2.resize(page_0, (width, height)) 

    for image in images:
        video.write(page_0)
        for _ in range(3): 
            video.write(cv2.imread( thedir + "//" + image)) 
        print(f"Added to video: {image}")

    cv2.destroyAllWindows()
    video.release()
    print("Video saved!!!!!!!!!!!!") 
    return 

if __name__ == "__main__":  
    video_name = 'video.avi'
    thedir = "puzzles_png"  
    mk_video(thedir, video_name ) 



