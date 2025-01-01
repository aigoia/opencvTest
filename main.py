import cv2 as opencv
import numpy 

# Constants
WIDTH, HEIGHT = 800, 600
PADDLE_WIDTH, PADDLE_HEIGHT = 20, 100
BALL_RADIUS = 15
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Key settings
key_esc = 27  # ESC key

def main():
    ball_pos = [WIDTH // 2, HEIGHT // 2]
    player1_pos = HEIGHT // 2 - PADDLE_HEIGHT // 2
    player2_pos = HEIGHT // 2 - PADDLE_HEIGHT // 2
    paddle_speed = 10
    score1, score2 = 0, 0

    # Create window
    opencv.namedWindow("Pong", opencv.WINDOW_GUI_NORMAL)

    while True:
        # Create a blank frame
        frame = numpy.zeros((HEIGHT, WIDTH, 3), dtype=numpy.uint8)

        # Draw paddles and ball
        opencv.rectangle(frame, (20, player1_pos), (20 + PADDLE_WIDTH, player1_pos + PADDLE_HEIGHT), WHITE, -1)
        opencv.rectangle(frame, (WIDTH - 20 - PADDLE_WIDTH, player2_pos), (WIDTH - 20, player2_pos + PADDLE_HEIGHT), WHITE, -1)
        opencv.circle(frame, tuple(ball_pos), BALL_RADIUS, WHITE, -1)

        # Draw scores
        font = opencv.FONT_HERSHEY_SIMPLEX
        opencv.putText(frame, f"{score1}", (WIDTH // 4, 50), font, 1.5, WHITE, 2)
        opencv.putText(frame, f"{score2}", (3 * WIDTH // 4, 50), font, 1.5, WHITE, 2)

        # Handle key events
        key = opencv.waitKey(1) & 0xFF
        if key == ord('w') and player1_pos > 0:
            player1_pos -= paddle_speed
        if key == ord('s') and player1_pos < HEIGHT - PADDLE_HEIGHT:
            player1_pos += paddle_speed
        if key == ord('o') and player2_pos > 0:
            player2_pos -= paddle_speed
        if key == ord('l') and player2_pos < HEIGHT - PADDLE_HEIGHT:
            player2_pos += paddle_speed
        
        # Exit on ESC key
        if key == key_esc:  
            break

        # Display frame
        opencv.imshow("Pong", frame)

    opencv.destroyAllWindows()

if __name__ == "__main__":
    main()