import cv2
import numpy 

# 화면 크기
WIDTH, HEIGHT = 800, 600

# 패들과 공의 초기 속성
PADDLE_WIDTH, PADDLE_HEIGHT = 20, 100
BALL_RADIUS = 15

# 색상 정의 (BGR 형식)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# 초기 위치와 속도
ball_pos = [WIDTH // 2, HEIGHT // 2]
ball_velocity = [4, 4]

player1_pos = HEIGHT // 2 - PADDLE_HEIGHT // 2
player2_pos = HEIGHT // 2 - PADDLE_HEIGHT // 2
paddle_speed = 10

# 점수
score1, score2 = 0, 0

# OpenCV 윈도우 초기화
cv2.namedWindow("Pong Game")

while True:
    frame = numpy.zeros((HEIGHT, WIDTH, 3), dtype=numpy.uint8)

    cv2.rectangle(frame, (20, player1_pos), (20 + PADDLE_WIDTH, player1_pos + PADDLE_HEIGHT), WHITE, -1)
    cv2.rectangle(frame, (WIDTH - 20 - PADDLE_WIDTH, player2_pos), (WIDTH - 20, player2_pos + PADDLE_HEIGHT), WHITE, -1)

    cv2.circle(frame, tuple(ball_pos), BALL_RADIUS, WHITE, -1)

    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, f"{score1}", (WIDTH // 4, 50), font, 1.5, WHITE, 2)
    cv2.putText(frame, f"{score2}", (3 * WIDTH // 4, 50), font, 1.5, WHITE, 2)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('w') and player1_pos > 0:
        player1_pos -= paddle_speed
    if key == ord('s') and player1_pos < HEIGHT - PADDLE_HEIGHT:
        player1_pos += paddle_speed
    if key == ord('o') and player2_pos > 0:
        player2_pos -= paddle_speed
    if key == ord('l') and player2_pos < HEIGHT - PADDLE_HEIGHT:
        player2_pos += paddle_speed
    if key == ord('q'):  # 'q' key is exit
        break

    cv2.imshow("Pong Game", frame)


cv2.destroyAllWindows()