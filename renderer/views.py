from django.shortcuts import render
from random import randint
from .db import how_many, get_cont_with_id, op_featured, geneate_rand_for_rand

# Create your views here.
def home_(request):
    categories = {"Sandbox": ["/g/sandbox", "box_2.png"], "Real-time strategy (RTS)": ["/g/rts", "strategy_1.png"], "Shooters (FPS and TPS)": ["/g/shooters", "gun_3.png"], "Multiplayer online battle arena (MOBA)": ["/g/moab", "multi_1.png"], "Role-playing (RPG, ARPG, and More)": ["/g/rpg", "role_1.jpg"], "Simulation and sports": ["/g/simulation", "simu_1.png"], "Puzzlers and party games": ["/g/puzzle", "puzzle_1.png"], "Action-adventure": ["/g/action" , "sword_3.png"], "Survival and horror": ["/g/horror", "horror_2.png"], "Platformer": ["/g/platformer", "platform_1.webp"]}
    categories = dict(sorted(categories.items(), key=lambda x:x[1]))
    hot_game_list = get_cont_with_id(geneate_rand_for_rand())
    feature = get_cont_with_id(op_featured())
    #for mock data test i will be using  random games
    random = 7
    featured = 8
    recent = 8 #scrapt for now
    context = {
        "categories": categories,
        "random_games": hot_game_list,
        "featured": feature,
    }
    return render(request, "renderer/index.html", context=context)