import numpy as np


def input_properties_case_7_psudocomponents():
    '''
    7 pseudo-components

    '''

    temperature = 366.5
    pressure = 150.0 * 1.0e5

    critical_pressure = 101325.0 * np.array([45.45, 51.29, 39.89, 31.95, 27.91, 17.71, 12.52])  # [atm]
    critical_temperature = np.array([189.2, 305.4, 395.8, 485.1, 592.0, 697.1, 804.4])  # [K]
    acentric_factor = np.array([0.00891, 0.11352, 0.17113, 0.26910, 0.34196, 0.51730, 0.72755])  # [-]
    molar_mass = 0.001 * np.array([16.38, 31.77, 50.64, 77.78, 118.44, 193.95, 295.30])  # [g/mol]
    omega_a = np.array([0.344772, 0.521974, 0.514972, 0.419169, 0.485943, 0.570583, 0.457236])  # [-]
    omega_b = np.array([0.063282, 0.099825, 0.107479, 0.093455, 0.07486, 0.101206, 0.077796])  # [-]

    binary_interaction = np.array(
        [[0.000000, 0.000622, -0.002471, 0.011418, -0.028367, -0.100000, 0.206868],
         [0.000622, 0.000000, -0.001540, 0.010046, 0.010046, 0.010046, 0.010046],
         [-0.002471, -0.001540, 0.000000, 0.002246, 0.002246, 0.002246, 0.002246],
         [0.011418, 0.010046, 0.002246, 0.000000, 0.000000, 0.000000, 0.000000],
         [-0.028367, 0.010046, 0.002246, 0.000000, 0.000000, 0.000000, 0.000000],
         [-0.100000, 0.010046, 0.002246, 0.000000, 0.000000, 0.000000, 0.000000],
         [0.206868, 0.010046, 0.002246, 0.000000, 0.000000, 0.000000, 0.000000]]
    )

    global_molar_fractions = np.array([0.6793, 0.099, 0.1108, 0.045, 0.05011, 0.0134, 0.00239])

    return (pressure, temperature, global_molar_fractions,
            critical_pressure, critical_temperature, acentric_factor,
            molar_mass, omega_a, omega_b, binary_interaction)


def input_properties_case_whitson_problem_18_PR():
    '''
    TEST PROBLEM PHASE BEHAVIOUR WHITSON PROBLEM 18 APPENDIX

    Methane, Butane and Decane (C1, C4 and C10).

    Properties for the Van der Waals Equation of State.

    '''
    temperature = (280.0 + 459.67) * 5.0 / 9.0
    pressure = 500.0 * 6894.75729

    critical_pressure = 6894.75729 * np.array([667.8, 550.7, 304.0])  # [atm]
    critical_temperature = (5.0 / 9.0) * np.array([343.0, 765.3, 1111.8])  # [K]
    acentric_factor = np.array([0.011500, 0.192800, 0.490200])  # [-]
    molar_mass = 0.001 * np.array([16.04, 58.12, 142.29])  # [g/mol]
    omega_a = 0.45724 * np.array([1.0, 1.0, 1.0])  # [-]
    omega_b = 0.07780 * np.array([1.0, 1.0, 1.0])  # [-]

    binary_interaction = np.array(
        [[0.000000, 0.000000, 0.000000],
         [0.000000, 0.000000, 0.000000],
         [0.000000, 0.000000, 0.000000]]
    )

    global_molar_fractions = np.array([0.5, 0.42, 0.08])

    return (pressure, temperature, global_molar_fractions,
            critical_pressure, critical_temperature, acentric_factor,
            molar_mass, omega_a, omega_b, binary_interaction)


def input_properties_case_whitson_problem_18_VDW():
    '''
    TEST PROBLEM PHASE BEHAVIOUR WHITSON PROBLEM 18 APPENDIX

    Methane, Butane and Decane (C1, C4 and C10).

    Properties for the Van der Waals Equation of State.

    '''
    temperature = (280.0 + 459.67) * 5.0 / 9.0
    pressure = 500.0 * 6894.75729

    critical_pressure = 6894.75729 * np.array([667.8, 550.7, 304.0])  # [atm]
    critical_temperature = (5.0 / 9.0) * np.array([343.0, 765.3, 1111.8])  # [K]
    acentric_factor = np.array([0.011500, 0.192800, 0.490200])  # [-]
    molar_mass = 0.001 * np.array([16.04, 58.12, 142.29])  # [g/mol]
    omega_a = (27.0 / 64.0) * np.array([1.0, 1.0, 1.0])  # [-]
    omega_b = (1.0 / 8.0) * np.array([1.0, 1.0, 1.0])  # [-]

    binary_interaction = np.array(
        [[0.000000, 0.000000, 0.000000],
         [0.000000, 0.000000, 0.000000],
         [0.000000, 0.000000, 0.000000]]
    )

    global_molar_fractions = np.array([0.5, 0.42, 0.08])

    return (pressure, temperature, global_molar_fractions,
            critical_pressure, critical_temperature, acentric_factor,
            molar_mass, omega_a, omega_b, binary_interaction)


def input_properties_case_whitson_problem_18_SRK():
    '''
    TEST PROBLEM PHASE BEHAVIOUR WHITSON PROBLEM 18 APPENDIX

    Methane, Butane and Decane (C1, C4 and C10).

    Properties for the Soave-Redlich-Kwong Equation of State.

    '''
    temperature = (280.0 + 459.67) * 5.0 / 9.0
    pressure = 500.0 * 6894.75729

    critical_pressure = 6894.75729 * np.array([667.8, 550.7, 304.0])  # [atm]
    critical_temperature = (5.0 / 9.0) * np.array([343.0, 765.3, 1111.8])  # [K]
    acentric_factor = np.array([0.011500, 0.192800, 0.490200])  # [-]
    molar_mass = 0.001 * np.array([16.04, 58.12, 142.29])  # [g/mol]
    omega_a = 0.42748 * np.array([1.0, 1.0, 1.0])  # [-]
    omega_b = 0.08664 * np.array([1.0, 1.0, 1.0])  # [-]

    binary_interaction = np.array(
        [[0.000000, 0.000000, 0.000000],
         [0.000000, 0.000000, 0.000000],
         [0.000000, 0.000000, 0.000000]]
    )

    global_molar_fractions = np.array([0.5, 0.42, 0.08])

    return (pressure, temperature, global_molar_fractions,
            critical_pressure, critical_temperature, acentric_factor,
            molar_mass, omega_a, omega_b, binary_interaction)


def input_properties_case_dissertation_PR():
    '''
    TEST PROBLEM PHASE BEHAVIOUR DISSERTATION

    Methane, Ethane, Butane and Heptane (pseudo) (C1, C2, C4 and C7).

    Properties for the Peng-Robinson Equation of State.

    '''
    temperature = np.nan
    pressure = np.nan

    critical_pressure = 101325.0 * np.array([45.40, 48.20, 37.50, 30.97])  # [atm]
    critical_temperature = np.array([190.6, 305.4, 425.2, 543.2])  # [K]
    acentric_factor = np.array([0.008, 0.098, 0.193, 0.308])  # [-]
    molar_mass = 0.001 * np.array([16.04, 30.07, 58.12, 96.00])  # [g/mol]
    omega_a = 0.45724 * np.array([1.0, 1.0, 1.0, 1.0])  # [-]
    omega_b = 0.07780 * np.array([1.0, 1.0, 1.0, 1.0])  # [-]

    binary_interaction = np.array(
        [[0.000000, 0.000000, 0.000000, 0.000000],
         [0.000000, 0.000000, 0.000000, 0.000000],
         [0.000000, 0.000000, 0.000000, 0.000000],
         [0.000000, 0.000000, 0.000000, 0.000000]]
    )

    global_molar_fractions = np.array([0.1, 0.4, 0.4, 0.1])

    return (pressure, temperature, global_molar_fractions,
            critical_pressure, critical_temperature, acentric_factor,
            molar_mass, omega_a, omega_b, binary_interaction)
