import cv2
import pygame
from pygame.locals import *

def video_chat():
    # Initialize Pygame window
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Video Chat")
    
    # Initialize video capture
    cap = cv2.VideoCapture(0)
    
    while True:
        ret, frame = cap.read()  # Read a frame from the video capture
        
        # Convert the frame to RGB for Pygame display
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_pygame = pygame.image.frombuffer(frame_rgb.tostring(), frame.shape[1::-1], "RGB")
        
        # Display the frame on Pygame window
        screen.blit(frame_pygame, (0, 0))
        pygame.display.update()
        
        # Check for quit event
        for event in pygame.event.get():
            if event.type == QUIT:
                cap.release()  # Release the video capture
                pygame.quit()
                return

if __name__ == '__main__':
    video_chat()
