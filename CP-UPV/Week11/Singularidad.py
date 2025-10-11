import sys
 
MINC = -10**9
MAXC = 10**9
 
def ask(x, y):
    """Envía una consulta y devuelve la respuesta del juez."""
    print(f"? {x} {y}", flush=True)
    return sys.stdin.readline().strip()
 
def binary_search_for_IND_horizontal(y_fixed, direction):
    """
    Busca un punto donde la brújula devuelve IND en la recta horizontal y = y_fixed.
    - direction = -1 busca hacia el oeste (disminuyendo x)
    - direction = +1 busca hacia el este  (aumentando x)
    """
    lo, hi = MINC, MAXC
    ind_pos = None
    while lo <= hi:
        mid = (lo + hi) // 2
        res = ask(mid, y_fixed)
        if res == "IND":
            ind_pos = mid
            # seguimos buscando en la misma dirección para hallar el extremo más alejado
            if direction == -1:
                hi = mid - 1
            else:
                lo = mid + 1
        elif direction == -1:
            # Si buscamos hacia el oeste
            if res == "E":
                lo = mid + 1
            else:
                hi = mid - 1
        else:
            # Si buscamos hacia el este
            if res == "O":
                hi = mid - 1
            else:
                lo = mid + 1
    return ind_pos
 
def binary_search_for_IND_vertical(x_fixed, direction):
    """
    Busca un punto donde la brújula devuelve IND en la recta vertical x = x_fixed.
    - direction = -1 busca hacia el sur (disminuyendo y)
    - direction = +1 busca hacia el norte (aumentando y)
    """
    lo, hi = MINC, MAXC
    ind_pos = None
    while lo <= hi:
        mid = (lo + hi) // 2
        res = ask(x_fixed, mid)
        if res == "IND":
            ind_pos = mid
            if direction == -1:
                hi = mid - 1
            else:
                lo = mid + 1
        elif direction == -1:
            if res == "N":
                lo = mid + 1
            else:
                hi = mid - 1
        else:
            if res == "S":
                hi = mid - 1
            else:
                lo = mid + 1
    return ind_pos
 
def solve_case(x0, y0):
    # Primera consulta: brújula en Arenópolis
    res0 = ask(x0, y0)
 
    if res0 in ("N", "S", "IND"):
        # Buscamos sobre una recta horizontal (mismo Y)
        y_line = y0
 
        # Encontramos los dos puntos IND: a la izquierda y a la derecha
        x_left = binary_search_for_IND_horizontal(y_line, -1)
        x_right = binary_search_for_IND_horizontal(y_line, +1)
 
        if x_left is None or x_right is None:
            # Si no encontramos ambos IND, no podemos continuar
            print(f"! {x0} {y0}", flush=True)
            return
 
        # El centro X está en el punto medio
        X = (x_left + x_right) // 2
        dist = (x_right - x_left) // 2
 
        # Ahora averiguamos la coordenada Y:
        # hacemos una consulta segura en el centro de la recta
        res_mid = ask(X, y_line)

        if res_mid == "N":

            Y = y_line + dist
        elif res_mid == "S":
            Y = y_line - dist
        else:
            # Si ya es IND, ya estamos alineados
            Y = y_line
 
    else:
        # res0 es E u O: buscamos sobre una recta vertical (mismo X)
        x_line = x0
 
        # Encontramos los dos puntos IND: arriba y abajo
        y_down = binary_search_for_IND_vertical(x_line, -1)
        y_up = binary_search_for_IND_vertical(x_line, +1)
 
        if y_down is None or y_up is None:
            print(f"! {x0} {y0}", flush=True)
            return
 
        # El centro Y está en el punto medio
        Y = (y_down + y_up) // 2
        dist = (y_up - y_down) // 2
 
        # Averiguamos X consultando en (x_line, Y)
        res_mid = ask(x_line, Y)
        if res_mid == "E":

            X = x_line + dist
        elif res_mid == "O":
            X = x_line - dist
        else:
            X = x_line
 
    # Reportamos el resultado final
    print(f"! {X} {Y}", flush=True)
 
def main():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        x0, y0 = map(int, line.split())
        solve_case(x0, y0)
 
if __name__ == "__main__":
    main()
