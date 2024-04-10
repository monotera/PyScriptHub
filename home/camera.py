import cv2
import os
from dotenv import load_dotenv

load_dotenv()

def connect_to_ip_camera(ip_url):
    """
    Connect to an IP camera and display the video stream.

    Parameters:
    - ip_url: The URL of the IP camera stream (e.g., "rstp://username:password@192.168.1.100:8080/video").
    """
    # Create a VideoCapture object with the IP URL
    cap = cv2.VideoCapture(ip_url)

    # Check if the camera opened successfully
    if not cap.isOpened():
        print("Error: Could not open video stream.")
        return

    # Read and display the video frames in a loop
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # If frame is read correctly ret is True
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break

        # Display the resulting frame
        cv2.imshow("IP Camera Stream", frame)

        # Break the loop when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    # When everything done, release the capture and destroy all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    password = os.getenv("PASSWORD")
    username = os.getenv("CAMERA_USERNAME")
    stream_channel=os.getenv("STREAM_CHANNEL")
    ip_address=os.getenv("IP_ADDRESS")
    ip_camera_url = f"rtsp://{username}:{password}@{ip_address}/{stream_channel}"
    connect_to_ip_camera(ip_camera_url)
