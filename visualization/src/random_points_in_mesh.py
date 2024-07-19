import numpy as np
import gpytoolbox as gpy

def box(V):
    m_x, m_y, m_z = V[0]
    M_x, M_y, M_z = V[0]

    for [x, y, z] in V:
        m_x = min(m_x, x)
        m_y = min(m_y, y)
        m_z = min(m_z, z)
        M_x = max(M_x, x)
        M_y = max(M_y, y)
        M_z = max(M_z, z)

    return m_x, m_y, m_z, M_x, M_y, M_z

def random_points(V, F, num_points = 1000, eps = 1e-3):

    P = []

    m_x, m_y, m_z, M_x, M_y, M_z = box(V)

    print('Generating Points...')

    while len(P) < num_points:
        p = [np.random.rand() * (M_x - m_x) + m_x, np.random.rand() * (M_y - m_y) + m_y, np.random.rand() * (M_z - m_z) + m_z]

        # print(f'{p} => {gpy.fast_winding_number(np.array([p]), V, F)}')

        dist, _, _ = gpy.signed_distance(np.array([p]), V, F)
        # print(f'{p} => {dist}')

        if dist[0] < -eps:
            P.append(p)
            print(f'OK {len(P)}/{num_points}')

    return np.array(P)