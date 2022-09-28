from lib.Simulacion import Simulacion

def test_case_1():

    simu = Simulacion(1, 1, 1, False, lambda x: 5, lambda x: 60)
    simu.start()
    pr, profesores = simu.getResultados()
    ppap_list = list(map(lambda x: x.getPPAP(), profesores)).sort()

    assert pr == 0
    assert ppap_list == [100].sort()


def test_case_2():

    simu = Simulacion(1, 1, 4, False, lambda x: 5, lambda x: 60)
    simu.start()
    pr, profesores = simu.getResultados()
    ppap_list = list(map(lambda x: x.getPPAP(), profesores)).sort()

    assert pr == 0
    assert ppap_list == [100].sort()

def test_case_3():

    simu = Simulacion(1, 1, 5, False, lambda x: 5, lambda x: 60)
    simu.start()
    pr, profesores = simu.getResultados()
    ppap_list = list(map(lambda x: x.getPPAP(), profesores)).sort()

    assert pr == 50
    assert ppap_list == [100].sort()

def test_case_4():

    simu = Simulacion(1, 2, 5, False, lambda x: 5, lambda x: 60)
    simu.start()
    pr, profesores = simu.getResultados()
    ppap_list = list(map(lambda x: x.getPPAP(), profesores)).sort()

    assert pr == 0
    assert ppap_list == [100].sort()

def test_case_5():

    simu = Simulacion(2, 1, 6, False, lambda x: 5, lambda x: 60)
    simu.start()
    pr, profesores = simu.getResultados()
    ppap_list = list(map(lambda x: x.getPPAP(), profesores)).sort()

    assert pr == 0
    assert ppap_list == [50, 50].sort()

def test_case_6():

    simu = Simulacion(2, 2, 15, False, lambda x: 5, lambda x: 60)
    simu.start()
    pr, profesores = simu.getResultados()
    ppap_list = list(map(lambda x: x.getPPAP(), profesores)).sort()

    assert pr == 0
    assert ppap_list == [50, 50].sort()

def test_case_7():

    simu = Simulacion(1, 4, 15, False, lambda x: 5, lambda x: 60)
    simu.start()
    pr, profesores = simu.getResultados()
    ppap_list = list(map(lambda x: x.getPPAP(), profesores)).sort()

    assert pr == 0
    assert ppap_list == [100].sort()

def test_case_8():

    simu = Simulacion(4, 1, 15, False, lambda x: 5, lambda x: 60)
    simu.start()
    pr, profesores = simu.getResultados()
    ppap_list = list(map(lambda x: x.getPPAP(), profesores)).sort()

    assert pr == 0
    assert ppap_list == [25, 25, 25, 25].sort()

def test_case_9():

    simu = Simulacion(2, 2, 20, False, lambda x: 5, lambda x: 60)
    simu.start()
    pr, profesores = simu.getResultados()
    ppap_list = list(map(lambda x: x.getPPAP(), profesores)).sort()

    assert pr == 20
    assert ppap_list == [50, 50].sort()

def test_case_10():

    simu = Simulacion(3, 10, 60, False, lambda x: 5, lambda x: 60)
    simu.start()
    pr, profesores = simu.getResultados()
    ppap_list = list(map(lambda x: x.getPPAP(), profesores)).sort()

    assert pr == 0
    assert ppap_list == [0, 23.076923076923077, 76.92307692307693].sort()
