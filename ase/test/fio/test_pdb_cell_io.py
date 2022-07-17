import pytest
import numpy as np
from ase import Atoms
from ase.build import fcc111
from ase.io import read, write

# Check that saving/loading pdb files correctly reproduces the atoms object.
#
# Loading will restore the cell from lengths/angles, so the best we can do
# is to recreate the scaled positions, not the absolute positions.

images = [
    Atoms(symbols='C8O8Ru64',
          pbc=np.array([True, True, True], dtype=bool),
          cell=np.array([[9.46101634e+00, 5.46231901e+00, -7.62683750e-07],
                         [0.00000000e+00, 1.09246400e+01, -7.62683750e-07],
                         [0.00000000e+00, 0.00000000e+00, 2.14654300e+01]]),
          positions=np.array(
              [[7.80131882e-01, 6.83747136e+00, 8.38204657e+00],
               [5.51092271e+00, 9.56854231e+00, 8.38223568e+00],
               [3.07270715e+00, 2.87955302e+00, 8.37140640e+00],
               [7.80350536e+00, 5.61092571e+00, 8.37131213e+00],
               [4.27438360e+00, 6.25264571e+00, 7.97264597e+00],
               [9.00498640e+00, 8.98355980e+00, 7.97286435e+00],
               [6.37288973e+00, 1.35474697e+01, 7.83982205e+00],
               [1.64255024e+00, 1.08160090e+01, 7.83994023e+00],
               [7.71235875e-01, 6.84831577e+00, 9.54503003e+00],
               [5.50223518e+00, 9.57934418e+00, 9.54476437e+00],
               [3.03497100e+00, 2.94960249e+00, 9.52997683e+00],
               [7.76620880e+00, 5.68120179e+00, 9.52999700e+00],
               [4.23008702e+00, 6.32508468e+00, 9.15933250e+00],
               [8.96060688e+00, 9.05590199e+00, 9.15923442e+00],
               [6.34874076e+00, 1.35969943e+01, 9.03839912e+00],
               [1.61820848e+00, 1.08649253e+01, 9.01849841e+00],
               [1.57683637e+00, 2.73116147e+00, -2.54228044e-07],
               [1.56720630e+00, 2.72722886e+00, 4.28570884e+00],
               [7.88417713e-01, 1.36558046e+00, 2.15514407e+00],
               [8.02210750e-01, 1.34385101e+00, 6.43536380e+00],
               [3.94209046e+00, 4.09674123e+00, -4.44898981e-07],
               [3.95116212e+00, 4.10376637e+00, 4.28640956e+00],
               [3.15367180e+00, 2.73116022e+00, 2.15514388e+00],
               [3.15302826e+00, 2.73391087e+00, 6.47587998e+00],
               [6.30734454e+00, 5.46232098e+00, -6.35569919e-07],
               [6.29772257e+00, 5.45840160e+00, 4.28564811e+00],
               [5.51892683e+00, 4.09674051e+00, 2.15514369e+00],
               [5.53267073e+00, 4.07509705e+00, 6.43527963e+00],
               [8.67259863e+00, 6.82790073e+00, -8.26240856e-07],
               [8.68166544e+00, 6.83494012e+00, 4.28642358e+00],
               [7.88417997e+00, 5.46231972e+00, 2.15514350e+00],
               [7.88362942e+00, 5.46507502e+00, 6.47590212e+00],
               [1.57683637e+00, 5.46232147e+00, -4.44898981e-07],
               [1.58727500e+00, 5.44486645e+00, 4.24854361e+00],
               [7.88417713e-01, 4.09674046e+00, 2.15514388e+00],
               [8.01608482e-01, 4.07705367e+00, 6.44578990e+00],
               [3.94209046e+00, 6.82790123e+00, -6.35569919e-07],
               [3.95243122e+00, 6.81073405e+00, 4.32065689e+00],
               [3.15367180e+00, 5.46232022e+00, 2.15514369e+00],
               [3.16456215e+00, 5.44150374e+00, 6.44566316e+00],
               [6.30734454e+00, 8.19348098e+00, -8.26240856e-07],
               [6.31780039e+00, 8.17600912e+00, 4.24852811e+00],
               [5.51892588e+00, 6.82789997e+00, 2.15514350e+00],
               [5.53216899e+00, 6.80824683e+00, 6.44574538e+00],
               [8.67259863e+00, 9.55906073e+00, -1.01691179e-06],
               [8.68296348e+00, 9.54187626e+00, 4.32068356e+00],
               [7.88417997e+00, 8.19347972e+00, 2.15514331e+00],
               [7.89512792e+00, 8.17267187e+00, 6.44565547e+00],
               [1.57683637e+00, 8.19348147e+00, -6.35569919e-07],
               [1.58115689e+00, 8.20071292e+00, 4.29055653e+00],
               [7.88417713e-01, 6.82790046e+00, 2.15514369e+00],
               [7.91948666e-01, 6.82222698e+00, 6.48549188e+00],
               [3.94209046e+00, 9.55906123e+00, -8.26240856e-07],
               [3.93358820e+00, 9.55894698e+00, 4.29187459e+00],
               [3.15367180e+00, 8.19348022e+00, 2.15514350e+00],
               [3.15825664e+00, 8.18574447e+00, 6.38108109e+00],
               [6.30734454e+00, 1.09246410e+01, -1.01691179e-06],
               [6.31166355e+00, 1.09318806e+01, 4.29057142e+00],
               [5.51892588e+00, 9.55905997e+00, 2.15514331e+00],
               [5.52249944e+00, 9.55339051e+00, 6.48545486e+00],
               [8.67259863e+00, 1.22902207e+01, -1.20758273e-06],
               [8.66410508e+00, 1.22901152e+01, 4.29183559e+00],
               [7.88418091e+00, 1.09246403e+01, 2.15514312e+00],
               [7.88880125e+00, 1.09169018e+01, 6.38105940e+00],
               [1.57683637e+00, 1.09246415e+01, -8.26240856e-07],
               [1.58687157e+00, 1.09077863e+01, 4.32193338e+00],
               [7.88417713e-01, 9.55906046e+00, 2.15514350e+00],
               [7.78394031e-01, 9.52397919e+00, 6.44162756e+00],
               [3.94209046e+00, 1.22902212e+01, -1.01691179e-06],
               [3.95166143e+00, 1.22749617e+01, 4.26568019e+00],
               [3.15367180e+00, 1.09246402e+01, 2.15514331e+00],
               [3.19235336e+00, 1.09175437e+01, 6.44091634e+00],
               [6.30734454e+00, 1.36558010e+01, -1.20758273e-06],
               [6.31737307e+00, 1.36389093e+01, 4.32189961e+00],
               [5.51892588e+00, 1.22902200e+01, 2.15514312e+00],
               [5.50895045e+00, 1.22551312e+01, 6.44172685e+00],
               [8.67259863e+00, 1.50213807e+01, -1.39825367e-06],
               [8.68213569e+00, 1.50061426e+01, 4.26566744e+00],
               [7.88418091e+00, 1.36558003e+01, 2.15514293e+00],
               [7.92283529e+00, 1.36487476e+01, 6.44087611e+00]])),
]


@pytest.mark.parametrize('nrepeat', [1, 2])
def test_pdb_cell_io(nrepeat):
    traj1 = images * nrepeat
    write('grumbles.pdb', traj1)
    traj2 = read('grumbles.pdb', index=':')

    assert len(traj1) == len(traj2)
    for atoms1, atoms2 in zip(traj1, traj2):
        spos1 = (atoms1.get_scaled_positions() + 0.5) % 1.0
        spos2 = (atoms2.get_scaled_positions() + 0.5) % 1.0
        cell1 = atoms1.cell.cellpar()
        cell2 = atoms2.cell.cellpar()

        np.testing.assert_allclose(
            atoms1.get_atomic_numbers(), atoms2.get_atomic_numbers())
        np.testing.assert_allclose(spos1, spos2, rtol=0, atol=2e-4)
        np.testing.assert_allclose(cell1, cell2, rtol=0, atol=1e-3)


def test_pdb_nonbulk_read():
    atoms1 = fcc111('Au', size=(3, 3, 1))
    atoms1.symbols[4:10] = 'Ag'
    atoms1.write('test.pdb')
    atoms2 = read('test.pdb')

    spos1 = (atoms1.get_scaled_positions() + 0.5) % 1.0
    spos2 = (atoms2.get_scaled_positions() + 0.5) % 1.0

    np.testing.assert_allclose(
        atoms1.get_atomic_numbers(), atoms2.get_atomic_numbers())
    np.testing.assert_allclose(spos1, spos2, rtol=0, atol=2e-4)


def test_pdb_no_periodic():
    atoms1 = Atoms('H')
    atoms1.center(vacuum=1)
    atoms1.write('h.pdb')

    atoms2 = read('h.pdb')

    spos1 = atoms1.get_positions()
    spos2 = atoms2.get_positions()

    np.testing.assert_allclose(
        atoms1.get_atomic_numbers(), atoms2.get_atomic_numbers())
    np.testing.assert_allclose(spos1, spos2, rtol=0, atol=2e-4)
