def raizes(a, b, c):
    D = (b**2 - 4*a*c)
    x1 = round((-b + D**(1/2)) / (2*a),2)
    x2 = round((-b - D**(1/2)) / (2*a),2)
    return x1, x2

def equation(ax, b, solve):
    result = solve - b / ax
    return result


class Matriz:
    def __init__(self, Array: list, solve: list = []) -> None:
        """"param Array: square list of lines x rows
        example: [[i,j], [i, j]] or [[i,j,k],[i,j,k],[i,j,k]]
        minimum 2x2
        for minus use function equation
        Class to matrix manipulation"""
        self.matriz = Array
        self.lenght = len(self.matriz)
        self.solve = solve


    def Multiplicar(self, Array: list, x: float, linha: int = 0) -> None:
            """Multiply the matrix by float x
            param Array: matrix
            param x: multiplier
            optional param linha: line to multiply, if non-specified multiply all lines
            """
            for i in range(len(Array)):
                for j in range(len(Array[i])):
                    if linha != 0 and linha != i+1:
                        pass
                    else:
                        Array[i][j] = Array[i][j]*x
            return Array
    
    def somaGJ(self, Array: list, LPrincipal: int, Lsoma: int, coeficiente: float = 1) -> None:
        """Do plus operations line to line multiplied by a coefficient
        param Array: matrix
        param LPrincipal: line to change values
        param Lsoma: line to operate with values
        param coeficiente: x
        Lprincipal += x*Lsoma
        return the matrix operated"""
        LinhaP = Array[LPrincipal]
        LinhaS = Array[Lsoma]
        result = []
        for num in range(len(LinhaP)):
            result.append(LinhaP[num] + (coeficiente * LinhaS[num]))
        return result
    


    def autoValor(self):
        """calculate autovalor
        return lambdas"""
        matriz = self.matriz
        a = 1
        b1 = -1 * matriz[1][1]
        b2 = -1 * matriz[0][0]
        b = b1 + b2
        c = matriz[0][0] * matriz[1][1]
        c -= (matriz[0][1] * matriz[1][0])
        return raizes(a,b,c)
        
    



                
    
    
    def AutoVetor(self) -> None:
        """calculate autovetor"""
        lambdas = self.autoValor()
        eachLambda = []
        a = []
        matriz = self.matriz[:]
        for lmbds in range(len(lambdas)):
            eachLambda.append([])
            for eq in range(len(matriz)):
                a = matriz[eq].copy()
                a[eq] -=  lambdas[lmbds]
                eachLambda[lmbds].append(a)
        lb = 0
        str = ''
        for l in eachLambda:
            x = l[0][0]
            y1 = -1 * l[0][1]
            if y1 == 0 or y1 % x == 0:
                d = None
            else:
                d = 1
            if y1 != 0:
                y = round((y1 / x), d)
                str += f"Com lambda = {lambdas[lb]}:\n  x = {y}y \n(1, {y})\n\n"
            else:
                y = y1
                str += f"Com lambda = {lambdas[lb]}:\n  x = {y}y, \n({x},{y})\n\n"
            lb += 1
        return str
    
    def gaussJordan(self) -> list:
        """Gauss Jordan to solve linear systems 2x2 or plus
        param matriz: matrix
        param solve: solutions of every line of matrix"""
        matriz = self.matriz[:]
        if self.solve == []:
            for i in range(len(matriz)):
                self.solve.append(0)
        for i in range(len(self.solve)):
            matriz[i].append(self.solve[i])
        for eq in range(len(matriz)):
            pivo = matriz[eq][eq]
            nxt = eq + 1
            if pivo != 1:
                if pivo == 0:
                    if eq + 1 == len(matriz):
                        return []
                    else:
                        for k in range(len(matriz)):
                            if k == eq:
                                pass
                            else:
                                if matriz[k][eq] != 0:
                                    matriz[eq] = self.somaGJ(matriz, eq, k, (1 / matriz[k][eq]))
                                break
                else:
                    matriz = self.Multiplicar(matriz, 1 / pivo, nxt)
            for i in range(eq+1, len(matriz)):
                if matriz[i][eq] != 0:
                    matriz[i] = self.somaGJ(matriz, i, eq, -1* matriz[i][eq])
        for eq in range(len(matriz) - 1, 0, -1):
            for i in range(eq - 1, -1, - 1):
                if matriz[i][eq] != 0:
                    matriz[i] = self.somaGJ(matriz, i, eq, -1* matriz[i][eq])
        for i in matriz:
            i[-1] = round(i[-1], 2)
        return matriz

                