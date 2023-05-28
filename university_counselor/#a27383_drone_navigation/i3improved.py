import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

from geopy.distance import geodesic


# 假设DME导航台的位置
# 我们将高度设为 0。这意味着我们假设无人机在一个恒定的高度上飞行
dme_stations = np.array(
    [
        [119.679316, 25.934989, 0],  # 福州长乐国际机场
        [119.494418, 25.220857, 0],  # 南日岛
        [118.599816, 24.800826, 0],  # 泉州晋江国际机场
        [118.143639, 24.545038, 0],  # 厦门高崎国际机场
        [118.108445, 24.250145, 0],  # 镇海角
        [117.780122, 23.918635, 0],  # 鸟嘴山
    ]
)


waypoints = np.array(
    [
        [119.490139, 25.221315, 0],  # 南日岛南日镇
        [121.562923, 25.071035, 0],  # 台北市松山机场
        [120.821857, 24.235421, 0],  # 台中市新社机场
        [120.226775, 22.951215, 0],  # 台南市台南机场
        [120.289663, 22.709078, 0],  # 高雄市左营机场
    ]
)


def dme_distance(pos1, pos2):
    return np.linalg.norm(pos1 - pos2)


def dme_dme_position(known_positions, distances):
    print("dme_dme_position:", known_positions, distances)
    A = np.zeros((len(known_positions) - 1, 2))
    b = np.zeros(len(known_positions) - 1)

    for i in range(1, len(known_positions)):
        A[i - 1] = 2 * (known_positions[i] - known_positions[0])[:2]
        b[i - 1] = (
            distances[i] ** 2
            - distances[0] ** 2
            - np.sum((known_positions[i] - known_positions[0]) ** 2)
        )

    position, _ = np.linalg.lstsq(A, b, rcond=None)[:2]
    return np.array([position[0], position[1], 0])


def fly_drone(waypoints, dme_stations):
    # 假设DME距离测量和无人机位置估算是实时进行的
    # 暂时没有添加延迟参数
    actual_positions = []
    estimated_positions = []

    for i in range(len(waypoints) - 1):
        start = waypoints[i]
        end = waypoints[i + 1]
        print(f"从 {start} 飞行至 {end}")

        steps = 500
        for j in range(steps):
            t = j / steps
            position = (1 - t) * start + t * end
            actual_positions.append(position)

            distances = [dme_distance(position, station) for station in dme_stations]
            estimated_position = dme_dme_position(dme_stations, distances)
            estimated_positions.append(estimated_position)

    actual_positions = np.array(actual_positions)
    estimated_positions = np.array(estimated_positions)

    # 计算实际位置和估计位置之间的平均偏移量
    mean_offset = np.mean(actual_positions - estimated_positions, axis=0)
    print(f"实际位置和估计位置之间的平均偏移量为: {mean_offset}")

    return actual_positions, estimated_positions, mean_offset


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def plot_trajectory(
    actual_positions, estimated_positions, mean_offset, animate=False, bg_image=None
):
    if animate:
        n = 20  # Adjust this to a larger number if you want less data
        actual_positions = actual_positions[::n]
        estimated_positions = estimated_positions[::n]

        # Create a function that will do the plotting for a given point i
        def animate(i):
            plt.cla()

            if bg_image is not None:
                # img = plt.imread(bg_image)

                # Load the image
                img = plt.imread(bg_image)

                # Compute the minimum and maximum longitude and latitude
                min_lon = min(
                    np.min(actual_positions[:, 0]), np.min(dme_stations[:, 0])
                )
                max_lon = max(
                    np.max(actual_positions[:, 0]), np.max(dme_stations[:, 0])
                )
                min_lat = min(
                    np.min(actual_positions[:, 1]), np.min(dme_stations[:, 1])
                )
                max_lat = max(
                    np.max(actual_positions[:, 1]), np.max(dme_stations[:, 1])
                )

                # Add a margin
                lon_margin = (max_lon - min_lon) * 0.15  # 5% of the longitude range
                lat_margin = (max_lat - min_lat) * 0.15  # 5% of the latitude range

                # Set the extent of the image to match the data, including the margin
                img_extent = [
                    min_lon - lon_margin,
                    max_lon + lon_margin,
                    min_lat - lat_margin,
                    max_lat + lat_margin,
                ]

                # Display the image with the correct extent
                plt.imshow(img, extent=img_extent)
                # Add lines to represent communication with the DME stations
                drone_position = actual_positions[i]
                for station in dme_stations:
                    plt.plot(
                        [drone_position[0], station[0]],
                        [drone_position[1], station[1]],
                        color="blue",
                        linestyle=":",
                        linewidth=0.5,
                    )
                # Add lines to represent predicted communication with the DME stations
                estimated_position = estimated_positions[i] + mean_offset
                for station in dme_stations:
                    plt.plot(
                        [estimated_position[0], station[0]],
                        [estimated_position[1], station[1]],
                        color="yellow",
                        linestyle="--",
                        linewidth=0.5,
                    )

                    # plt.imshow(img, extent=[np.min(actual_positions[:, 0]), np.max(actual_positions[:, 0]), np.min(actual_positions[:, 1]), np.max(actual_positions[:, 1])])

            corrected_estimated_positions = estimated_positions[:i] + mean_offset
            plt.plot(
                actual_positions[:i, 0],
                actual_positions[:i, 1],
                label="Actual trajectory",
            )
            plt.plot(
                corrected_estimated_positions[:, 0],
                corrected_estimated_positions[:, 1],
                label="Corrected estimated trajectory",
                linestyle="--",
            )
            plt.scatter(
                dme_stations[:, 0],
                dme_stations[:, 1],
                marker="^",
                color="red",
                label="DME stations",
            )

            for i, station in enumerate(dme_stations):
                plt.annotate(
                    f"DME {i+1}",
                    (station[0], station[1]),
                    textcoords="offset points",
                    xytext=(-15, 5),
                    fontsize=9,
                    color="darkred",
                )

            # Add transponder indicator
            for station in dme_stations:
                dist_to_station = np.linalg.norm(actual_positions[i][:2] - station[:2])
                if dist_to_station < 0.01:  # adjust this value as needed
                    plt.scatter(*station[:2], color="green", s=100)
                else:
                    plt.scatter(*station[:2], color="red", s=100)

            plt.xlabel("Longitude")
            plt.ylabel("Latitude")
            plt.legend()
            plt.title(
                "Drone flight trajectory using DME/DME navigation with mean offset compensation"
            )
            plt.grid()

        # Call the animator
        ani = animation.FuncAnimation(
            plt.figure(figsize=(10, 8)),
            animate,
            frames=len(actual_positions),
            interval=1,
        )

        plt.show()

    else:
        # Original static plot
        corrected_estimated_positions = estimated_positions + mean_offset
        plt.figure(figsize=(10, 8))
        plt.plot(
            actual_positions[:, 0], actual_positions[:, 1], label="Actual trajectory"
        )
        plt.plot(
            corrected_estimated_positions[:, 0],
            corrected_estimated_positions[:, 1],
            label="Corrected estimated trajectory",
            linestyle="--",
        )
        plt.scatter(
            dme_stations[:, 0],
            dme_stations[:, 1],
            marker="^",
            color="red",
            label="DME stations",
        )

        for i, station in enumerate(dme_stations):
            plt.annotate(
                f"DME {i+1}",
                (station[0], station[1]),
                textcoords="offset points",
                xytext=(-15, 5),
                fontsize=9,
                color="darkred",
            )

        plt.xlabel("Longitude")
        plt.ylabel("Latitude")
        plt.legend()
        plt.title(
            "Drone flight trajectory using DME/DME navigation with mean offset compensation"
        )
        plt.grid()
        plt.show()


if __name__ == "__main__":
    actual_positions, estimated_positions, mean_offset = fly_drone(
        waypoints, dme_stations
    )
    plot_trajectory(
        actual_positions,
        estimated_positions,
        mean_offset,
        animate=True,
        bg_image="bg.png",
    )
