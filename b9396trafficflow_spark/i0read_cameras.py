import time
import multiprocessing as mp
import cv2

from i1rabbitmq import sender
import i2rabbitmq_config


def image_put(q, user, pwd, ip, channel=1):
    #     cap = cv2.VideoCapture("rtsp://%s:%s@%s//Streaming/Channels/%d" % (user, pwd, ip, channel))
    #     if cap.isOpened():
    #         print('HIKVISION')
    #     else:
    #         cap = cv2.VideoCapture("rtsp://%s:%s@%s/cam/realmonitor?channel=%d&subtype=0" % (user, pwd, ip, channel))
    #         print('DaHua')
    video_url = ""
    if ip == "192.168.0.1":
        video_url = "mock_cameras/mock_intersection0.mp4"
    elif ip == "192.168.0.2":
        video_url = "mock_cameras/mock_intersection1.mp4"
    elif ip == "192.168.0.3":
        video_url = "mock_cameras/mock_intersection2.mp4"
    cap = cv2.VideoCapture(video_url)

    while True:
        q.put(cap.read()[1])
        q.get() if q.qsize() > 1 else time.sleep(0.1)


def image_get(q, window_name):
    # 通过timeF控制多少帧数真正读取1帧到队列中
    timeF = 15
    count = 1
    cv2.namedWindow(window_name, flags=cv2.WINDOW_FREERATIO)
    while True:
        frame = q.get()
        # 只有frame有长宽，才是有意义的输入的情况
        if frame is not None and frame.shape[1] > 0 and frame.shape[0] > 0:
            cv2.imshow(window_name, frame)
            cv2.waitKey(1)
            count += 1
            if count % timeF == 0:
                sender(
                    i2rabbitmq_config.Where_This_Server_ReadFrom,
                    frame,
                    window_name,
                    "LifeJacket",
                )


def run_multi_camera():
    user_name, user_pwd = "admin", "passwordtest"
    camera_ip_l = [
        "192.168.0.1",
        "192.168.0.2",
        "192.168.0.3",
    ]

    mp.set_start_method(method="spawn")  # init
    queues = [mp.Queue(maxsize=4) for _ in camera_ip_l]

    processes = []
    for queue, camera_ip in zip(queues, camera_ip_l):
        processes.append(
            mp.Process(target=image_put, args=(queue, user_name, user_pwd, camera_ip))
        )
        processes.append(mp.Process(target=image_get, args=(queue, camera_ip)))

    for process in processes:
        process.daemon = True
        process.start()
    for process in processes:
        process.join()


def run():
    run_multi_camera()
    # with 1 + n threads
    pass


if __name__ == "__main__":
    run()
