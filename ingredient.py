import numpy as np
from bezier import BezierCurve

bloodthorn = BezierCurve(np.array([
    [[0.0, 0.0], [0.0, 0.0], [0.0, -2.0], [0.0, -2.0]],
    [[0.0, -2.0], [0.0, -2.0], [-1.75, 1.0], [-1.75, 1.0]],
    [[-1.75, 1.0], [-1.75, 1.0], [-1.75, -3.0], [-1.75, -3.0]],
    [[-1.75, -3.0], [-1.75, -3.0], [-4.0, 2.0], [-4.0, 2.0]],
    [[-4.0, 2.0], [-4.0, 2.0], [-4.0, -4.0], [-4.0, -4.0]],
    [[-4.0, -4.0], [-4.0, -4.0], [-6.0, 0.0], [-6.0, 0.0]]]))

waterbloom = BezierCurve(np.array([
    [[0.0, 0.0], [0.25, -0.5], [1.0, -0.5], [1.25, 0.0]],
    [[1.25, 0.0], [1.5, 0.5], [2.25, 0.5], [2.5, 0.0]],
    [[2.5, 0.0], [2.75, -0.5], [3.5, - 0.5], [3.75, 0.0]],
    [[3.75, 0.0], [4.0, 0.5], [4.75, 0.5], [5.0, 0.0]]]))

terraria = BezierCurve(np.array([
    [[0.0, 0.0], [0.0, 0.0], [-0.25, -0.75], [0.0, -1.0]],
    [[0.0, -1.0], [0.25, -1.25], [0.5, -1.0], [0.75, -1.25]],
    [[0.75, -1.25], [1, -1.5], [1, -2.25], [0.75, -2.5]],
    [[0.75, -2.5], [0.5, -2.75], [-0.5, -2.25], [-0.75, -2.5]],
    [[-0.75, -2.5], [-1, -2.75], [-1, -3.5], [-0.75, -3.75]],
    [[-0.75, -3.75], [-0.5, -4], [-0.1767767, -3.823223], [0, -4]],
    [[0, -4], [0.25, -4.25], [0, -5], [0, -5]]]))

firebell = BezierCurve(np.array([
    [[0, 0], [-1.25, 1], [-1.25, 1], [-1.25, 1]],
    [[-1.25, 1], [-1.25, 1], [-2.5, 0], [-2.5, 0]],
    [[-2.5, 0], [-2.5, 0], [-3.75, 1], [-3.75, 1]],
    [[-3.75, 1], [-3.75, 1], [-3.75, 1], [-5, 0]]]))

windbloom = BezierCurve(np.array([
    [[0, 0], [0, 0], [1, 2.5], [1, 2.5]],
    [[1, 2.5], [1, 2.5], [-1, 2.5], [-1, 2.5]],
    [[-1, 2.5], [-1, 2.5], [0, 5], [0, 5]]]))

brown_mushroom = BezierCurve(np.array([
    [[0, 0], [0, -1], [0, -1], [-1, -1]],
    [[-1, -1], [-2, -1], [-2, -1], [-2, -2]],
    [[-2, -2], [-2, -3], [-2, -3], [0, -3]],
    [[0, -3], [2, -3], [2, -3], [2, -4]],
    [[2, -4], [2, -5], [2, -5], [0.5, -5]],
    [[0.5, -5], [0, -5], [0, -5], [0, -6]]]))

tangleweed = BezierCurve(np.array([
    [[0, 0], [0, -1], [3, -1], [3, 0]],
    [[3, 0], [3, 1], [1.5, 1], [1.5, 0]],
    [[1.5, 0], [1.5, -1], [3, -2], [4, 0]],
    [[4, 0], [5, 2], [6.5, 1], [6.5, 0]],
    [[6.5, 0], [6.5, -1], [5, -1], [5, 0]],
    [[5, 0], [5, 1], [8, 1], [8, 0]]]))

green_mushroom = BezierCurve(np.array([
    [[0, 0], [3.02107, 1.020414], [0.5508628, -1.518064], [1.527383, -2.506451]],
    [[1.527383, -2.506451], [2.500548, -3.491441], [5.012281, -0.9910625], [3.996144, -3.978157]]]))

dryads_saddle = BezierCurve(np.array([
    [[0, 0], [-0.25, 0], [-1.33541, -0.3291796], [-1, -1]],
    [[-1, -1], [-0.5, -2], [2, -0.5], [2, -2]],
    [[2, -2], [2, -3.5], [-2, -1.25], [-2, -3]],
    [[-2, -3], [-2, -3.75], [0, -3.75], [0, -3.75]]]))

shadow_chanterelle = BezierCurve(np.array([
    [[0, 0], [3, 0], [0, 5], [3, 5]],
    [[3, 5], [4, 5], [4.5, 4], [4.5, 3]]]))

hairy_banana = BezierCurve(np.array([
    [[0, 0], [0, 0], [-3, -3], [-4, -3]],
    [[-4, -3], [-5, -3], [-8.0, 0], [-8, 0]],
    [[-8, 0], [-7, 0.25], [-5, -1.25], [-4, -1]]]))

ice_fruit = BezierCurve(np.array([
    [[0, 0], [0, 0], [1, 2], [1, 2]],
    [[1, 2], [1, 2], [3, -2], [3, -2]],
    [[3, -2], [3, -2], [5, 2], [5, 2]],
    [[5, 2], [5, 2], [6, 0], [6, 0]]]))

goblin_shroom = BezierCurve(np.array([
    [[0, 0], [3, 0], [3, -5], [0, -5]]]))

marshroom = BezierCurve(np.array([
    [[0, 0], [2, -2], [1, -4], [3, -4]],
    [[3, -4], [3.5, -4], [5, -4], [5, -3]]]))

weirdshroom = BezierCurve(np.array([
    [[0, 0], [-2, 0], [-2, -6], [-1, -6]],
    [[-1, -6], [0.25, -6], [1.353553, -6.207107], [1, -5.5]],
    [[1, -5.5], [0.5, -4.5], [-0.25, -3.75], [0, -3]]]))

thornstick = BezierCurve(np.array([
    [[0, 0], [0, 0], [-4, -6], [-4, -6]],
    [[-4, -6], [-4, -6], [-2, -5], [-2, -5]]]))

thunder_thistle = BezierCurve(np.array([
    [[0, 0], [0, 0], [2, 3.5], [2, 3.5]],
    [[2, 3.5], [2, 3.5], [-1, 2.5], [-1, 2.5]],
    [[-1, 2.5], [-1.0, 2.5], [1.0, 6], [1, 6]]]))

lava_root = BezierCurve(np.array([
    [[0, 0], [0, 1.5], [-2.5, 1.5], [-2.5, 0]],
    [[-2.5, 0], [-2.5, -1.5], [-5, -1.5], [-5, 0]],
    [[-5, 0], [-5, 1.5], [-7.5, 1.5], [-7.5, 0]],
    [[-7.5, 0], [-7.5, -0.75], [-6.25, -0.75], [-6.25, 0]]]))

sulphur_shelf = BezierCurve(np.array([
    [[0, 0], [-2, 0], [-3.5, 0], [-3.5, 0.75]],
    [[-3.5, 0.75], [-3.5, 1.5], [-2.75, 1.5], [-2.25, 1.5]],
    [[-2.25, 1.5], [-1.75, 1.5], [-1, 1.5], [-1, 2.25]],
    [[-1, 2.25], [-1, 3], [-2.5, 3], [-4.5, 3]]]))

goldthorn = BezierCurve(np.array([
    [[0, 0], [-0.25, 0], [-0.5, 0.25], [-0.5, 0.5]],
    [[-0.5, 0.5], [-0.5, 0.75], [-0.25, 1], [0, 1]],
    [[0, 1], [1, 1], [1, 0.5], [1, 0]],
    [[1, 0], [1, -0.5], [0.5, -1], [0, -1]],
    [[0, -1], [-0.75, -1], [-1.5, -0.25], [-1.5, 0.25]],
    [[-1.5, 0.25], [-1.5, 1.75], [-0.75, 2], [0, 2]],
    [[0, 2], [1.25, 2], [2, 1.25], [2, 0]],
    [[2, 0], [2, -1], [1, -2], [0, -2]]]))

witch_mushroom = BezierCurve(np.array([
    [[0, 0], [0, 4], [5, 1], [5, 5]]]))

grave_truffle = BezierCurve(np.array([
    [[0.0, 0.0], [0.0, 0.0], [-3.0, -2.0], [-3.0, -2.0]],
    [[-3.0, -2.0], [-3.0, -2.0], [-0.8, -7.0], [-0.8, -7.0]],
    [[-0.8, -7.0], [-0.7, -7.0], [0.7, -7.0], [0.8, -7.0]],
    [[0.8, -7.0], [0.8, -7.0], [3.0, -2.0], [3.0, -2.0]],
    [[3.0, -2.0], [3.0, -2.0], [0.0, -1.3], [0.0, -1.3]],
    [[0.0, -1.3], [0.0, -1.3], [0.0, -5.0], [0.0, -5.0]]]))

lumpy_beet = BezierCurve(np.array([
    [[0.0, 0.0], [0.0, 2.0], [3.0, 1.0], [3.0, 3.0]],
    [[3.0, 3.0], [3.0, 4.0], [1.0, 4.0], [1.0, 3.0]],
    [[1.0, 3.0], [1.0, 2.0], [1.0, 1.0], [1.0, 0.0]],
    [[1.0, 0.0], [1.0, -1.0], [3.0, -1.0], [3.0, 0.0]],
    [[3.0, 0.0], [3.0, 1.0], [3.0, 2.0], [4.0, 2.0]]]))

red_mushroom = BezierCurve(np.array([
    [[0.0, 0.0], [-4.0, 4.0], [-4.0, -4.0], [-8.0, 0.0]]]))

blood_ruby = BezierCurve(np.array([
    [[0.0, 0.0], [0.0, 0.0], [-3.0, -3.0], [-3.0, -3.0]],
    [[-3.0, -3.0], [-3.0, -3.0], [-3.0, 3.0], [-3.0, 3.0]],
    [[-3.0, 3.0], [-3.0, 3.0], [-6.0, 0.0], [-6.0, 0.0]]]))

cloud_crystal = BezierCurve(np.array([
    [[0.0, 0.0], [0.0, 0.0], [-0.8, 1.0], [0.0, 1.5]],
    [[0.0, 1.5], [0.7, 2.0], [1.0, 2.0], [1.0, 2.8]],
    [[1.0, 2.8], [1.0, 3.8], [-1.0, 3.3], [-1.0, 4.3]],
    [[-1.0, 4.3], [-1.0, 5.0], [-0.8, 5.0], [0.0, 5.5]],
    [[0.0, 5.5], [0.7, 6.0], [0.0, 7.0], [0.0, 7.0]]]))

earth_pyrite = BezierCurve(np.array([
    [[0.0, 0.0], [0.0, 0.0], [0.0, -1.5], [0.0, -1.5]],
    [[0.0, -1.5], [0.0, -1.5], [-1.0, -1.5], [-1.0, -1.5]],
    [[-1.0, -1.5], [-1.0, -1.5], [-1.0, -3.5], [-1.0, -3.5]],
    [[-1.0, -3.5], [-1.0, -3.5], [1.0, -3.5], [1.0, -3.5]],
    [[1.0, -3.5], [1.0, -3.5], [1.0, -5.5], [1.0, -5.5]],
    [[1.0, -5.5], [1.0, -5.5], [0.0, -5.5], [0.0, -5.5]],
    [[0.0, -5.5], [0.0, -5.5], [0.0, -7.0], [0.0, -7.0]]]))

fire_citrine = BezierCurve(np.array([
    [[0.0, 0.0], [0.0, 0.0], [-0.8, -1.5], [-1.5, 0.0]],
    [[-1.5, 0.0], [-2.5, 2.0], [-2.8, -0.7], [-3.5, -0.8]],
    [[-3.5, -0.8], [-4.3, -0.8], [-4.5, 2.0], [-5.5, 0.0]],
    [[-5.5, 0.0], [-6.3, -1.5], [-7.0, 0.0], [-7.0, 0.0]]]))

frost_sapphire = BezierCurve(np.array([
    [[0.0, 0.0], [0.0, 0.0], [0.3, 0.5], [0.3, 0.5]],
    [[0.3, 0.5], [0.3, 0.5], [1.0, -1.0], [1.0, -1.0]],
    [[1.0, -1.0], [1.0, -1.0], [2.0, 1.0], [2.0, 1.0]],
    [[2.0, 1.0], [2.0, 1.0], [3.0, -1.0], [3.0, -1.0]],
    [[3.0, -1.0], [3.0, -1.0], [4.0, 1.0], [4.0, 1.0]],
    [[4.0, 1.0], [4.0, 1.0], [5.0, -1.0], [5.0, -1.0]],
    [[5.0, -1.0], [5.0, -1.0], [6.0, 1.0], [6.0, 1.0]],
    [[6.0, 1.0], [6.0, 1.0], [6.8, -0.5], [6.8, -0.5]],
    [[6.8, -0.5], [6.8, -0.5], [7.0, 0.0], [7.0, 0.0]]]))

all_ingredients = [waterbloom, terraria, firebell, windbloom, bloodthorn, brown_mushroom, tangleweed, green_mushroom,
                   dryads_saddle, shadow_chanterelle, hairy_banana, ice_fruit, goblin_shroom, marshroom, weirdshroom,
                   thornstick, lava_root, sulphur_shelf, goldthorn, witch_mushroom, thunder_thistle, grave_truffle,
                   lumpy_beet, red_mushroom, blood_ruby, cloud_crystal, earth_pyrite, fire_citrine, frost_sapphire]



all_ingredient_names = ["waterbloom", "terraria", "firebell", "windbloom", "bloodthorn", "brown_mushroom", "tangleweed",
                        "green_mushroom", "dryads_saddle", "shadow_chanterelle", "hairy_banana", "ice_fruit",
                        "goblin_shroom", "marshroom", "weirdshroom", "thornstick", "lava_root", "sulphur_shelf",
                        "goldthorn", "witch_mushroom", "thunder_thistle", "grave_truffle", "lumpy_beet", "red_mushroom",
                        "blood_ruby", "cloud_crystal", "earth_pyrite", "fire_citrine", "frost_sapphire"]
