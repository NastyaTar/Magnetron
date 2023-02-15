import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.lines import Line2D
import subprocess
import os


def cycloid(R, v, t, w):
    '''Уравнение циклоиды'''
    return np.array([(v * t - R * np.sin(w * t)), (R * (1 - np.cos(w * t)))])

    # укажем директорию, в которую будем # сохранять сгенерированные картинки FOLDER = 'cycloid'


FOLDER = 'cycloid'


def model_cycloid(R, v, w):
    try:
        os.mkdir(FOLDER)
    except FileExistsError:
        pass
    fig18 = plt.figure(1)
    ax01 = fig18.add_subplot(1, 1, 1)
    ax01.set_aspect('equal')
    # радиус генерирующей окружности
    # R = 1.0
    final_t = 30
    # h = 3.0
    final_x, _ = cycloid(R, v, final_t, w)
    for counter, last_t in enumerate(np.arange(0.0, final_t + 0.1, 0.1)):
        # стираем все, что было на картинке
        ax01.clear()
        T = np.linspace(0.0, last_t, 1000)
        X, Y = cycloid(R, v, T, w)
        # последняя точка кривой
        last_x, last_y = cycloid(R, v, T[-1], w)
        # # Генерирующая окружность с центром в точке (Rt, R)
        # circ = mpatches.Circle((R * T[-1], R), R, fill=False, color='black')
        # Точка на катящейся окружности
        last_point = mpatches.Circle((last_x, last_y), 0.05, color='black')
        # stick = Line2D([R * T[-1], last_x], [R, last_y], color='k')
        # задаем границы осей
        ax01.set_xlim(right=final_x + 3 * R)
        ax01.set_ylim([-R, 4 * R])
        # рисуем циклоиду
        ax01.plot(X, Y, linestyle='--')
        # добавляем на картинку точку и окружность
        ax01.add_patch(last_point)
        # ax01.add_patch(circ)
        # ax01.add_line(stick)

        fig18.savefig('{0}/{1:03d}.png'.format(FOLDER, counter), dpi=300, format='png')

    CMD = ['/Users/a789/Downloads/science1/ffmpeg', '-y', '-r', '30', '-f', 'image2', '-i',
           '{0}/%03d.png'.format(FOLDER),
           '-vcodec', 'libx264', '-crf',
           '25', '-pix_fmt', 'yuv420p', 'cycloid.mp4']
    subprocess.run(CMD)
    cycloid_done = True
