# coding: utf-8
# license: GPLv3

from solar_objects import Star, Planet


def read_space_objects_data_from_file(input_filename):
    """Cчитывает данные о космических объектах из файла, создаёт сами объекты
    и вызывает создание их графических образов

    Параметры:

    **input_filename** — имя входного файла
    """

    objects = []
    with open(input_filename) as input_file:
        for line in input_file:
            if len(line.strip()) == 0 or line[0] == '#':
                continue  # пустые строки и строки-комментарии пропускаем
            object_type = line[0].lower()
            if object_type == "s":
                star = Star()
                parse_star_parameters(line, star)
                objects.append(star)
            elif object_type == "p":
                planet = Planet()
                parse_planet_parameters(line, planet)
                objects.append(planet)

    return objects


def parse_star_parameters(line, star):
    """Считывает данные о звезде из строки.
    Входная строка должна иметь слеюущий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Здесь (x, y) — координаты зведы, (Vx, Vy) — скорость.
    Пример строки:
    Star 10 red 1000 1 2 3 4

    Параметры:

    **line** — строка с описание звезды.
    **star** — объект звезды.
    """

    list = line.split()

    star.type = list[0].lower()
    star.R = float(format(float(list[1]), "f"))
    star.color = list[2]
    star.m = float(format(float(list[3]), "f"))
    star.x = float(format(float(list[4]), "f"))
    star.y = float(format(float(list[5]), "f"))
    star.Vx = float(format(float(list[6]), "f"))
    star.Vy = float(format(float(list[7]), "f"))


def parse_planet_parameters(line, planet):
    """Считывает данные о планете из строки.
    Предполагается такая строка:
    Входная строка должна иметь слеюущий формат:
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Здесь (x, y) — координаты планеты, (Vx, Vy) — скорость.
    Пример строки:
    Planet 10 red 1000 1 2 3 4

    Параметры:

    **line** — строка с описание планеты.
    **planet** — объект планеты.
    """

    list = line.split()

    planet.type = list[0].lower()
    planet.R = int(list[1])
    planet.color = list[2]
    planet.m = int(list[3])
    planet.x = int(list[4])
    planet.y = int(list[5])
    planet.Vx = int(list[6])
    planet.Vy = int(list[7])


def write_space_objects_data_to_file(output_filename, space_objects):
    """Сохраняет данные о космических объектах в файл.
    Строки должны иметь следующий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Параметры:

    **output_filename** — имя входного файла
    **space_objects** — список объектов планет и звёзд
    """
    with open(output_filename, 'w') as out_file:
        for obj in space_objects:
            if obj.type == "star":
                type = "Star"
            if obj.type == "planet":
                type = "Planet"
            rad = str(obj.R)
            color = obj.color
            mass = str(obj.m)
            x = str(obj.x)
            y = str(obj.t)
            vx = str(obj.Vx)
            vy = str(obj.Vy)
            print(out_file, type, rad, color, mass, x, y, vx, vy, sep=' ')


# FIXME: хорошо бы ещё сделать функцию, сохранающую статистику в заданный файл...

if __name__ == "__main__":
    print("This module is not for direct call!")
