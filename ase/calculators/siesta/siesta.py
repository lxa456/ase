from __future__ import print_function
"""This module defines an ASE interface to SIESTA.

http://www.uam.es/departamentos/ciencias/fismateriac/siesta
"""
from ase.calculators.siesta.base_siesta import BaseSiesta


# Version 3.2 of Siesta
class Siesta3_2(BaseSiesta):
    allowed_xc = {
        'LDA': ['PZ', 'CA', 'PW92'],
        'GGA': ['PBE', 'revPBE', 'RPBE',
                'WC', 'PBEsol', 'LYP'],
    }
    allowed_fdf_keywords = [
        'LongOutput',
        'SystemName',
        'SystemLabel',
        'NumberOfSpecies',
        'NumberOfAtoms',
        'ChemicalSpeciesLabel',
        'AtomicMass',
        'PAO_BasisType',
        'PAO_SplitNorm',
        'PAO_SplitNormH',
        'PAO_NewSplitCode',
        'PAO_FixSplitTable',
        'PAO_FixSplitTailNorm',
        'PAO_SoftDefault',
        'PAO_SoftInnerRadius',
        'PAO_SoftPotential',
        'PS.lmax',
        'PS.KBprojectors',
        'FilterCutoff',
        'FilterTol',
        'User_Basis',
        'User_Basis_NetCDF',
        'BasisPressure',
        'ReparametrizePseudos',
        'New_A_Parameter',
        'New_B_Parameter',
        'Rmax_Radial_Grid',
        'Restricted_Radial_Grid',
        'LatticeConstant',
        'LatticeParameters',
        'LatticeVectors',
        'SuperCell',
        'AtomicCoordinatesFormat',
        'AtomicCoorFormatOut',
        'AtomicCoordinatesOrigin',
        'AtomicCoordinatesAndAtomicSpecies',
        'Zmatrix',
        'ZM_UnitsLength',
        'ZM_UnitsAngle',
        'WriteCoorXmol',
        'WriteCoorCerius',
        'WriteMDXmol',
        'WarningMiniumAtomicDistance',
        'MaxBondDistance',
        'kgrid__cutoff',
        'kgrid__Monkhorst__Pack',
        'ChangeKgridInMD',
        'TimeReversalSymmetryForKpoints',
        'WriteKpoints',
        'XC_functional',
        'XC_authors',
        'XC_hydrid',
        'SpinPolarised',
        'NonCollinearSpin',
        'FixSpin',
        'TotalSpin',
        'SingleExcitation',
        'Harris__functional',
        'MaxSCFIterations',
        'SCFMustConverge',
        'DM_MixingWeight',
        'DM_NumberPulay',
        'DM_Pulay_Avoid_First_After_Kick',
        'DM_NumberBroyden',
        'DM_Broyden_Cycle_On_Maxit',
        'DM_NumberKick',
        'DM_KickMixingWeight',
        'DM_MixSCF1',
        'DM_UseSaveDM',
        'DM_FormattedFiles',
        'DM_FormattedInput',
        'DM_FormattedOutput',
        'DM_InitSpinAF',
        'DM_InitSpin',
        'DM_AllowReuse',
        'DM_AllowExtrapolation',
        'SCF_Read_Charge_NetCDF',
        'SCF_ReadDeformation_Charge_NetCDF',
        'WriteDM',
        'WriteDM_NetCDF',
        'WrireDMHS_NetCDF',
        'WriteDM_History_NetCDF',
        'WrireDMHS_History_NetCDF',
        'DM_Tolerance',
        'DM_Require_Energy_Convergence',
        'DM_Energy_Tolerance',
        'DM_Require_Harris_Convergence',
        'DM_Harris_Tolerance',
        'MeshCutoff',
        'MeshSubDivisions'
        'GridCellSampling',
        'EggboxRemove',
        'EggboxScale',
        'NeglNonOverlapInt',
        'SaveHS',
        'FixAuxiliaryCell',
        'NaiveAuxiliaryCell',
        'SolutionMethod',
        'NumberOfEigenStates',
        'Use_New_Diagk',
        'Diag_DivideAndConquer',
        'Diag_AllInOne',
        'Diag_NoExpert',
        'Diag_PreRotate',
        'Diag_Use2D',
        'WriteEigenvalues',
        'OccupationFunction',
        'OccupationMPOrder',
        'ElectronicTemperature',
        'ON_functional',
        'ON_MaxNumIter',
        'ON_etol',
        'ON_eta',
        'ON_eta_alpha',
        'ON_eta_beta',
        'ON_RcLWF',
        'ON_ChemicalPotential',
        'ON_ChemicalPotentialUse',
        'ON_ChemicalPotentialRc',
        'ON_ChemicalPotentialTemperature',
        'ON_ChemicalPotentialOrder',
        'ON_LowerMemory',
        'ON_UseSaveLWF',
        'BandLinesScale',
        'BandLines',
        'BandPoints',
        'WriteKbands',
        'WriteBands',
        'WFS_Write_For_Bands',
        'WFS_Band_Min',
        'WFS_Band_Max',
        'WaveFuncPointScale',
        'WaveFuncKPoints',
        'WriteWaveFunctions',
        'ProjectedDensityOfStates',
        'LocalDensityOfStates',
        'WriteMullikenPop',
        'MullikenInSCF',
        'WriteHirshfeldPop',
        'WriteVoronoiPop',
        'PartialChargesAtEveryGeometry',
        'PartialChargesAtEveryScfStep',
        'COOP_Write',
        'WFS_Energy_Min',
        'WFS_Energy_Max',
        'OpticalCalculation',
        'Optical_Energy_Minimum',
        'Optical_Energy_Maximum',
        'Optical_Broaden',
        'Optical_Scissor',
        'Optical_NumberOfBands',
        'Optical_Mesh',
        'Optical_OffsetMesh',
        'Optical_PolarizationType',
        'Optical_Vector',
        'PolarizationGrids',
        'BornCharge',
        'NetCharge',
        'SimulateDoping',
        'ExternalElectricField',
        'SlabDipoleCorrection',
        'SaveRho',
        'SaveDeltaRho',
        'SaveElectrostaticPotential',
        'SaveNeutralAtomPotential',
        'SaveBaderCharge',
        'SaveInitialChargeDensity',
        'MM_Potentials',
        'MM_Cutoff',
        'MM_UnitsEnergy',
        'MM_UnitsDistance',
        'MM_Grimme_D',
        'MM_Grimme_S6',
        'BlockSize'
        'ProcessorY',
        'Diag_Memory',
        'Diag_ParallelOverK',
        'UseDomainDecomposition',
        'UseSpatialDecomposition',
        'RcSpatial',
        'DirectPhi',
        'AllocReportLevel',
        'UseSaveData',
        'WriteDenchar',
        'MD_TypeOfRun',
        'MD_VariableCell',
        'MD_ConstantVolume',
        'MD_RelaxCellOnly',
        'MD_MaxForceTol',
        'MD_MaxStressTol',
        'MD_NumCGsteps',
        'MD_MaxCGDispl',
        'MD_PreconditioningVariableCell',
        'ZM_ForceTolLength',
        'ZM_ForceTolAngle',
        'ZM_MaxDiplLength',
        'ZM_MaxDiplAngle',
        'MD_UseSaveCG',
        'MD_Broyden_History_Steps',
        'MD_Broyden_Cycle_On_Maxit',
        'MD_Broyden_Initial_Inverse_Jacobian',
        'MD_FIRE_TimeStep',
        'MD_Quench',
        'MD_FireQuench',
        'MD_TargetPressure',
        'MD_TargetStress',
        'MD_RemoveIntramolecularPressure',
        'MD_InitialTimeStep',
        'MD_FinalTimestep',
        'MD_LengthTimeStep',
        'MD_InitialTemperature',
        'MD_TargetTemperature',
        'MD_NoseMass',
        'MD_ParrinelloRahmanMass',
        'MD_AnnealOption',
        'MD_TauRelax',
        'MD_BulkModulus',
        'WriteCoorInitial',
        'WriteCoorStep',
        'WriteForces',
        'WriteMDhistory',
        'GeometryConstraints',
        'MD_FCDispl',
        'MD_FCfirst',
        'MD_FClast',
        'PhononLabels',
        'MD_ATforPhonon',
    ]


# Trunk version, snapshot 462
class SiestaTrunk462(BaseSiesta):
    allowed_xc = {
        'LDA': ['PZ', 'CA', 'PW92'],
        'GGA': ['PW91', 'PBE', 'revPBE', 'RPBE',
                'WC', 'AM05', 'PBEsol', 'PBEJsJrLO',
                'PBEGcGxLO', 'PBEGcGxHEG', 'BLYP',
                ],
        'VDW': ['DRSLL', 'LMKLL', 'KBM', 'C09', 'BH', 'VV'],
    }


Siesta = Siesta3_2
