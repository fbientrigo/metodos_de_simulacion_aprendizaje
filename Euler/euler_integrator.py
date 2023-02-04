


def unzip(zipped_information):
    ''' usado para separar en dos objetos el output de eulers'''
    unzip = list(zip(*zipped_information))
    return unzip[0], unzip[1]


def euler1step(fun, dt, t0, y0):
    """
    mucho mas flexible, unicamente da un salto
    """
    return y0 + fun(t0, y0) * dt


def euler_forward(dt, T, xdot, x0, t0, args_for_xdot = {}, xdot_time = False):
    """
    Realiza el proceso x_k+1 = x_k + delta t * f(x_k)
    si se urtiliza xdot_time = True entonces f(x_k, t, argumentos extras)

    Notar que la funcion xdot, debe ser xdot(x_k, otrosParametros)
    dt: time step (recomendado 0.01)
    T: periodo, (hasta que tiempo corre el codigo)
    xdot: la funcion a evaluar
    args_for_xdot: argumentos dentro de un diccionario {'a':1, 'b':3}
    xdot_time: activa la dependencia temporal de la funcion

    """
    t = t0
    xk = x0

    if not(xdot_time): 
        while t<T:
            xk1 = xk + dt * xdot(xk, **args_for_xdot) # desempaqueta el diccionario
            t += dt
            xk = xk1
            yield t,xk1    
    else:        # ------------- caso que sea time deppendent
        while t<T:
            xk1 = xk + dt * xdot(xk, t, **args_for_xdot) 
            t += dt
            xk = xk1
            yield t,xk1     # generadores y los datos nos quedan en tuplas (t_k, x_k)


def euler_forward_less(dt, T, xdot, x0, t0, xdot_time = False):
    """
    Realiza el proceso x_k+1 = x_k + delta t * f(x_k)
    si se urtiliza xdot_time = True entonces f(x_k, t, argumentos extras)

    Notar que la funcion xdot, debe ser xdot(x_k, otrosParametros)
    dt: time step (recomendado 0.01)
    T: periodo, (hasta que tiempo corre el codigo)
    xdot: la funcion a evaluar
    args_for_xdot: argumentos dentro de un diccionario {'a':1, 'b':3}
    xdot_time: activa la dependencia temporal de la funcion

    """
    t = t0
    xk = x0

    if not(xdot_time): 
        while t<T:
            xk1 = xk + dt * xdot(xk) # desempaqueta el diccionario
            t += dt
            xk = xk1
            yield t,xk1    
    else:        # ------------- caso que sea time deppendent
        while t<T:
            xk1 = xk + dt * xdot(xk, t) 
            t += dt
            xk = xk1
            yield t,xk1     # generadores y los datos nos quedan en tuplas (t_k, x_k)