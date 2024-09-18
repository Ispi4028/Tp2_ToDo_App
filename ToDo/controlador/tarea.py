class Tarea:
    def __init__(self, descripcion):
        self.__descripcion = descripcion
        self.__completada = False

    def obtener_descripcion(self):
        return self.__descripcion

    def marcar_como_completada(self):
        self.__completada = True

    def desmarcar_como_completada(self):
        self.__completada = False
