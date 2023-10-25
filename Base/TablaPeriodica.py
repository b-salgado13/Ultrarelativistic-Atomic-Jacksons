"""
Aquí se definen las masas y cargas de cada núcleo atómico y sus principales isótopos
Estos se definen en términos de la masa del electrón ya que en física
molecular la masa del electrón es la unidad de la masa
La masa del electron es aproximadamente 5.485799*10^(-4) uma
"""
Atomo = {
    "H" : {
        1 : {
            "masa" : 1837.152618
            #Estable, abundancia 99.97%
        },
        2 : {
            "masa" : 3671.481583
            #Estable, abundancia 0.001
        },
        3 : {
            "masa" : 5497.921086
            #Inestable, Trazas
        },
        "carga" : 1
    },
    "He" : {
        2 : {
            "masa" : 3674.750022
        },
        3 : {
            "masa" : 5497.884629
            #Estable, abundancia 0.0002%
        },
        4 : {
            "masa" : 7296.299044
            #Estable, abundancia 99.9998%
        },
        5 : {
            "masa" : 9136.421148
        },
        "carga" : 2
    },
    "Li" : {
        5 : {
            "masa" : 9137.301603
        },
        6 : {
            "masa" : 10964.896818
            #Estable, abundancia 1.9%-7.8%
        },
        7 : {
            "masa" : 12789.391299
            #Estable, abundancia 98.1%-92.2%
        },
        8 : {
            "masa" : 14624.097601
        },
        9 : {
            "masa" : 16454.831830
        },
        "carga" : 3
    },
    "Be" : {
        7 : {
            "masa" : 12791.077471
            #Inestable, Traza
        },
        8 : {
            "masa" : 14592.778554
        },
        9 : {
            "masa" : 16428.204897
            #Estable, abundancia 100%
        },
        10 : {
            "masa" : 18253.556136
            #Inestable, Traza
        },
        11 : {
            "masa" : 20091.259267
        },
        "carga" : 4
    },
    "B" : {
        8 : {
            "masa" : 14627.963948
        },
        9 : {
            "masa" : 16430.293928
        },
        10 : {
            "masa" : 18252.466049
            #Estable, abundancia 18.9%-20.4%
        },
        11 : {
            "masa" : 20068.735657
            #Estable, abundancia 81.1&-79.6%
        },
        12 : {
            "masa" : 21900.824291
        },
        "carga" : 5
    },
    "C" : {
        10 : {
            "masa" : 18259.606303
        },
        11 : {
            "masa" : 20072.612941
        },
        12 : {
            "masa" : 21874.662195
            #Estable, abundancia 98.84%-99.04%
        },
        13 : {
            "masa" : 23703.66468
            #Estable, abundancia 1.16%-0.96%
        },
        14 : {
            "masa" : 25526.34721
            #Inestable, Traza
        },
        15 : {
            "masa" : 27362.64854
        },
        16 : {
            "masa" : 29193.014545
        },
        17 : {
            "masa" : 31030.263777
        },
        "carga" : 6
    },
    "N" : {
        12 : {
            "masa" : 21908.591619
        },
        13 : {
            "masa" : 23708.010446
        },
        14 : {
            "masa" : 25526.042787
            #Estable, abundancia 99.57%
        },
        15 : {
            "masa" : 27343.524616
            #Estable, abundancia 0.33%
        },
        16 : {
            "masa" : 29177.337704
        },
        17 : {
            "masa" : 31004.506362
        },
        18 : {
            "masa" : 32837.655918
        },
        "carga" : 7
    },
    "O" : {
        13 : {
            "masa" : 23742.78569
        },
        14 : {
            "masa" : 25536.108778
        },
        15 : {
            "masa" : 27348.914898
        },
        16 : {
            "masa" : 29156.94505
            #Estable, abundancia 99.73%-99.77%
        },
        17 : {
            "masa" : 30987.520687
            #Estable, abundancia 0.03%
        },
        18 : {
            "masa" : 32810.460244
            #Estable, abundancia 0.18%
        },
        19 : {
            "masa" : 34641.404105
        },
        20 : {
            "masa" : 36465.198597
        },
        21 : {
            "masa" : 38296.435943
        },
        "carga" : 8
    },
    "F" : {
        17 : {
            "masa" : 30992.923729
        },
        18 : {
            "masa" : 32813.70134
            #Inestable, Traza
        },
        19 : {
            "masa" : 34631.970657
            #Estable, abundancia 100%
        },
        20 : {
            "masa" : 36457.735691
        },
        21 : {
            "masa" : 38280.564052
        },
        22 : {
            "masa" : 40109.014201
        },
        23 : {
            "masa" : 41932.870672
        },
        "carga" : 9
    },
    "Ne" : {
        17 : {
            "masa" : 31021.395424
        },
        18 : {
            "masa" : 32822.398341
        },
        19 : {
            "masa" : 34638.30884
        },
        20 : {
            "masa" : 36443.989289
            #Estable, abundancia 90.48%
        },
        21 : {
            "masa" : 38269.440787
            #Estable, abundancia 0.27%
        },
        22 : {
            "masa" : 40087.843174
            #Estable, abundancia 9.25%
        },
        23 : {
            "masa" : 41916.34801
        },
        24 : {
            "masa" : 43737.676134
        },
        "carga" : 10
    },
    "Na" : {
        21 : {
            "masa" : 38276.382346
        },
        22 : {
            "masa" : 40093.40663
            #Inestable, Traza
        },
        23 : {
            "masa" : 41907.785903
            #Estable, abundancia 100%
        },
        24 : {
            "masa" : 43732.850948
            #Inestable, Traza
        },
        25 : {
            "masa" : 45553.90017
        },
        26 : {
            "masa" : 47381.67585
        },
        "carga" : 11
    },
    "Mg" : {
        22 : {
            "masa" : 40102.763517
        },
        23 : {
            "masa" : 41915.722759
        },
        24 : {
            "masa" : 43722.055802
            #Estable, abundancia 78.88%-79.05%
        },
        25 : {
            "masa" : 45546.393515
            #Estable, abundancia 9.98%-10.03%
        },
        26 : {
            "masa" : 47363.368581
            #Estable, abundancia 10.96%-11.09%
        },
        27 : {
            "masa" : 49189.443506
        },
        28 : {
            "masa" : 51011.484379
        },
        "carga" : 12
    },
    "Al" : {
        25 : {
            "masa" : 45554.764219
        },
        26 : {
            "masa" : 47371.205179
            #Inestable, Traza
        },
        27 : {
            "masa" : 49184.335773
            #Estable, abundancia 100%
        },
        28 : {
            "masa" : 51007.902404
        },
        29 : {
            "masa" : 52828.134971
        },
        "carga" : 13
    },
    "Si" : {
        26 : {
            "masa" : 47381.1253383
        },
        27 : {
            "masa" : 49193.752815
        },
        28 : {
            "masa" : 50998.817127
            #Estable, abundancia 92.22%
        },
        29 : {
            "masa" : 52820.918156
            #Estable, abundancia 4.68%
        },
        30 : {
            "masa" : 54638.841124
            #Estable, abundancia 3.09%
        },
        31 : {
            "masa" : 56464.633501
        },
        32 : {
            "masa" : 58285.312677
            #Inestable, Traza
        },
        "carga" : 14
    },
    "P" : {
        30 : {
            "masa" : 54647.122506
        },
        31 : {
            "masa" : 56461.713234
            #Estable, abundancia 100%
        },
        32 : {
            "masa" : 58284.867892
            #Inestable, Traza
        },
        33 : {
            "masa" : 60103.778866
            #Inestable, Traza
        },
        34 : {
            "masa" : 61930.167328
        },
        "carga" : 15
    },
    "S" : {
        31 : {
            "masa" : 56472.278696
        },
        32 : {
            "masa" : 58281.521069
            #Estable, abundancia 94.99%
        },
        33 : {
            "masa" : 60103.292154
            #Estable, abundancia 0.75%
        },
        34 : {
            "masa" : 61919.634678
            #Estable, abundancia 4.25%
        },
        35 : {
            "masa" : 63744.64686
            #Intestable, Traza
        },
        36 : {
            "masa" : 65563.977097
            #Estable, abundancia 0.01%
        },
        37 : {
            "masa" : 67394.239198
        },
        "carga" : 16
    },
    "Cl" : {
        34 : {
            "masa" : 61930.380606
        },
        35 : {
            "masa" : 63744.31874
            #Estable, abundancia 75.76%
        },
        36 : {
            "masa" : 65566.211959
            #Inestable, Traza
        },
        37 : {
            "masa" : 67384.718251
            #Estable, abundancia 24.24%
        },
        38 : {
            "masa" : 69211.449416
        },
        "carga" : 17
    },
    "Ar" : {
        35 : {
            "masa" : 63755.994341
        },
        36 : {
            "masa" : 65564.824741
            #Estable, abundancia 0.33%
        },
        37 : {
            "masa" : 67386.311456
        },
        38 : {
            "masa" : 69201.828211
            #Estable, abundancia 0.06%
        },
        39 : {
            "masa" : 71027.598714
            #Inestable, Traza
        },
        40 : {
            "masa" : 72846.969055
            #Estable, abundancia 99.6%
        },
        41 : {
            "masa" : 74673.71772
        },
        42 : {
            "masa" : 76493.954663
            #Inestable, Traza
        },
        43 : {
            "masa" : 78321.564461
        },
        "carga" : 18
    },
    "K" : {
        38 : {
            "masa" : 69213.40173
        },
        39 : {
            "masa" : 71026.492221
            #Estable, abundancia 93.25%
        },
        40 : {
            "masa" : 72849.913020
            #Inestable, abundancia 0.017%
        },
        41 : {
            "masa" : 74668.8404
            #Estable, abundancia 6.73%
        },
        42 : {
            "masa" : 76492.780723
            #Inestable, Traza
        },
        43 : {
            "masa" : 78312.628661
        },
        "carga" : 19
    },
    "Ca" : {
        39 : {
            "masa" : 71039.259732
        },
        40 : {
            "masa" : 72847.346393
            #Estable, abundancia 96.94%
        },
        41 : {
            "masa" : 74669.664346
            #Inestable, Traza
        },
        42 : {
            "masa" : 76485.881090
            #Estable, abundancia 0.64%
        },
        43 : {
            "masa" : 78309.041217
            #Estable, abundancia 0.13%
        },
        44 : {
            "masa" : 80125.941544
            #Estable, abundancia 2.08%
        },
        45 : {
            "masa" : 81950.115197
        },
        46 : {
            "masa" : 83768.450138
            #Estable, abundancia 0.04%
        },
        47 : {
            "masa" : 85592.893578
        },
        48 : {
            "masa" : 87412.101682
        },
        49 : {
            "masa" : 89240.641153
            #Inestable, abundancia 0.18%
        },
        "carga" : 20
    },
    "Sc" : {
        44 : {
            "masa" : 80133.08909
        },
        45 : {
            "masa" : 81949.613903
            #Estable, abundancia 100%
        },
        46 : {
            "masa" : 83771.153481
        },
        47 : {
            "masa" : 85589.003534
        },
        "carga" : 21
    },
    "Ti" : {
        44 : {
            "masa" : 80133.614082
        },
        45 : {
            "masa" : 81953.649778
        },
        46 : {
            "masa" : 83766.523345
            #Estable, abundancia 8.25%
        },
        47 : {
            "masa" : 85587.829594
            #Estable, abundancia 7.44%
        },
        48 : {
            "masa" : 87403.760145
            #Estable, abundancia 73.72%
        },
        49 : {
            "masa" : 89226.510121
            #Estable, abundancia 5.41%
        },
        50 : {
            "masa" : 91043.785964
            #Estable, abundancia 5.18%
        },
        51 : {
            "masa" : 92869.999429
        },
        "carga" : 22
    },
    "V" : {
        48 : {
            "masa" : 87411.611325
        },
        49 : {
            "masa" : 89227.687707
        },
        50 : {
            "masa" : 91048.100741
            #Inestable, abundancia 0.25%
        },
        51 : {
            "masa" : 92865.157837
            #Estable, abundancia 99.75%
        },
        52 : {
            "masa" : 94689.533830
        },
        "carga" : 23
    },
    "Cr" : {
        50 : {
            "masa" : 91046.070043
            #Estable, abundancia 4.34%
        },
        51 : {
            "masa" : 92866.630731
        },
        52 : {
            "masa" : 94681.753742
            #Estable, abundancia 83.78%
        },
        53 : {
            "masa" : 96504.901109
            #Estable, abundancia 9.5%
        },
        54 : {
            "masa" : 98324.564935
            #Estable, abundancia 2.36%
        },
        55 : {
            "masa" : 100151.024490
        },
        "carga" : 24
    },
    "Mn" : {
        52 : {
            "masa" : 94690.973912
        },
        53 : {
            "masa" : 96506.069580
            #Inestable, Traza
        },
        54 : {
            "masa" : 98327.259165
        },
        55 : {
            "masa" : 100145.931340
            #Estable, abundancia 100%
        },
        56 : {
            "masa" : 101970.385717
        },
        "carga" : 25
    },
    "Fe" : {
        53 : {
            "masa" : 96513.392123
        },
        54 : {
            "masa" : 98325.893821
            #Estable, abundancia 5.84%
        },
        55 : {
            "masa" : 100146.383416
        },
        56 : {
            "masa" : 101963.152496
            #Estable, abundancia 91.75%
        },
        57 : {
            "masa" : 103786.872249
            #Estable, abundancia 2.11%
        },
        58 : {
            "masa" : 105605.899888
            #Estable, abundancia 0.28%
        },
        59 : {
            "masa" : 107431.706848
        },
        "carga" : 26
    }
}
