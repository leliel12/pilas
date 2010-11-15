# -*- encoding: utf-8 -*-
# Pilas engine - A video game framework.
#
# Copyright 2010 - Hugo Ruscitti
# License: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)
#
# Website - http://www.pilas-engine.com.ar

from pilas.actores import Actor
import pilas

class Piedra(Actor):
    "Representa un bloque que tiene fisica como una caja."

    def __init__(self, x=0, y=0, tamano="grande"):
        imagen = pilas.imagenes.cargar('piedra_' + tamano + '.png')
        Actor.__init__(self, imagen)
        self.rotacion = 0
        self.x = x
        self.y = y

        radios = {
                'grande': 25,
                'media': 20,
                'chica': 10,
                }

        self.radio_de_colision = radios[tamano]

    def actualizar(self):
        self.rotacion += 1
