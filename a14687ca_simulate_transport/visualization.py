import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import cv2


def show_img(image_path):
    new_img = cv2.imread(image_path)
    plt.title("City original geographical_urban 2D Map")
    plt.imshow(new_img)
    plt.show()


def show_simplify_to_path():
    df1 = pd.DataFrame(np.random.randint(0, 15, size=(15, 1)))

    df2 = pd.DataFrame(np.random.randint(20, 35, size=(10, 1)))

    df3 = pd.DataFrame(np.random.randint(15, 20, size=(12, 1)))

    frames = [df1, df2, df3]
    result = pd.DataFrame(pd.concat(frames))

    df3 = result.cumsum()
    df3 = df3.reset_index(drop=False)
    print(df3)
    ax = df3.iloc[:15, :].plot(y=0, color="gray")
    df3.iloc[15:20].plot(y=0, color="red", ax=ax)
    df3.iloc[20:, :].plot(y=0, color="blue", ax=ax)

    plt.title("Simplify City geographical_urban to 3-lane Path ")
    plt.savefig("i2show_simplify_to_path.png")
    plt.show()


def visulize_to_png(x, y):

    plt.close()
    plt.plot(x, y)

    # Add title and axis names
    plt.title("total-driving-distance /electronic-car+fast_through_area_ratio rate")
    plt.xlabel("electronic-car+fast_through_area_ratio rate")
    plt.ylabel("total-driving-distance")

    plt.savefig("i3result_comparison.png")
    plt.show()
