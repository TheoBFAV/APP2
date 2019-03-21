"""
Module qui gère le robot Curiosity.

Les méthodes utilisables par l'interprète sont les suivante:

    cur.avance()
    cur.gauche()
    cur.droite()
    cur.mesure(direction)
    => renvoie un entier

    cur.pose(booléen)

    cur.debug()
    => Affiche sur la console la position et l'orientation de Curiosity

"""

import time

class CibleAtteinte(Exception):
    pass

PLAIN = 0
MARK  = 1
WATER = 2
ROCK  = 3


FORWARD = 1
BACKWARD = 5
LEFT = 7
RIGHT = 3

DSTEP  = 40 ## peut être descendu à 20 pour labyrinthe
ANGLE  = 90

SHWATER = "imgs/water.gif"
SHROVERE = "imgs/roverE.gif"
SHROVERW = "imgs/roverW.gif"
SHROVERS = "imgs/roverS.gif"
SHROVERN = "imgs/roverN.gif"
SHROCK  = "imgs/rock.gif"
SHTARGET= "imgs/flag.gif"
SHMARK  = "imgs/checkmark.gif"

WAIT_EACH_STEP = True

def clicked(x, y):
    global waiting
    print('clicked at %f %f' % (x,y))
    waiting = False
    return

def wait_for_click(win):
    return
    # code below is not working, don't know why though...
    input('Press enter to continue: ')

    global waiting
    waiting = True
    win.listen()
    mainloop()
    return


class Curiosity:

    x = 0
    y = 0
    target_x = 0
    target_y = 0
    orient = 3

    largeur = 0
    hauteur = 0

    ascii_mode = False

    def _selectRoverShape(self):
        if self.ascii_mode:
            return
        if self.orient == 1:
            self.turtle.shape(SHROVERN)
        elif self.orient == 3:
            self.turtle.shape(SHROVERE)
        elif self.orient == 5:
            self.turtle.shape(SHROVERS)
        elif self.orient == 7:
            self.turtle.shape(SHROVERW)
        else:
            raise ValueError("Direction impossible!")


    """Orientations
      8   1   2
          ^
      7 < 0 > 3
          v
      6   5   4
    """

    carte = None

    def __init__(self, ascii_mode=False):
        self.ascii_mode = ascii_mode
        if not ascii_mode:
            self.turtle = __import__('turtle')

            self.win = self.turtle.Screen()
            self.win.register_shape(SHWATER)
            self.win.register_shape(SHROVERE)
            self.win.register_shape(SHROVERW)
            self.win.register_shape(SHROVERN)
            self.win.register_shape(SHROVERS)
            self.win.register_shape(SHROCK)
            self.win.register_shape(SHTARGET)
            self.win.register_shape(SHMARK)
            self.win.onclick(clicked)

    def pos(self, x, y):
        if self.ascii_mode:
            return
        self.turtle.goto ((x - self.largeur/2) * DSTEP, (self.hauteur/2 - y)*DSTEP)

    def affiche_carte_ascii(self):
        print ("Hauteur: ", self.hauteur, " Largeur: ", self.largeur)
        for y in range (0, self.hauteur):
            ligne = ""
            for x in range (0, self.largeur):
                if y == self.y and x == self.x:
                    ligne += 'C'
                    continue
                if y == self.target_y and x == self.target_x:
                    ligne += '@'
                    continue
                t = self.carte[y][x]
                if t == PLAIN:
                    ligne += '.'
                if t == MARK:
                    ligne += 'M'
                elif t == ROCK:
                    ligne += '#'
                elif t == WATER:
                    ligne += '~'
            print (ligne)


    def reset(self, carte):

        if not self.ascii_mode:
            self.turtle.reset()

        self.hauteur = len(carte)
        self.largeur = len(carte[0])

        print ("largeur: ", self.largeur)

        self.carte = []
        self.marques = []
        self.init_marques = []

        # print ("asciimode: ", self.ascii_mode)
        if not self.ascii_mode:

            self.turtle.up ()
            # turtle.tracer(0, 0) then at the end do turtle.update()
            save_tracer = self.turtle.tracer(0,0)
            # on dessine des murs
            self.turtle.speed(-1)
            self.turtle.shape(SHROCK)
            for x in range (-1, self.largeur+1):
                self.pos (x, -1)
                self.turtle.stamp()
                self.pos (x, self.hauteur)
                self.turtle.stamp()
            for y in range (0, self.hauteur):
                self.pos (-1, y)
                self.turtle.stamp()
                self.pos (self.largeur, y)
                self.turtle.stamp()


        y = -1
        x = -1

        def stamp_it(st):
            if self.ascii_mode:
                return
            self.pos (x, y)
            self.turtle.shape(st)
            self.turtle.stamp()


        y = -1
        for line in carte:
            self.carte.append([])
            self.marques.append([])
            x = -1
            y += 1
            if len(line) != self.largeur:
                raise ValueErreur ('Mauvaise longueur de ligne pour la carte!')
            for char in line:
                x += 1
                self.marques[y].append(None)
                if char == '.':
                    self.carte[y].append(PLAIN)
                elif char == 'M':
                    self.carte[y].append(PLAIN)
                    self.init_marques.append((x,y))
                elif char == '#':
                    self.carte[y].append(ROCK)
                    stamp_it (SHROCK)
                elif char == '~':
                    self.carte[y].append(WATER)
                    stamp_it (SHWATER)
                elif char == '@':
                    self.carte[y].append(PLAIN)
                    self.target_x = x
                    self.target_y = y
                    stamp_it (SHTARGET)
                    # print ("Target found at ", x, 'x', y)
                elif char == 'C':
                    self.carte[y].append(PLAIN)
                    self.x = x
                    self.y = y
                elif char == 'P':
                    self.carte[y].append(PLAIN)
                    self.x = x
                    self.y = y
                    self.init_marques.append((x,y))

                    # print ("Curiosity found at ", x, 'x', y)
                elif char == '\n':
                    break
                else:
                    raise ValueError("Caractère interdit: " + char)




        self.orient = 3
        self.pos (self.x, self.y)

        if not self.ascii_mode:
            # down()
            self._selectRoverShape()
            # speed(3)
            # speed(0)
            self.turtle.speed(3)
            # tracer(save_tracer)
            self.turtle.tracer(1,10)

    def __abs_direction__(self, direct):
        if direct == 0:
            dx = 0
            dy = 0
        elif direct == 1:
            dx = 0
            dy = -1
        elif direct == 2:
            dx = 1
            dy = -1
        elif direct == 3:
            dx = 1
            dy = 0
        elif direct == 4:
            dx = 1
            dy = 1
        elif direct == 5:
            dx = 0
            dy = 1
        elif direct == 6:
            dx = -1
            dy = 1
        elif direct == 7:
            dx = -1
            dy = 0
        elif direct == 8:
            dx = -1
            dy = -1
        else:
            raise RuntimeError("Direction invalide")
        return (dx, dy)

    def __direction__(self, direct):
        if direct == 0:
            return (0, 0)

        abs_dir = (direct - 1 + self.orient - 1) % 8 + 1
        return self.__abs_direction__(abs_dir)

    def __cible(self):
        flag = self.x == self.target_x and self.y == self.target_y
        return flag

    def _cible(self):
        if self.__cible():
            print ("Cible atteinte!")
            self.affiche_carte_ascii()
            raise CibleAtteinte("Victoire")
            return True
        return False

    def cible(self):
        return self.__cible()

        return flag

    def succes (self):
        if not self.__cible():
            print ("******************************************")
            print ("*        ERREUR                          *")
            print ("* Curiosity n'est pas au bon endroit !   *")
            return False

        # vérifier les marques
        manque = False
        for (mx, my) in self.init_marques:
            if self.carte[my][mx] != MARK:
                if not manque:
                    print ("******************************************")
                    print ("*        ERREUR                          *")
                    print ("* marque(s) manquante(s)                 *")
                    manque = True
                print ("- marque manquante position: ", mx, "x", my)

        if manque:
            return False

        compte = 0
        for y in range (0, self.hauteur):
            for x in range (0, self.largeur):
                if self.carte[y][x] == MARK:
                    compte += 1

        if compte != len(self.init_marques):
            print ("******************************************")
            print ("*        ERREUR                          *")
            print ("Trop de marques sur la carte")
            return False

        return True



    def attendre(self):
        if self.ascii_mode:
            return
        wait_for_click(self.win)

    def gauche(self):
        self.orient = (self.orient - 2 + 8 - 1) % 8 + 1
        self._selectRoverShape()
        # tilt (ANGLE)
        if not self.ascii_mode:
            self.turtle.left (ANGLE)
        if WAIT_EACH_STEP: self.attendre()

    def droite(self):
        self.orient = (self.orient + 2 - 1) % 8 + 1
        self._selectRoverShape()
        # tilt  (-ANGLE)
        if not self.ascii_mode:
            self.turtle.right (ANGLE)
        if WAIT_EACH_STEP: self.attendre()

    def avance(self):
        (dx, dy) = self.__direction__(FORWARD)
        # print ("dx and dy are ", end="")
        # print (dx, end="")
        # print (' - ', end="")
        # print (dy)
        newx = self.x+dx
        newy = self.y+dy

        if newx < 0 or newx >= self.largeur or \
           newy < 0 or newy >= self.hauteur:
            raise RuntimeError("Sortie de carte :-(")

        if self.carte[newy][newx] == WATER:
            raise RuntimeError("Curiosity a l'eau :-(")

        elif self.carte[newy][newx] == ROCK:
            print ("Ouch!!!")
        else:
            self.x = newx
            self.y = newy
            if not self.ascii_mode:
                self.turtle.forward(DSTEP)

        if WAIT_EACH_STEP: self.attendre()
        self._cible()

    def mesure(self, direct):
        (dx, dy) = self.__direction__(direct)
        val = self.carte[self.y+dy][self.x+dx]
        # print ("Mesure: ", val, " a ", self.y, "+", dy, "x", self.x, "+", dx, "  direction: ", direct)

        if WAIT_EACH_STEP: self.attendre()
        return val

    def pose(self, pose):
        # print ("Pose ", pose, " a ", self.y, "x", self.x)
        if pose:
            self.carte[self.y][self.x] = MARK

            if not self.ascii_mode:
                self.turtle.shape(SHMARK)
                self.marques[self.y][self.x] = self.turtle.stamp()

            self._selectRoverShape()
        else:
            self.carte[self.y][self.x] = PLAIN

            if not self.ascii_mode:
                self.turtle.clearstamp(self.marques[self.y][self.x])
        if WAIT_EACH_STEP: self.attendre()

    def fin(self):
        self.attendre()

    def debug(self):
        print ("Curiosity: ", end="")
        print (self.x, end="")
        print ('x', end="")
        print (self.y, end="")
        print (" looking ", end="")
        print (self.orient)
