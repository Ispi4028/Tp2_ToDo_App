class Tarea:
    def __init__(self, descripcion):
        self.descripcion = descripcion
        self.completada = False

    def marcar_como_completada(self):
        self.completada = True

    def desmarcar_como_completada(self):
        self.completada = False
