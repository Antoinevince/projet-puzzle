import coordinates


def bfs_edge_only_group():
    config_init = [
    # Liste des coins
    [
        [0, 0],  # Coin 0
        [1, 0],  # Coin 1
        [2, 0],  # Coin 2
        [3, 0],   # Coin 3
        [4, 0],
        [5, 0],
        [6, 0],
        [7, 0],
        [8, 0]
    ],
    # Liste des arêtes
    [
        [0, 0],  # Arête 0
        [1, 0],  # Arête 1
        [2, 0],  # Arête 2
        [3, 0],  # Arête 3
        [4, 0],  # Arête 4
        [5, 0],  # Arête 5
        [6, 0],  # Arête 6
        [7, 0]   # Arête 7
    ]
    ]

    visited = [config_init]
    profondeur = 0
    deja_vu = [config_init]
    

    a_voir = [coordinates.Rubikscubemoves.rotateF(config_init), 
              coordinates.Rubikscubemoves.rotateB(config_init), 
              coordinates.Rubikscubemoves.rotateD(config_init), 
              coordinates.Rubikscubemoves.rotateL(config_init), 
              coordinates.Rubikscubemoves.rotateR(config_init), 
              coordinates.Rubikscubemoves.rotateU(config_init),
              coordinates.Rubikscubemoves.move_E(config_init),
              coordinates.Rubikscubemoves.move_M(config_init),
              coordinates.Rubikscubemoves.move_S(config_init)]
    
    
    
     
    

    while a_voir != []:


        new_config = a_voir.pop()
        
        a_voir_new_configs = [coordinates.Rubikscubemoves.rotateF(new_config), 
                              coordinates.Rubikscubemoves.rotateB(new_config), 
                              coordinates.Rubikscubemoves.rotateD(new_config), 
                              coordinates.Rubikscubemoves.rotateL(new_config), 
                              coordinates.Rubikscubemoves.rotateR(new_config), 
                              coordinates.Rubikscubemoves.rotateU(new_config),
                              coordinates.Rubikscubemoves.move_E(config_init),
                              coordinates.Rubikscubemoves.move_M(config_init),
                              coordinates.Rubikscubemoves.move_S(config_init)]
        
        
        a_voir = a_voir_new_configs+a_voir
        
            


        #on appelle le dfs de nouveau
        bfs_edge_only_group(new_config)

    return 