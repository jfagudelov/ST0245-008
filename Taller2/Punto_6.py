futbolistasTup = [(1, "Casillas"), (15, "Ramos"), (3, "Pique"), (5, "Puyol"), 
                  (11, "Capdevila"),  (14, "Xabi Alonso"), (16, "Busquets"), 
                  (8, "Xavi Hernandez"), (18, "Pedrito"), (6, "Iniesta"), 
                  (7, "Villa")]

tomar_primero = lambda futbolistas: futbolistas[0]
futbolistasTup.sort(key=tomar_primero)
print(futbolistasTup)

inventos_importantes = [('Starlink', 70), ('Starship', 100), ('GPT-3', 60),
                        ('MyEye2', 50), ('5G', 80)]

tomar_segundo = lambda inventos: inventos[1]
inventos_importantes.sort(key=tomar_segundo)
print('Los inventos más importantes del menos al más son:', inventos_importantes)
