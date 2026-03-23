import pygame
import random
import math

#i initlized pygame and the pygame mixer for music and sound effects
pygame.init()
pygame.mixer.init()
pygame.mixer.set_num_channels(600) # change this depending on the atoms and neutrons number so the sound isnt going to be delayed
#also if the number are generaly bigger than 15 consider deleting the sound effects all togther 

#i loaded the background music you can delete this part or add your own mp3 file!
pygame.mixer.music.load("sounds/UpPiano.mp3")
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)
#the sound effects for the ball hitting the wall, you can also delete this or change it and delete the hit.play() part
hit = pygame.mixer.Sound("sounds/8-Bit Hit.mp3")
hit.set_volume(0.01)
#the sound effect when the neutron hits the atom, you can also delete this or change it and delete the hit.play() part
atom_hit = pygame.mixer.Sound("sounds/special hit.mp3")
atom_hit.set_volume(0.01)
#the game settings and variables
resolution = 800, 850
screen = pygame.display.set_mode(resolution)
pygame.display.set_caption("Neutrons fission simulation")
click = pygame.time.Clock()
flashes = []
green_neutron_counter = 0
number = 0
hue = 0
text_font = pygame.font.SysFont("Times New Roman", 35)
text_font2 = pygame.font.SysFont("Comic Sans", 20)
running = True
dashboard = pygame.Rect(0, 600, 800, 300)
def text(text, font, color, x, y):
    image = font.render(text, True, color)
    screen.blit(image, (x, y))
#the list that holds the neutrons and atoms
neutrons = []
atoms = []


#i created neutrons with random positions and speed and added them to the list so i can draw them! change range to add more or less neutrons!
for i in range(50):
    neutrons.append({
        "x": random.randint(5, 795),
        "y": random.randint(5, 595),
        "xv": random.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]),
        "yv": random.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]),
        "color" : (137, 207, 240)
    })
#i created atoms with random positions and added them to the list so i can draw them! change range to add more or less atoms!
for i in range(20):
    atoms.append({
        "x": random.randint(5, 795),
        "y": random.randint(5, 595),
        "xv": random.choice([-2, -1, 1, 2]),
        "yv": random.choice([-2, -1, 1, 2])
    })
#i created a function to check if the neutron hit the atom or not
def colide(neutron, atom):
    x = neutron["x"] - atom["x"]
    y = neutron["y"] - atom["y"]
    distance = math.sqrt(x**2 + y**2)
    if distance <= 12:
        return True
    else:
        return False



while running:
    for event in  pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                if number % 2 == 0:
                    neutrons = [{"x": random.randint(5, 795), "y": random.randint(5, 595), "xv": random.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]), "yv": random.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]), "r": 5, "color": (137, 207, 240)} for _ in range(50)]
                    atoms = [{"x": random.randint(5,795), "y": random.randint(5,595),"xv": random.choice([-2, -1, 1, 2]), "yv": random.choice([-2, -1, 1, 2]), "r": 18} for _ in range(30)]
                else:
                    neutrons = [{"x": random.randint(5, 795), "y": random.randint(5, 595), "xv": random.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]), "yv": random.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]), "r": 5, "color": (137, 207, 240)} for _ in range(50)]
                    atoms = [{"x": random.randint(5,795), "y": random.randint(5,595),"xv": (0), "yv": (0), "r": 18} for _ in range(30)]
                flashes = []
                green_neutron_counter = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                if number % 2 == 0:
                    neutrons = [{"x": random.randint(5, 795), "y": random.randint(5, 595), "xv": random.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]), "yv": random.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]), "r": 5, "color": (137, 207, 240)} for _ in range(50)]
                    atoms = [{"x": random.randint(5,795), "y": random.randint(5,595),"xv": (0), "yv": (0), "r": 18} for _ in range(30)]
                else:
                    neutrons = [{"x": random.randint(5, 795), "y": random.randint(5, 595), "xv": random.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]), "yv": random.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]), "r": 5, "color": (137, 207, 240)} for _ in range(50)]
                    atoms = [{"x": random.randint(5,795), "y": random.randint(5,595),"xv": random.choice([-2, -1, 1, 2]), "yv": random.choice([-2, -1, 1, 2]), "r": 18} for _ in range(30)]
                number += 1
                green_neutron_counter = 0


        if event.type == pygame.QUIT:
          pygame.mixer.music.stop()
          running = False
        

    screen.fill((45, 56, 58))
    dead_flashes = []
    for f in flashes:
        f["r"] += 1
        f["alpha"] -= 5
        if f["alpha"] <= 0:
            flashes.remove(f)
            continue
        surf = pygame.Surface((f["r"]*2, f["r"]*2), pygame.SRCALPHA)
        pygame.draw.circle(surf, (255, 200, 80, f["alpha"]),
                        (f["r"], f["r"]), f["r"])
        screen.blit(surf, (f["x"] - f["r"], f["y"] - f["r"]))
    #a cool rainbow effect i have read about and wanted to try it out
    hue += 1
    r = int((math.sin(math.radians(hue)) * 127) + 128)
    g = int((math.sin(math.radians(hue + 120)) * 127) + 128)
    b = int((math.sin(math.radians(hue + 240)) * 127) + 128)
    #drawing the dashboard and the text on it, you can change the text and the colors if you want to (don't mind the spaces in the text)
    pygame.draw.rect(screen, ("black"), dashboard)
    if number % 2 == 0:
        text("gas mode", text_font, (0, 128, 0), 600, 620)
    else:
        text("nuclear mode", text_font, (0, 128, 0), 600, 620)
    text("Neutrons: " + str(len(neutrons)), text_font, (0, 128, 0), 0, 650)
    text("Atoms: " + str(len(atoms)), text_font, (0, 128, 0), 0, 700)
    text("New neutrons \nfrom the fission: " + str(green_neutron_counter), text_font, (0, 128, 0), 0, 750)
    text("|-------------------------------------CONTROLS-----------------------------------------------|", text_font2, (0, 128, 0), 0, 600)
    text("|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|", text_font2, (0, 128, 0), 280, 615)
    text("                  change game mode:\n 'f' for nuclear reactor mode (atoms dont move)\n and 'r' for gas mode (atoms move)", text_font2, (0, 128, 0), 300, 630)
    if len(atoms) == 0:
        text("            All atoms have been hit!\n                thank's for playing!\n            change modes or restart!\n", text_font2, (0, 128, 0), 300, 720)
    text("simulation by: Rih Mohamed Islam", text_font2, (r, g, b), 480, 820)
    #for every neutron in that list i update his position and check if he hit the wall!
    for neutron in neutrons:
        neutron["x"] += neutron["xv"]
        neutron["y"] += neutron["yv"]
        if neutron["x"] >= 795 or neutron["x"] <= 5:
            hit.play()
            neutron["xv"] = -neutron["xv"]
        if neutron["y"] >= 595 or neutron["y"] <= 5:
            hit.play()
            neutron["yv"] = -neutron["yv"]
        # in here i needed to put [:] to avoid an index error when i remove an atom while iterating
        for atom in atoms[:]:
            if colide(neutron, atom) and len(atoms) != 0:
                atom_hit.play()
                atoms.remove(atom)
                green_neutron_counter += 1
                flashes.append({"x": atom["x"], "y": atom["y"], "r": 5, "alpha": 255})
                for i in range(2):
                    neutrons.append({
                        "x": atom["x"],
                        "y": atom["y"],
                        "xv": random.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]),
                        "yv": random.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]),
                        "color" : (0, 100, 0)
                    })
        pygame.draw.circle(screen, neutron["color"], (neutron["x"], neutron["y"]), 5)
    #for every atom in that list i update his position and check if he hit the wall!
    for atom in atoms:
        atom["x"] += atom["xv"]
        atom["y"] += atom["yv"]
        if atom["x"] >= 795 or atom["x"] <= 5:
            hit.play()
            atom["xv"] = -atom["xv"]
        if atom["y"] >= 595 or atom["y"] <= 5:
            hit.play()
            atom["yv"] = -atom["yv"]
        pygame.draw.circle(screen, (144, 238, 144), (atom["x"], atom["y"]), 7)

    pygame.display.flip()
    click.tick(60)

pygame.quit()
