# This file was automatically created by FeynRules 2.0.6
# Mathematica version: 9.0 for Mac OS X x86 (64-bit) (January 28, 2013)
# Date: Sat 4 Jan 2014 00:16:06


from object_library import all_couplings, Coupling

from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot



GC_1 = Coupling(name = 'GC_1',
                value = '-(ee*complex(0,1))/3.',
                order = {'QED':1})

GC_2 = Coupling(name = 'GC_2',
                value = '(2*ee*complex(0,1))/3.',
                order = {'QED':1})

GC_3 = Coupling(name = 'GC_3',
                value = '-(ee*complex(0,1))',
                order = {'QED':1})

GC_4 = Coupling(name = 'GC_4',
                value = '(ee*complex(0,1))/cw',
                order = {'QED':1})

GC_5 = Coupling(name = 'GC_5',
                value = '-G',
                order = {'QCD':1})

GC_6 = Coupling(name = 'GC_6',
                value = 'complex(0,1)*G',
                order = {'QCD':1})

GC_7 = Coupling(name = 'GC_7',
                value = 'complex(0,1)*G**2',
                order = {'QCD':2})

GC_8 = Coupling(name = 'GC_8',
                value = 'cw*complex(0,1)*gw',
                order = {'QED':1})

GC_9 = Coupling(name = 'GC_9',
                value = '(complex(0,1)*gw**2)/2.',
                order = {'QED':2})

GC_10 = Coupling(name = 'GC_10',
                 value = '-(complex(0,1)*gw**2)',
                 order = {'QED':2})

GC_11 = Coupling(name = 'GC_11',
                 value = 'cw**2*complex(0,1)*gw**2',
                 order = {'QED':2})

GC_12 = Coupling(name = 'GC_12',
                 value = '-4*complex(0,1)*l2',
                 order = {'QED':2})

GC_13 = Coupling(name = 'GC_13',
                 value = 'complex(0,1)*lambdaZp',
                 order = {'S1VV':1})

GC_14 = Coupling(name = 'GC_14',
                 value = '(ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_15 = Coupling(name = 'GC_15',
                 value = '(CKM1x1*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_16 = Coupling(name = 'GC_16',
                 value = '(CKM1x2*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_17 = Coupling(name = 'GC_17',
                 value = '(CKM2x1*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_18 = Coupling(name = 'GC_18',
                 value = '(CKM2x2*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_19 = Coupling(name = 'GC_19',
                 value = '-(cw*ee*complex(0,1))/(2.*sw)',
                 order = {'QED':1})

GC_20 = Coupling(name = 'GC_20',
                 value = '(cw*ee*complex(0,1))/(2.*sw)',
                 order = {'QED':1})

GC_21 = Coupling(name = 'GC_21',
                 value = '-(ee*complex(0,1)*sw)/(6.*cw)',
                 order = {'QED':1})

GC_22 = Coupling(name = 'GC_22',
                 value = '(ee*complex(0,1)*sw)/(2.*cw)',
                 order = {'QED':1})

GC_23 = Coupling(name = 'GC_23',
                 value = 'complex(0,1)*gw*sw',
                 order = {'QED':1})

GC_24 = Coupling(name = 'GC_24',
                 value = '-2*cw*complex(0,1)*gw**2*sw',
                 order = {'QED':2})

GC_25 = Coupling(name = 'GC_25',
                 value = 'complex(0,1)*gw**2*sw**2',
                 order = {'QED':2})

GC_26 = Coupling(name = 'GC_26',
                 value = '(cw*ee*complex(0,1))/(2.*sw) + (ee*complex(0,1)*sw)/(2.*cw)',
                 order = {'QED':1})

GC_27 = Coupling(name = 'GC_27',
                 value = '-(cw*complex(0,1)*gw)/2. + (complex(0,1)*g1*sw)/2.',
                 order = {'QED':1})

GC_28 = Coupling(name = 'GC_28',
                 value = '-(cw*complex(0,1)*g1)/2. - (complex(0,1)*gw*sw)/2.',
                 order = {'QED':1})

GC_29 = Coupling(name = 'GC_29',
                 value = '(cw**2*complex(0,1)*gw**2)/2. - cw*complex(0,1)*g1*gw*sw + (complex(0,1)*g1**2*sw**2)/2.',
                 order = {'QED':2})

GC_30 = Coupling(name = 'GC_30',
                 value = '(cw**2*complex(0,1)*g1*gw)/2. - (cw*complex(0,1)*g1**2*sw)/2. + (cw*complex(0,1)*gw**2*sw)/2. - (complex(0,1)*g1*gw*sw**2)/2.',
                 order = {'QED':2})

GC_31 = Coupling(name = 'GC_31',
                 value = '(cw**2*complex(0,1)*g1**2)/2. + cw*complex(0,1)*g1*gw*sw + (complex(0,1)*gw**2*sw**2)/2.',
                 order = {'QED':2})

GC_32 = Coupling(name = 'GC_32',
                 value = '-(complex(0,1)*gw*TH2x1)/2. + (gw*TH3x1)/2.',
                 order = {'QED':1})

GC_33 = Coupling(name = 'GC_33',
                 value = '(complex(0,1)*gw*TH2x1)/2. + (gw*TH3x1)/2.',
                 order = {'QED':1})

GC_34 = Coupling(name = 'GC_34',
                 value = '(cw*complex(0,1)*g1*gw*TH2x1)/2. - (cw*g1*gw*TH3x1)/2.',
                 order = {'QED':2})

GC_35 = Coupling(name = 'GC_35',
                 value = '(cw*complex(0,1)*g1*gw*TH2x1)/2. + (cw*g1*gw*TH3x1)/2.',
                 order = {'QED':2})

GC_36 = Coupling(name = 'GC_36',
                 value = '-(complex(0,1)*g1*gw*sw*TH2x1)/2. - (g1*gw*sw*TH3x1)/2.',
                 order = {'QED':2})

GC_37 = Coupling(name = 'GC_37',
                 value = '-(complex(0,1)*g1*gw*sw*TH2x1)/2. + (g1*gw*sw*TH3x1)/2.',
                 order = {'QED':2})

GC_38 = Coupling(name = 'GC_38',
                 value = '(complex(0,1)*gw**2*TH1x1**2)/2. + (complex(0,1)*gw**2*TH2x1**2)/2. + (complex(0,1)*gw**2*TH3x1**2)/2.',
                 order = {'QED':2})

GC_39 = Coupling(name = 'GC_39',
                 value = '(cw**2*complex(0,1)*gw**2*TH1x1**2)/2. + cw*complex(0,1)*g1*gw*sw*TH1x1**2 + (complex(0,1)*g1**2*sw**2*TH1x1**2)/2. + (cw**2*complex(0,1)*gw**2*TH2x1**2)/2. + cw*complex(0,1)*g1*gw*sw*TH2x1**2 + (complex(0,1)*g1**2*sw**2*TH2x1**2)/2. + (cw**2*complex(0,1)*gw**2*TH3x1**2)/2. + cw*complex(0,1)*g1*gw*sw*TH3x1**2 + (complex(0,1)*g1**2*sw**2*TH3x1**2)/2.',
                 order = {'QED':2})

GC_40 = Coupling(name = 'GC_40',
                 value = '-(cw**2*complex(0,1)*g1*gw*TH1x1**2)/2. - (cw*complex(0,1)*g1**2*sw*TH1x1**2)/2. + (cw*complex(0,1)*gw**2*sw*TH1x1**2)/2. + (complex(0,1)*g1*gw*sw**2*TH1x1**2)/2. - (cw**2*complex(0,1)*g1*gw*TH2x1**2)/2. - (cw*complex(0,1)*g1**2*sw*TH2x1**2)/2. + (cw*complex(0,1)*gw**2*sw*TH2x1**2)/2. + (complex(0,1)*g1*gw*sw**2*TH2x1**2)/2. - (cw**2*complex(0,1)*g1*gw*TH3x1**2)/2. - (cw*complex(0,1)*g1**2*sw*TH3x1**2)/2. + (cw*complex(0,1)*gw**2*sw*TH3x1**2)/2. + (complex(0,1)*g1*gw*sw**2*TH3x1**2)/2.',
                 order = {'QED':2})

GC_41 = Coupling(name = 'GC_41',
                 value = '(cw**2*complex(0,1)*g1**2*TH1x1**2)/2. - cw*complex(0,1)*g1*gw*sw*TH1x1**2 + (complex(0,1)*gw**2*sw**2*TH1x1**2)/2. + (cw**2*complex(0,1)*g1**2*TH2x1**2)/2. - cw*complex(0,1)*g1*gw*sw*TH2x1**2 + (complex(0,1)*gw**2*sw**2*TH2x1**2)/2. + (cw**2*complex(0,1)*g1**2*TH3x1**2)/2. - cw*complex(0,1)*g1*gw*sw*TH3x1**2 + (complex(0,1)*gw**2*sw**2*TH3x1**2)/2.',
                 order = {'QED':2})

GC_42 = Coupling(name = 'GC_42',
                 value = '-(complex(0,1)*gw*TH2x2)/2. + (gw*TH3x2)/2.',
                 order = {'QED':1})

GC_43 = Coupling(name = 'GC_43',
                 value = '(complex(0,1)*gw*TH2x2)/2. + (gw*TH3x2)/2.',
                 order = {'QED':1})

GC_44 = Coupling(name = 'GC_44',
                 value = '(cw*complex(0,1)*g1*gw*TH2x2)/2. - (cw*g1*gw*TH3x2)/2.',
                 order = {'QED':2})

GC_45 = Coupling(name = 'GC_45',
                 value = '(cw*complex(0,1)*g1*gw*TH2x2)/2. + (cw*g1*gw*TH3x2)/2.',
                 order = {'QED':2})

GC_46 = Coupling(name = 'GC_46',
                 value = '-(complex(0,1)*g1*gw*sw*TH2x2)/2. - (g1*gw*sw*TH3x2)/2.',
                 order = {'QED':2})

GC_47 = Coupling(name = 'GC_47',
                 value = '-(complex(0,1)*g1*gw*sw*TH2x2)/2. + (g1*gw*sw*TH3x2)/2.',
                 order = {'QED':2})

GC_48 = Coupling(name = 'GC_48',
                 value = '-(cw*gw*TH2x2*TH3x1)/2. - (g1*sw*TH2x2*TH3x1)/2. + (cw*gw*TH2x1*TH3x2)/2. + (g1*sw*TH2x1*TH3x2)/2.',
                 order = {'QED':1})

GC_49 = Coupling(name = 'GC_49',
                 value = '(cw*g1*TH2x2*TH3x1)/2. - (gw*sw*TH2x2*TH3x1)/2. - (cw*g1*TH2x1*TH3x2)/2. + (gw*sw*TH2x1*TH3x2)/2.',
                 order = {'QED':1})

GC_50 = Coupling(name = 'GC_50',
                 value = '(complex(0,1)*gw**2*TH1x1*TH1x2)/2. + (complex(0,1)*gw**2*TH2x1*TH2x2)/2. + (complex(0,1)*gw**2*TH3x1*TH3x2)/2.',
                 order = {'QED':2})

GC_51 = Coupling(name = 'GC_51',
                 value = '(cw**2*complex(0,1)*gw**2*TH1x1*TH1x2)/2. + cw*complex(0,1)*g1*gw*sw*TH1x1*TH1x2 + (complex(0,1)*g1**2*sw**2*TH1x1*TH1x2)/2. + (cw**2*complex(0,1)*gw**2*TH2x1*TH2x2)/2. + cw*complex(0,1)*g1*gw*sw*TH2x1*TH2x2 + (complex(0,1)*g1**2*sw**2*TH2x1*TH2x2)/2. + (cw**2*complex(0,1)*gw**2*TH3x1*TH3x2)/2. + cw*complex(0,1)*g1*gw*sw*TH3x1*TH3x2 + (complex(0,1)*g1**2*sw**2*TH3x1*TH3x2)/2.',
                 order = {'QED':2})

GC_52 = Coupling(name = 'GC_52',
                 value = '-(cw**2*complex(0,1)*g1*gw*TH1x1*TH1x2)/2. - (cw*complex(0,1)*g1**2*sw*TH1x1*TH1x2)/2. + (cw*complex(0,1)*gw**2*sw*TH1x1*TH1x2)/2. + (complex(0,1)*g1*gw*sw**2*TH1x1*TH1x2)/2. - (cw**2*complex(0,1)*g1*gw*TH2x1*TH2x2)/2. - (cw*complex(0,1)*g1**2*sw*TH2x1*TH2x2)/2. + (cw*complex(0,1)*gw**2*sw*TH2x1*TH2x2)/2. + (complex(0,1)*g1*gw*sw**2*TH2x1*TH2x2)/2. - (cw**2*complex(0,1)*g1*gw*TH3x1*TH3x2)/2. - (cw*complex(0,1)*g1**2*sw*TH3x1*TH3x2)/2. + (cw*complex(0,1)*gw**2*sw*TH3x1*TH3x2)/2. + (complex(0,1)*g1*gw*sw**2*TH3x1*TH3x2)/2.',
                 order = {'QED':2})

GC_53 = Coupling(name = 'GC_53',
                 value = '(cw**2*complex(0,1)*g1**2*TH1x1*TH1x2)/2. - cw*complex(0,1)*g1*gw*sw*TH1x1*TH1x2 + (complex(0,1)*gw**2*sw**2*TH1x1*TH1x2)/2. + (cw**2*complex(0,1)*g1**2*TH2x1*TH2x2)/2. - cw*complex(0,1)*g1*gw*sw*TH2x1*TH2x2 + (complex(0,1)*gw**2*sw**2*TH2x1*TH2x2)/2. + (cw**2*complex(0,1)*g1**2*TH3x1*TH3x2)/2. - cw*complex(0,1)*g1*gw*sw*TH3x1*TH3x2 + (complex(0,1)*gw**2*sw**2*TH3x1*TH3x2)/2.',
                 order = {'QED':2})

GC_54 = Coupling(name = 'GC_54',
                 value = '(complex(0,1)*gw**2*TH1x2**2)/2. + (complex(0,1)*gw**2*TH2x2**2)/2. + (complex(0,1)*gw**2*TH3x2**2)/2.',
                 order = {'QED':2})

GC_55 = Coupling(name = 'GC_55',
                 value = '(cw**2*complex(0,1)*gw**2*TH1x2**2)/2. + cw*complex(0,1)*g1*gw*sw*TH1x2**2 + (complex(0,1)*g1**2*sw**2*TH1x2**2)/2. + (cw**2*complex(0,1)*gw**2*TH2x2**2)/2. + cw*complex(0,1)*g1*gw*sw*TH2x2**2 + (complex(0,1)*g1**2*sw**2*TH2x2**2)/2. + (cw**2*complex(0,1)*gw**2*TH3x2**2)/2. + cw*complex(0,1)*g1*gw*sw*TH3x2**2 + (complex(0,1)*g1**2*sw**2*TH3x2**2)/2.',
                 order = {'QED':2})

GC_56 = Coupling(name = 'GC_56',
                 value = '-(cw**2*complex(0,1)*g1*gw*TH1x2**2)/2. - (cw*complex(0,1)*g1**2*sw*TH1x2**2)/2. + (cw*complex(0,1)*gw**2*sw*TH1x2**2)/2. + (complex(0,1)*g1*gw*sw**2*TH1x2**2)/2. - (cw**2*complex(0,1)*g1*gw*TH2x2**2)/2. - (cw*complex(0,1)*g1**2*sw*TH2x2**2)/2. + (cw*complex(0,1)*gw**2*sw*TH2x2**2)/2. + (complex(0,1)*g1*gw*sw**2*TH2x2**2)/2. - (cw**2*complex(0,1)*g1*gw*TH3x2**2)/2. - (cw*complex(0,1)*g1**2*sw*TH3x2**2)/2. + (cw*complex(0,1)*gw**2*sw*TH3x2**2)/2. + (complex(0,1)*g1*gw*sw**2*TH3x2**2)/2.',
                 order = {'QED':2})

GC_57 = Coupling(name = 'GC_57',
                 value = '(cw**2*complex(0,1)*g1**2*TH1x2**2)/2. - cw*complex(0,1)*g1*gw*sw*TH1x2**2 + (complex(0,1)*gw**2*sw**2*TH1x2**2)/2. + (cw**2*complex(0,1)*g1**2*TH2x2**2)/2. - cw*complex(0,1)*g1*gw*sw*TH2x2**2 + (complex(0,1)*gw**2*sw**2*TH2x2**2)/2. + (cw**2*complex(0,1)*g1**2*TH3x2**2)/2. - cw*complex(0,1)*g1*gw*sw*TH3x2**2 + (complex(0,1)*gw**2*sw**2*TH3x2**2)/2.',
                 order = {'QED':2})

GC_58 = Coupling(name = 'GC_58',
                 value = '-(complex(0,1)*gw*TH2x3)/2. + (gw*TH3x3)/2.',
                 order = {'QED':1})

GC_59 = Coupling(name = 'GC_59',
                 value = '(complex(0,1)*gw*TH2x3)/2. + (gw*TH3x3)/2.',
                 order = {'QED':1})

GC_60 = Coupling(name = 'GC_60',
                 value = '(cw*complex(0,1)*g1*gw*TH2x3)/2. - (cw*g1*gw*TH3x3)/2.',
                 order = {'QED':2})

GC_61 = Coupling(name = 'GC_61',
                 value = '(cw*complex(0,1)*g1*gw*TH2x3)/2. + (cw*g1*gw*TH3x3)/2.',
                 order = {'QED':2})

GC_62 = Coupling(name = 'GC_62',
                 value = '-(complex(0,1)*g1*gw*sw*TH2x3)/2. - (g1*gw*sw*TH3x3)/2.',
                 order = {'QED':2})

GC_63 = Coupling(name = 'GC_63',
                 value = '-(complex(0,1)*g1*gw*sw*TH2x3)/2. + (g1*gw*sw*TH3x3)/2.',
                 order = {'QED':2})

GC_64 = Coupling(name = 'GC_64',
                 value = '-(cw*gw*TH2x3*TH3x1)/2. - (g1*sw*TH2x3*TH3x1)/2. + (cw*gw*TH2x1*TH3x3)/2. + (g1*sw*TH2x1*TH3x3)/2.',
                 order = {'QED':1})

GC_65 = Coupling(name = 'GC_65',
                 value = '(cw*g1*TH2x3*TH3x1)/2. - (gw*sw*TH2x3*TH3x1)/2. - (cw*g1*TH2x1*TH3x3)/2. + (gw*sw*TH2x1*TH3x3)/2.',
                 order = {'QED':1})

GC_66 = Coupling(name = 'GC_66',
                 value = '-(cw*gw*TH2x3*TH3x2)/2. - (g1*sw*TH2x3*TH3x2)/2. + (cw*gw*TH2x2*TH3x3)/2. + (g1*sw*TH2x2*TH3x3)/2.',
                 order = {'QED':1})

GC_67 = Coupling(name = 'GC_67',
                 value = '(cw*g1*TH2x3*TH3x2)/2. - (gw*sw*TH2x3*TH3x2)/2. - (cw*g1*TH2x2*TH3x3)/2. + (gw*sw*TH2x2*TH3x3)/2.',
                 order = {'QED':1})

GC_68 = Coupling(name = 'GC_68',
                 value = '(complex(0,1)*gw**2*TH1x1*TH1x3)/2. + (complex(0,1)*gw**2*TH2x1*TH2x3)/2. + (complex(0,1)*gw**2*TH3x1*TH3x3)/2.',
                 order = {'QED':2})

GC_69 = Coupling(name = 'GC_69',
                 value = '(cw**2*complex(0,1)*gw**2*TH1x1*TH1x3)/2. + cw*complex(0,1)*g1*gw*sw*TH1x1*TH1x3 + (complex(0,1)*g1**2*sw**2*TH1x1*TH1x3)/2. + (cw**2*complex(0,1)*gw**2*TH2x1*TH2x3)/2. + cw*complex(0,1)*g1*gw*sw*TH2x1*TH2x3 + (complex(0,1)*g1**2*sw**2*TH2x1*TH2x3)/2. + (cw**2*complex(0,1)*gw**2*TH3x1*TH3x3)/2. + cw*complex(0,1)*g1*gw*sw*TH3x1*TH3x3 + (complex(0,1)*g1**2*sw**2*TH3x1*TH3x3)/2.',
                 order = {'QED':2})

GC_70 = Coupling(name = 'GC_70',
                 value = '-(cw**2*complex(0,1)*g1*gw*TH1x1*TH1x3)/2. - (cw*complex(0,1)*g1**2*sw*TH1x1*TH1x3)/2. + (cw*complex(0,1)*gw**2*sw*TH1x1*TH1x3)/2. + (complex(0,1)*g1*gw*sw**2*TH1x1*TH1x3)/2. - (cw**2*complex(0,1)*g1*gw*TH2x1*TH2x3)/2. - (cw*complex(0,1)*g1**2*sw*TH2x1*TH2x3)/2. + (cw*complex(0,1)*gw**2*sw*TH2x1*TH2x3)/2. + (complex(0,1)*g1*gw*sw**2*TH2x1*TH2x3)/2. - (cw**2*complex(0,1)*g1*gw*TH3x1*TH3x3)/2. - (cw*complex(0,1)*g1**2*sw*TH3x1*TH3x3)/2. + (cw*complex(0,1)*gw**2*sw*TH3x1*TH3x3)/2. + (complex(0,1)*g1*gw*sw**2*TH3x1*TH3x3)/2.',
                 order = {'QED':2})

GC_71 = Coupling(name = 'GC_71',
                 value = '(cw**2*complex(0,1)*g1**2*TH1x1*TH1x3)/2. - cw*complex(0,1)*g1*gw*sw*TH1x1*TH1x3 + (complex(0,1)*gw**2*sw**2*TH1x1*TH1x3)/2. + (cw**2*complex(0,1)*g1**2*TH2x1*TH2x3)/2. - cw*complex(0,1)*g1*gw*sw*TH2x1*TH2x3 + (complex(0,1)*gw**2*sw**2*TH2x1*TH2x3)/2. + (cw**2*complex(0,1)*g1**2*TH3x1*TH3x3)/2. - cw*complex(0,1)*g1*gw*sw*TH3x1*TH3x3 + (complex(0,1)*gw**2*sw**2*TH3x1*TH3x3)/2.',
                 order = {'QED':2})

GC_72 = Coupling(name = 'GC_72',
                 value = '(complex(0,1)*gw**2*TH1x2*TH1x3)/2. + (complex(0,1)*gw**2*TH2x2*TH2x3)/2. + (complex(0,1)*gw**2*TH3x2*TH3x3)/2.',
                 order = {'QED':2})

GC_73 = Coupling(name = 'GC_73',
                 value = '(cw**2*complex(0,1)*gw**2*TH1x2*TH1x3)/2. + cw*complex(0,1)*g1*gw*sw*TH1x2*TH1x3 + (complex(0,1)*g1**2*sw**2*TH1x2*TH1x3)/2. + (cw**2*complex(0,1)*gw**2*TH2x2*TH2x3)/2. + cw*complex(0,1)*g1*gw*sw*TH2x2*TH2x3 + (complex(0,1)*g1**2*sw**2*TH2x2*TH2x3)/2. + (cw**2*complex(0,1)*gw**2*TH3x2*TH3x3)/2. + cw*complex(0,1)*g1*gw*sw*TH3x2*TH3x3 + (complex(0,1)*g1**2*sw**2*TH3x2*TH3x3)/2.',
                 order = {'QED':2})

GC_74 = Coupling(name = 'GC_74',
                 value = '-(cw**2*complex(0,1)*g1*gw*TH1x2*TH1x3)/2. - (cw*complex(0,1)*g1**2*sw*TH1x2*TH1x3)/2. + (cw*complex(0,1)*gw**2*sw*TH1x2*TH1x3)/2. + (complex(0,1)*g1*gw*sw**2*TH1x2*TH1x3)/2. - (cw**2*complex(0,1)*g1*gw*TH2x2*TH2x3)/2. - (cw*complex(0,1)*g1**2*sw*TH2x2*TH2x3)/2. + (cw*complex(0,1)*gw**2*sw*TH2x2*TH2x3)/2. + (complex(0,1)*g1*gw*sw**2*TH2x2*TH2x3)/2. - (cw**2*complex(0,1)*g1*gw*TH3x2*TH3x3)/2. - (cw*complex(0,1)*g1**2*sw*TH3x2*TH3x3)/2. + (cw*complex(0,1)*gw**2*sw*TH3x2*TH3x3)/2. + (complex(0,1)*g1*gw*sw**2*TH3x2*TH3x3)/2.',
                 order = {'QED':2})

GC_75 = Coupling(name = 'GC_75',
                 value = '(cw**2*complex(0,1)*g1**2*TH1x2*TH1x3)/2. - cw*complex(0,1)*g1*gw*sw*TH1x2*TH1x3 + (complex(0,1)*gw**2*sw**2*TH1x2*TH1x3)/2. + (cw**2*complex(0,1)*g1**2*TH2x2*TH2x3)/2. - cw*complex(0,1)*g1*gw*sw*TH2x2*TH2x3 + (complex(0,1)*gw**2*sw**2*TH2x2*TH2x3)/2. + (cw**2*complex(0,1)*g1**2*TH3x2*TH3x3)/2. - cw*complex(0,1)*g1*gw*sw*TH3x2*TH3x3 + (complex(0,1)*gw**2*sw**2*TH3x2*TH3x3)/2.',
                 order = {'QED':2})

GC_76 = Coupling(name = 'GC_76',
                 value = '(complex(0,1)*gw**2*TH1x3**2)/2. + (complex(0,1)*gw**2*TH2x3**2)/2. + (complex(0,1)*gw**2*TH3x3**2)/2.',
                 order = {'QED':2})

GC_77 = Coupling(name = 'GC_77',
                 value = '(cw**2*complex(0,1)*gw**2*TH1x3**2)/2. + cw*complex(0,1)*g1*gw*sw*TH1x3**2 + (complex(0,1)*g1**2*sw**2*TH1x3**2)/2. + (cw**2*complex(0,1)*gw**2*TH2x3**2)/2. + cw*complex(0,1)*g1*gw*sw*TH2x3**2 + (complex(0,1)*g1**2*sw**2*TH2x3**2)/2. + (cw**2*complex(0,1)*gw**2*TH3x3**2)/2. + cw*complex(0,1)*g1*gw*sw*TH3x3**2 + (complex(0,1)*g1**2*sw**2*TH3x3**2)/2.',
                 order = {'QED':2})

GC_78 = Coupling(name = 'GC_78',
                 value = '-(cw**2*complex(0,1)*g1*gw*TH1x3**2)/2. - (cw*complex(0,1)*g1**2*sw*TH1x3**2)/2. + (cw*complex(0,1)*gw**2*sw*TH1x3**2)/2. + (complex(0,1)*g1*gw*sw**2*TH1x3**2)/2. - (cw**2*complex(0,1)*g1*gw*TH2x3**2)/2. - (cw*complex(0,1)*g1**2*sw*TH2x3**2)/2. + (cw*complex(0,1)*gw**2*sw*TH2x3**2)/2. + (complex(0,1)*g1*gw*sw**2*TH2x3**2)/2. - (cw**2*complex(0,1)*g1*gw*TH3x3**2)/2. - (cw*complex(0,1)*g1**2*sw*TH3x3**2)/2. + (cw*complex(0,1)*gw**2*sw*TH3x3**2)/2. + (complex(0,1)*g1*gw*sw**2*TH3x3**2)/2.',
                 order = {'QED':2})

GC_79 = Coupling(name = 'GC_79',
                 value = '(cw**2*complex(0,1)*g1**2*TH1x3**2)/2. - cw*complex(0,1)*g1*gw*sw*TH1x3**2 + (complex(0,1)*gw**2*sw**2*TH1x3**2)/2. + (cw**2*complex(0,1)*g1**2*TH2x3**2)/2. - cw*complex(0,1)*g1*gw*sw*TH2x3**2 + (complex(0,1)*gw**2*sw**2*TH2x3**2)/2. + (cw**2*complex(0,1)*g1**2*TH3x3**2)/2. - cw*complex(0,1)*g1*gw*sw*TH3x3**2 + (complex(0,1)*gw**2*sw**2*TH3x3**2)/2.',
                 order = {'QED':2})

GC_80 = Coupling(name = 'GC_80',
                 value = '-((complex(0,1)*GL1x1*TH2x1)/v) + (GL1x1*TH3x1)/v',
                 order = {'QED':1})

GC_81 = Coupling(name = 'GC_81',
                 value = '-((complex(0,1)*GL1x2*TH2x1)/v) + (GL1x2*TH3x1)/v',
                 order = {'QED':1})

GC_82 = Coupling(name = 'GC_82',
                 value = '-((complex(0,1)*GL1x3*TH2x1)/v) + (GL1x3*TH3x1)/v',
                 order = {'QED':1})

GC_83 = Coupling(name = 'GC_83',
                 value = '-((complex(0,1)*GL2x1*TH2x1)/v) + (GL2x1*TH3x1)/v',
                 order = {'QED':1})

GC_84 = Coupling(name = 'GC_84',
                 value = '-((complex(0,1)*GL2x2*TH2x1)/v) + (GL2x2*TH3x1)/v',
                 order = {'QED':1})

GC_85 = Coupling(name = 'GC_85',
                 value = '-((complex(0,1)*GL2x3*TH2x1)/v) + (GL2x3*TH3x1)/v',
                 order = {'QED':1})

GC_86 = Coupling(name = 'GC_86',
                 value = '-((complex(0,1)*GL3x1*TH2x1)/v) + (GL3x1*TH3x1)/v',
                 order = {'QED':1})

GC_87 = Coupling(name = 'GC_87',
                 value = '-((complex(0,1)*GL3x2*TH2x1)/v) + (GL3x2*TH3x1)/v',
                 order = {'QED':1})

GC_88 = Coupling(name = 'GC_88',
                 value = '-((complex(0,1)*GL3x3*TH2x1)/v) + (GL3x3*TH3x1)/v',
                 order = {'QED':1})

GC_89 = Coupling(name = 'GC_89',
                 value = '-((complex(0,1)*GL1x1*TH2x2)/v) + (GL1x1*TH3x2)/v',
                 order = {'QED':1})

GC_90 = Coupling(name = 'GC_90',
                 value = '-((complex(0,1)*GL1x2*TH2x2)/v) + (GL1x2*TH3x2)/v',
                 order = {'QED':1})

GC_91 = Coupling(name = 'GC_91',
                 value = '-((complex(0,1)*GL1x3*TH2x2)/v) + (GL1x3*TH3x2)/v',
                 order = {'QED':1})

GC_92 = Coupling(name = 'GC_92',
                 value = '-((complex(0,1)*GL2x1*TH2x2)/v) + (GL2x1*TH3x2)/v',
                 order = {'QED':1})

GC_93 = Coupling(name = 'GC_93',
                 value = '-((complex(0,1)*GL2x2*TH2x2)/v) + (GL2x2*TH3x2)/v',
                 order = {'QED':1})

GC_94 = Coupling(name = 'GC_94',
                 value = '-((complex(0,1)*GL2x3*TH2x2)/v) + (GL2x3*TH3x2)/v',
                 order = {'QED':1})

GC_95 = Coupling(name = 'GC_95',
                 value = '-((complex(0,1)*GL3x1*TH2x2)/v) + (GL3x1*TH3x2)/v',
                 order = {'QED':1})

GC_96 = Coupling(name = 'GC_96',
                 value = '-((complex(0,1)*GL3x2*TH2x2)/v) + (GL3x2*TH3x2)/v',
                 order = {'QED':1})

GC_97 = Coupling(name = 'GC_97',
                 value = '-((complex(0,1)*GL3x3*TH2x2)/v) + (GL3x3*TH3x2)/v',
                 order = {'QED':1})

GC_98 = Coupling(name = 'GC_98',
                 value = '-((complex(0,1)*GL1x1*TH2x3)/v) + (GL1x1*TH3x3)/v',
                 order = {'QED':1})

GC_99 = Coupling(name = 'GC_99',
                 value = '-((complex(0,1)*GL1x2*TH2x3)/v) + (GL1x2*TH3x3)/v',
                 order = {'QED':1})

GC_100 = Coupling(name = 'GC_100',
                  value = '-((complex(0,1)*GL1x3*TH2x3)/v) + (GL1x3*TH3x3)/v',
                  order = {'QED':1})

GC_101 = Coupling(name = 'GC_101',
                  value = '-((complex(0,1)*GL2x1*TH2x3)/v) + (GL2x1*TH3x3)/v',
                  order = {'QED':1})

GC_102 = Coupling(name = 'GC_102',
                  value = '-((complex(0,1)*GL2x2*TH2x3)/v) + (GL2x2*TH3x3)/v',
                  order = {'QED':1})

GC_103 = Coupling(name = 'GC_103',
                  value = '-((complex(0,1)*GL2x3*TH2x3)/v) + (GL2x3*TH3x3)/v',
                  order = {'QED':1})

GC_104 = Coupling(name = 'GC_104',
                  value = '-((complex(0,1)*GL3x1*TH2x3)/v) + (GL3x1*TH3x3)/v',
                  order = {'QED':1})

GC_105 = Coupling(name = 'GC_105',
                  value = '-((complex(0,1)*GL3x2*TH2x3)/v) + (GL3x2*TH3x3)/v',
                  order = {'QED':1})

GC_106 = Coupling(name = 'GC_106',
                  value = '-((complex(0,1)*GL3x3*TH2x3)/v) + (GL3x3*TH3x3)/v',
                  order = {'QED':1})

GC_107 = Coupling(name = 'GC_107',
                  value = '-((complex(0,1)*GD1x1*cmath.sqrt(2))/v)',
                  order = {'QED':1})

GC_108 = Coupling(name = 'GC_108',
                  value = '-((complex(0,1)*GD1x2*cmath.sqrt(2))/v)',
                  order = {'QED':1})

GC_109 = Coupling(name = 'GC_109',
                  value = '-((complex(0,1)*GD1x3*cmath.sqrt(2))/v)',
                  order = {'QED':1})

GC_110 = Coupling(name = 'GC_110',
                  value = '-((complex(0,1)*GD2x1*cmath.sqrt(2))/v)',
                  order = {'QED':1})

GC_111 = Coupling(name = 'GC_111',
                  value = '-((complex(0,1)*GD2x2*cmath.sqrt(2))/v)',
                  order = {'QED':1})

GC_112 = Coupling(name = 'GC_112',
                  value = '-((complex(0,1)*GD2x3*cmath.sqrt(2))/v)',
                  order = {'QED':1})

GC_113 = Coupling(name = 'GC_113',
                  value = '-((complex(0,1)*GD3x1*cmath.sqrt(2))/v)',
                  order = {'QED':1})

GC_114 = Coupling(name = 'GC_114',
                  value = '-((complex(0,1)*GD3x2*cmath.sqrt(2))/v)',
                  order = {'QED':1})

GC_115 = Coupling(name = 'GC_115',
                  value = '-((complex(0,1)*GD3x3*cmath.sqrt(2))/v)',
                  order = {'QED':1})

GC_116 = Coupling(name = 'GC_116',
                  value = '-((complex(0,1)*GL1x1*cmath.sqrt(2))/v)',
                  order = {'QED':1})

GC_117 = Coupling(name = 'GC_117',
                  value = '-((complex(0,1)*GL1x2*cmath.sqrt(2))/v)',
                  order = {'QED':1})

GC_118 = Coupling(name = 'GC_118',
                  value = '-((complex(0,1)*GL1x3*cmath.sqrt(2))/v)',
                  order = {'QED':1})

GC_119 = Coupling(name = 'GC_119',
                  value = '-((complex(0,1)*GL2x1*cmath.sqrt(2))/v)',
                  order = {'QED':1})

GC_120 = Coupling(name = 'GC_120',
                  value = '-((complex(0,1)*GL2x2*cmath.sqrt(2))/v)',
                  order = {'QED':1})

GC_121 = Coupling(name = 'GC_121',
                  value = '-((complex(0,1)*GL2x3*cmath.sqrt(2))/v)',
                  order = {'QED':1})

GC_122 = Coupling(name = 'GC_122',
                  value = '-((complex(0,1)*GL3x1*cmath.sqrt(2))/v)',
                  order = {'QED':1})

GC_123 = Coupling(name = 'GC_123',
                  value = '-((complex(0,1)*GL3x2*cmath.sqrt(2))/v)',
                  order = {'QED':1})

GC_124 = Coupling(name = 'GC_124',
                  value = '-((complex(0,1)*GL3x3*cmath.sqrt(2))/v)',
                  order = {'QED':1})

GC_125 = Coupling(name = 'GC_125',
                  value = '(complex(0,1)*GU1x1*cmath.sqrt(2))/v',
                  order = {'QED':1})

GC_126 = Coupling(name = 'GC_126',
                  value = '(complex(0,1)*GU1x2*cmath.sqrt(2))/v',
                  order = {'QED':1})

GC_127 = Coupling(name = 'GC_127',
                  value = '(complex(0,1)*GU1x3*cmath.sqrt(2))/v',
                  order = {'QED':1})

GC_128 = Coupling(name = 'GC_128',
                  value = '(complex(0,1)*GU2x1*cmath.sqrt(2))/v',
                  order = {'QED':1})

GC_129 = Coupling(name = 'GC_129',
                  value = '(complex(0,1)*GU2x2*cmath.sqrt(2))/v',
                  order = {'QED':1})

GC_130 = Coupling(name = 'GC_130',
                  value = '(complex(0,1)*GU2x3*cmath.sqrt(2))/v',
                  order = {'QED':1})

GC_131 = Coupling(name = 'GC_131',
                  value = '(complex(0,1)*GU3x1*cmath.sqrt(2))/v',
                  order = {'QED':1})

GC_132 = Coupling(name = 'GC_132',
                  value = '(complex(0,1)*GU3x2*cmath.sqrt(2))/v',
                  order = {'QED':1})

GC_133 = Coupling(name = 'GC_133',
                  value = '(complex(0,1)*GU3x3*cmath.sqrt(2))/v',
                  order = {'QED':1})

GC_134 = Coupling(name = 'GC_134',
                  value = '(complex(0,1)*gw**2*TH1x1*v)/2.',
                  order = {'QED':1})

GC_135 = Coupling(name = 'GC_135',
                  value = '(complex(0,1)*gw**2*TH1x2*v)/2.',
                  order = {'QED':1})

GC_136 = Coupling(name = 'GC_136',
                  value = '(complex(0,1)*gw**2*TH1x3*v)/2.',
                  order = {'QED':1})

GC_137 = Coupling(name = 'GC_137',
                  value = '(cw**2*complex(0,1)*gw**2*TH1x1*v)/2. + cw*complex(0,1)*g1*gw*sw*TH1x1*v + (complex(0,1)*g1**2*sw**2*TH1x1*v)/2.',
                  order = {'QED':1})

GC_138 = Coupling(name = 'GC_138',
                  value = '-(cw**2*complex(0,1)*g1*gw*TH1x1*v)/2. - (cw*complex(0,1)*g1**2*sw*TH1x1*v)/2. + (cw*complex(0,1)*gw**2*sw*TH1x1*v)/2. + (complex(0,1)*g1*gw*sw**2*TH1x1*v)/2.',
                  order = {'QED':1})

GC_139 = Coupling(name = 'GC_139',
                  value = '(cw**2*complex(0,1)*g1**2*TH1x1*v)/2. - cw*complex(0,1)*g1*gw*sw*TH1x1*v + (complex(0,1)*gw**2*sw**2*TH1x1*v)/2.',
                  order = {'QED':1})

GC_140 = Coupling(name = 'GC_140',
                  value = '(cw**2*complex(0,1)*gw**2*TH1x2*v)/2. + cw*complex(0,1)*g1*gw*sw*TH1x2*v + (complex(0,1)*g1**2*sw**2*TH1x2*v)/2.',
                  order = {'QED':1})

GC_141 = Coupling(name = 'GC_141',
                  value = '-(cw**2*complex(0,1)*g1*gw*TH1x2*v)/2. - (cw*complex(0,1)*g1**2*sw*TH1x2*v)/2. + (cw*complex(0,1)*gw**2*sw*TH1x2*v)/2. + (complex(0,1)*g1*gw*sw**2*TH1x2*v)/2.',
                  order = {'QED':1})

GC_142 = Coupling(name = 'GC_142',
                  value = '(cw**2*complex(0,1)*g1**2*TH1x2*v)/2. - cw*complex(0,1)*g1*gw*sw*TH1x2*v + (complex(0,1)*gw**2*sw**2*TH1x2*v)/2.',
                  order = {'QED':1})

GC_143 = Coupling(name = 'GC_143',
                  value = '(cw**2*complex(0,1)*gw**2*TH1x3*v)/2. + cw*complex(0,1)*g1*gw*sw*TH1x3*v + (complex(0,1)*g1**2*sw**2*TH1x3*v)/2.',
                  order = {'QED':1})

GC_144 = Coupling(name = 'GC_144',
                  value = '-(cw**2*complex(0,1)*g1*gw*TH1x3*v)/2. - (cw*complex(0,1)*g1**2*sw*TH1x3*v)/2. + (cw*complex(0,1)*gw**2*sw*TH1x3*v)/2. + (complex(0,1)*g1*gw*sw**2*TH1x3*v)/2.',
                  order = {'QED':1})

GC_145 = Coupling(name = 'GC_145',
                  value = '(cw**2*complex(0,1)*g1**2*TH1x3*v)/2. - cw*complex(0,1)*g1*gw*sw*TH1x3*v + (complex(0,1)*gw**2*sw**2*TH1x3*v)/2.',
                  order = {'QED':1})

GC_146 = Coupling(name = 'GC_146',
                  value = '-((complex(0,1)*TH1x1*yukl1)/v)',
                  order = {'QED':2})

GC_147 = Coupling(name = 'GC_147',
                  value = '-((complex(0,1)*TH1x2*yukl1)/v)',
                  order = {'QED':2})

GC_148 = Coupling(name = 'GC_148',
                  value = '-((complex(0,1)*TH1x3*yukl1)/v)',
                  order = {'QED':2})

GC_149 = Coupling(name = 'GC_149',
                  value = '-((complex(0,1)*TH1x1*yukl2)/v)',
                  order = {'QED':2})

GC_150 = Coupling(name = 'GC_150',
                  value = '-((complex(0,1)*TH1x2*yukl2)/v)',
                  order = {'QED':2})

GC_151 = Coupling(name = 'GC_151',
                  value = '-((complex(0,1)*TH1x3*yukl2)/v)',
                  order = {'QED':2})

GC_152 = Coupling(name = 'GC_152',
                  value = '-((complex(0,1)*TH1x1*yukl3)/v)',
                  order = {'QED':2})

GC_153 = Coupling(name = 'GC_153',
                  value = '-((complex(0,1)*TH1x2*yukl3)/v)',
                  order = {'QED':2})

GC_154 = Coupling(name = 'GC_154',
                  value = '-((complex(0,1)*TH1x3*yukl3)/v)',
                  order = {'QED':2})

GC_155 = Coupling(name = 'GC_155',
                  value = '-(complex(0,1)*zpa)',
                  order = {'S1VV':2})

GC_156 = Coupling(name = 'GC_156',
                  value = 'complex(0,1)*zpv',
                  order = {'S1VV':2})

GC_157 = Coupling(name = 'GC_157',
                  value = '(ee*complex(0,1)*complexconjugate(CKM1x1))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_158 = Coupling(name = 'GC_158',
                  value = '(ee*complex(0,1)*complexconjugate(CKM1x2))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_159 = Coupling(name = 'GC_159',
                  value = '(ee*complex(0,1)*complexconjugate(CKM2x1))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_160 = Coupling(name = 'GC_160',
                  value = '(ee*complex(0,1)*complexconjugate(CKM2x2))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_161 = Coupling(name = 'GC_161',
                  value = '-((complex(0,1)*complexconjugate(GD1x1)*cmath.sqrt(2))/v)',
                  order = {'QED':1})

GC_162 = Coupling(name = 'GC_162',
                  value = '-((complex(0,1)*complexconjugate(GD1x2)*cmath.sqrt(2))/v)',
                  order = {'QED':1})

GC_163 = Coupling(name = 'GC_163',
                  value = '-((complex(0,1)*complexconjugate(GD1x3)*cmath.sqrt(2))/v)',
                  order = {'QED':1})

GC_164 = Coupling(name = 'GC_164',
                  value = '-((complex(0,1)*complexconjugate(GD2x1)*cmath.sqrt(2))/v)',
                  order = {'QED':1})

GC_165 = Coupling(name = 'GC_165',
                  value = '-((complex(0,1)*complexconjugate(GD2x2)*cmath.sqrt(2))/v)',
                  order = {'QED':1})

GC_166 = Coupling(name = 'GC_166',
                  value = '-((complex(0,1)*complexconjugate(GD2x3)*cmath.sqrt(2))/v)',
                  order = {'QED':1})

GC_167 = Coupling(name = 'GC_167',
                  value = '-((complex(0,1)*complexconjugate(GD3x1)*cmath.sqrt(2))/v)',
                  order = {'QED':1})

GC_168 = Coupling(name = 'GC_168',
                  value = '-((complex(0,1)*complexconjugate(GD3x2)*cmath.sqrt(2))/v)',
                  order = {'QED':1})

GC_169 = Coupling(name = 'GC_169',
                  value = '-((complex(0,1)*complexconjugate(GD3x3)*cmath.sqrt(2))/v)',
                  order = {'QED':1})

GC_170 = Coupling(name = 'GC_170',
                  value = '-((complex(0,1)*complexconjugate(GL1x1)*cmath.sqrt(2))/v)',
                  order = {'QED':1})

GC_171 = Coupling(name = 'GC_171',
                  value = '-((complex(0,1)*TH2x1*complexconjugate(GL1x1))/v) - (TH3x1*complexconjugate(GL1x1))/v',
                  order = {'QED':1})

GC_172 = Coupling(name = 'GC_172',
                  value = '-((complex(0,1)*TH2x2*complexconjugate(GL1x1))/v) - (TH3x2*complexconjugate(GL1x1))/v',
                  order = {'QED':1})

GC_173 = Coupling(name = 'GC_173',
                  value = '-((complex(0,1)*TH2x3*complexconjugate(GL1x1))/v) - (TH3x3*complexconjugate(GL1x1))/v',
                  order = {'QED':1})

GC_174 = Coupling(name = 'GC_174',
                  value = '-((complex(0,1)*complexconjugate(GL1x2)*cmath.sqrt(2))/v)',
                  order = {'QED':1})

GC_175 = Coupling(name = 'GC_175',
                  value = '-((complex(0,1)*TH2x1*complexconjugate(GL1x2))/v) - (TH3x1*complexconjugate(GL1x2))/v',
                  order = {'QED':1})

GC_176 = Coupling(name = 'GC_176',
                  value = '-((complex(0,1)*TH2x2*complexconjugate(GL1x2))/v) - (TH3x2*complexconjugate(GL1x2))/v',
                  order = {'QED':1})

GC_177 = Coupling(name = 'GC_177',
                  value = '-((complex(0,1)*TH2x3*complexconjugate(GL1x2))/v) - (TH3x3*complexconjugate(GL1x2))/v',
                  order = {'QED':1})

GC_178 = Coupling(name = 'GC_178',
                  value = '-((complex(0,1)*complexconjugate(GL1x3)*cmath.sqrt(2))/v)',
                  order = {'QED':1})

GC_179 = Coupling(name = 'GC_179',
                  value = '-((complex(0,1)*TH2x1*complexconjugate(GL1x3))/v) - (TH3x1*complexconjugate(GL1x3))/v',
                  order = {'QED':1})

GC_180 = Coupling(name = 'GC_180',
                  value = '-((complex(0,1)*TH2x2*complexconjugate(GL1x3))/v) - (TH3x2*complexconjugate(GL1x3))/v',
                  order = {'QED':1})

GC_181 = Coupling(name = 'GC_181',
                  value = '-((complex(0,1)*TH2x3*complexconjugate(GL1x3))/v) - (TH3x3*complexconjugate(GL1x3))/v',
                  order = {'QED':1})

GC_182 = Coupling(name = 'GC_182',
                  value = '-((complex(0,1)*complexconjugate(GL2x1)*cmath.sqrt(2))/v)',
                  order = {'QED':1})

GC_183 = Coupling(name = 'GC_183',
                  value = '-((complex(0,1)*TH2x1*complexconjugate(GL2x1))/v) - (TH3x1*complexconjugate(GL2x1))/v',
                  order = {'QED':1})

GC_184 = Coupling(name = 'GC_184',
                  value = '-((complex(0,1)*TH2x2*complexconjugate(GL2x1))/v) - (TH3x2*complexconjugate(GL2x1))/v',
                  order = {'QED':1})

GC_185 = Coupling(name = 'GC_185',
                  value = '-((complex(0,1)*TH2x3*complexconjugate(GL2x1))/v) - (TH3x3*complexconjugate(GL2x1))/v',
                  order = {'QED':1})

GC_186 = Coupling(name = 'GC_186',
                  value = '-((complex(0,1)*complexconjugate(GL2x2)*cmath.sqrt(2))/v)',
                  order = {'QED':1})

GC_187 = Coupling(name = 'GC_187',
                  value = '-((complex(0,1)*TH2x1*complexconjugate(GL2x2))/v) - (TH3x1*complexconjugate(GL2x2))/v',
                  order = {'QED':1})

GC_188 = Coupling(name = 'GC_188',
                  value = '-((complex(0,1)*TH2x2*complexconjugate(GL2x2))/v) - (TH3x2*complexconjugate(GL2x2))/v',
                  order = {'QED':1})

GC_189 = Coupling(name = 'GC_189',
                  value = '-((complex(0,1)*TH2x3*complexconjugate(GL2x2))/v) - (TH3x3*complexconjugate(GL2x2))/v',
                  order = {'QED':1})

GC_190 = Coupling(name = 'GC_190',
                  value = '-((complex(0,1)*complexconjugate(GL2x3)*cmath.sqrt(2))/v)',
                  order = {'QED':1})

GC_191 = Coupling(name = 'GC_191',
                  value = '-((complex(0,1)*TH2x1*complexconjugate(GL2x3))/v) - (TH3x1*complexconjugate(GL2x3))/v',
                  order = {'QED':1})

GC_192 = Coupling(name = 'GC_192',
                  value = '-((complex(0,1)*TH2x2*complexconjugate(GL2x3))/v) - (TH3x2*complexconjugate(GL2x3))/v',
                  order = {'QED':1})

GC_193 = Coupling(name = 'GC_193',
                  value = '-((complex(0,1)*TH2x3*complexconjugate(GL2x3))/v) - (TH3x3*complexconjugate(GL2x3))/v',
                  order = {'QED':1})

GC_194 = Coupling(name = 'GC_194',
                  value = '-((complex(0,1)*complexconjugate(GL3x1)*cmath.sqrt(2))/v)',
                  order = {'QED':1})

GC_195 = Coupling(name = 'GC_195',
                  value = '-((complex(0,1)*TH2x1*complexconjugate(GL3x1))/v) - (TH3x1*complexconjugate(GL3x1))/v',
                  order = {'QED':1})

GC_196 = Coupling(name = 'GC_196',
                  value = '-((complex(0,1)*TH2x2*complexconjugate(GL3x1))/v) - (TH3x2*complexconjugate(GL3x1))/v',
                  order = {'QED':1})

GC_197 = Coupling(name = 'GC_197',
                  value = '-((complex(0,1)*TH2x3*complexconjugate(GL3x1))/v) - (TH3x3*complexconjugate(GL3x1))/v',
                  order = {'QED':1})

GC_198 = Coupling(name = 'GC_198',
                  value = '-((complex(0,1)*complexconjugate(GL3x2)*cmath.sqrt(2))/v)',
                  order = {'QED':1})

GC_199 = Coupling(name = 'GC_199',
                  value = '-((complex(0,1)*TH2x1*complexconjugate(GL3x2))/v) - (TH3x1*complexconjugate(GL3x2))/v',
                  order = {'QED':1})

GC_200 = Coupling(name = 'GC_200',
                  value = '-((complex(0,1)*TH2x2*complexconjugate(GL3x2))/v) - (TH3x2*complexconjugate(GL3x2))/v',
                  order = {'QED':1})

GC_201 = Coupling(name = 'GC_201',
                  value = '-((complex(0,1)*TH2x3*complexconjugate(GL3x2))/v) - (TH3x3*complexconjugate(GL3x2))/v',
                  order = {'QED':1})

GC_202 = Coupling(name = 'GC_202',
                  value = '-((complex(0,1)*complexconjugate(GL3x3)*cmath.sqrt(2))/v)',
                  order = {'QED':1})

GC_203 = Coupling(name = 'GC_203',
                  value = '-((complex(0,1)*TH2x1*complexconjugate(GL3x3))/v) - (TH3x1*complexconjugate(GL3x3))/v',
                  order = {'QED':1})

GC_204 = Coupling(name = 'GC_204',
                  value = '-((complex(0,1)*TH2x2*complexconjugate(GL3x3))/v) - (TH3x2*complexconjugate(GL3x3))/v',
                  order = {'QED':1})

GC_205 = Coupling(name = 'GC_205',
                  value = '-((complex(0,1)*TH2x3*complexconjugate(GL3x3))/v) - (TH3x3*complexconjugate(GL3x3))/v',
                  order = {'QED':1})

GC_206 = Coupling(name = 'GC_206',
                  value = '(complex(0,1)*complexconjugate(GU1x1)*cmath.sqrt(2))/v',
                  order = {'QED':1})

GC_207 = Coupling(name = 'GC_207',
                  value = '(complex(0,1)*complexconjugate(GU1x2)*cmath.sqrt(2))/v',
                  order = {'QED':1})

GC_208 = Coupling(name = 'GC_208',
                  value = '(complex(0,1)*complexconjugate(GU1x3)*cmath.sqrt(2))/v',
                  order = {'QED':1})

GC_209 = Coupling(name = 'GC_209',
                  value = '(complex(0,1)*complexconjugate(GU2x1)*cmath.sqrt(2))/v',
                  order = {'QED':1})

GC_210 = Coupling(name = 'GC_210',
                  value = '(complex(0,1)*complexconjugate(GU2x2)*cmath.sqrt(2))/v',
                  order = {'QED':1})

GC_211 = Coupling(name = 'GC_211',
                  value = '(complex(0,1)*complexconjugate(GU2x3)*cmath.sqrt(2))/v',
                  order = {'QED':1})

GC_212 = Coupling(name = 'GC_212',
                  value = '(complex(0,1)*complexconjugate(GU3x1)*cmath.sqrt(2))/v',
                  order = {'QED':1})

GC_213 = Coupling(name = 'GC_213',
                  value = '(complex(0,1)*complexconjugate(GU3x2)*cmath.sqrt(2))/v',
                  order = {'QED':1})

GC_214 = Coupling(name = 'GC_214',
                  value = '(complex(0,1)*complexconjugate(GU3x3)*cmath.sqrt(2))/v',
                  order = {'QED':1})

GC_215 = Coupling(name = 'GC_215',
                  value = '-(complex(0,1)*l3*TH1x1**2) - complex(0,1)*l7*TH1x1*TH2x1 - 2*complex(0,1)*l2*TH2x1**2 + l7*TH1x1*TH3x1 - 2*complex(0,1)*l2*TH3x1**2 - complex(0,1)*TH1x1*TH2x1*complexconjugate(l7) - TH1x1*TH3x1*complexconjugate(l7)',
                  order = {'QED':2})

GC_216 = Coupling(name = 'GC_216',
                  value = '-6*complex(0,1)*l1*TH1x1**4 - 6*complex(0,1)*l6*TH1x1**3*TH2x1 - 6*complex(0,1)*l3*TH1x1**2*TH2x1**2 - 6*complex(0,1)*l4*TH1x1**2*TH2x1**2 - 12*complex(0,1)*l5*TH1x1**2*TH2x1**2 - 6*complex(0,1)*l7*TH1x1*TH2x1**3 - 6*complex(0,1)*l2*TH2x1**4 + 6*l6*TH1x1**3*TH3x1 + 6*l7*TH1x1*TH2x1**2*TH3x1 - 6*complex(0,1)*l3*TH1x1**2*TH3x1**2 - 6*complex(0,1)*l4*TH1x1**2*TH3x1**2 + 12*complex(0,1)*l5*TH1x1**2*TH3x1**2 - 6*complex(0,1)*l7*TH1x1*TH2x1*TH3x1**2 - 12*complex(0,1)*l2*TH2x1**2*TH3x1**2 + 6*l7*TH1x1*TH3x1**3 - 6*complex(0,1)*l2*TH3x1**4 - 6*complex(0,1)*TH1x1**3*TH2x1*complexconjugate(l6) - 6*TH1x1**3*TH3x1*complexconjugate(l6) - 6*complex(0,1)*TH1x1*TH2x1**3*complexconjugate(l7) - 6*TH1x1*TH2x1**2*TH3x1*complexconjugate(l7) - 6*complex(0,1)*TH1x1*TH2x1*TH3x1**2*complexconjugate(l7) - 6*TH1x1*TH3x1**3*complexconjugate(l7)',
                  order = {'QED':2})

GC_217 = Coupling(name = 'GC_217',
                  value = '-(complex(0,1)*l3*TH1x1*TH1x2) - (complex(0,1)*l7*TH1x2*TH2x1)/2. - (complex(0,1)*l7*TH1x1*TH2x2)/2. - 2*complex(0,1)*l2*TH2x1*TH2x2 + (l7*TH1x2*TH3x1)/2. + (l7*TH1x1*TH3x2)/2. - 2*complex(0,1)*l2*TH3x1*TH3x2 - (complex(0,1)*TH1x2*TH2x1*complexconjugate(l7))/2. - (complex(0,1)*TH1x1*TH2x2*complexconjugate(l7))/2. - (TH1x2*TH3x1*complexconjugate(l7))/2. - (TH1x1*TH3x2*complexconjugate(l7))/2.',
                  order = {'QED':2})

GC_218 = Coupling(name = 'GC_218',
                  value = '-(complex(0,1)*l3*TH1x2**2) - complex(0,1)*l7*TH1x2*TH2x2 - 2*complex(0,1)*l2*TH2x2**2 + l7*TH1x2*TH3x2 - 2*complex(0,1)*l2*TH3x2**2 - complex(0,1)*TH1x2*TH2x2*complexconjugate(l7) - TH1x2*TH3x2*complexconjugate(l7)',
                  order = {'QED':2})

GC_219 = Coupling(name = 'GC_219',
                  value = '-6*complex(0,1)*l1*TH1x1**3*TH1x2 - (9*complex(0,1)*l6*TH1x1**2*TH1x2*TH2x1)/2. - 3*complex(0,1)*l3*TH1x1*TH1x2*TH2x1**2 - 3*complex(0,1)*l4*TH1x1*TH1x2*TH2x1**2 - 6*complex(0,1)*l5*TH1x1*TH1x2*TH2x1**2 - (3*complex(0,1)*l7*TH1x2*TH2x1**3)/2. - (3*complex(0,1)*l6*TH1x1**3*TH2x2)/2. - 3*complex(0,1)*l3*TH1x1**2*TH2x1*TH2x2 - 3*complex(0,1)*l4*TH1x1**2*TH2x1*TH2x2 - 6*complex(0,1)*l5*TH1x1**2*TH2x1*TH2x2 - (9*complex(0,1)*l7*TH1x1*TH2x1**2*TH2x2)/2. - 6*complex(0,1)*l2*TH2x1**3*TH2x2 + (9*l6*TH1x1**2*TH1x2*TH3x1)/2. + (3*l7*TH1x2*TH2x1**2*TH3x1)/2. + 3*l7*TH1x1*TH2x1*TH2x2*TH3x1 - 3*complex(0,1)*l3*TH1x1*TH1x2*TH3x1**2 - 3*complex(0,1)*l4*TH1x1*TH1x2*TH3x1**2 + 6*complex(0,1)*l5*TH1x1*TH1x2*TH3x1**2 - (3*complex(0,1)*l7*TH1x2*TH2x1*TH3x1**2)/2. - (3*complex(0,1)*l7*TH1x1*TH2x2*TH3x1**2)/2. - 6*complex(0,1)*l2*TH2x1*TH2x2*TH3x1**2 + (3*l7*TH1x2*TH3x1**3)/2. + (3*l6*TH1x1**3*TH3x2)/2. + (3*l7*TH1x1*TH2x1**2*TH3x2)/2. - 3*complex(0,1)*l3*TH1x1**2*TH3x1*TH3x2 - 3*complex(0,1)*l4*TH1x1**2*TH3x1*TH3x2 + 6*complex(0,1)*l5*TH1x1**2*TH3x1*TH3x2 - 3*complex(0,1)*l7*TH1x1*TH2x1*TH3x1*TH3x2 - 6*complex(0,1)*l2*TH2x1**2*TH3x1*TH3x2 + (9*l7*TH1x1*TH3x1**2*TH3x2)/2. - 6*complex(0,1)*l2*TH3x1**3*TH3x2 - (9*complex(0,1)*TH1x1**2*TH1x2*TH2x1*complexconjugate(l6))/2. - (3*complex(0,1)*TH1x1**3*TH2x2*complexconjugate(l6))/2. - (9*TH1x1**2*TH1x2*TH3x1*complexconjugate(l6))/2. - (3*TH1x1**3*TH3x2*complexconjugate(l6))/2. - (3*complex(0,1)*TH1x2*TH2x1**3*complexconjugate(l7))/2. - (9*complex(0,1)*TH1x1*TH2x1**2*TH2x2*complexconjugate(l7))/2. - (3*TH1x2*TH2x1**2*TH3x1*complexconjugate(l7))/2. - 3*TH1x1*TH2x1*TH2x2*TH3x1*complexconjugate(l7) - (3*complex(0,1)*TH1x2*TH2x1*TH3x1**2*complexconjugate(l7))/2. - (3*complex(0,1)*TH1x1*TH2x2*TH3x1**2*complexconjugate(l7))/2. - (3*TH1x2*TH3x1**3*complexconjugate(l7))/2. - (3*TH1x1*TH2x1**2*TH3x2*complexconjugate(l7))/2. - 3*complex(0,1)*TH1x1*TH2x1*TH3x1*TH3x2*complexconjugate(l7) - (9*TH1x1*TH3x1**2*TH3x2*complexconjugate(l7))/2.',
                  order = {'QED':2})

GC_220 = Coupling(name = 'GC_220',
                  value = '-6*complex(0,1)*l1*TH1x1**2*TH1x2**2 - 3*complex(0,1)*l6*TH1x1*TH1x2**2*TH2x1 - complex(0,1)*l3*TH1x2**2*TH2x1**2 - complex(0,1)*l4*TH1x2**2*TH2x1**2 - 2*complex(0,1)*l5*TH1x2**2*TH2x1**2 - 3*complex(0,1)*l6*TH1x1**2*TH1x2*TH2x2 - 4*complex(0,1)*l3*TH1x1*TH1x2*TH2x1*TH2x2 - 4*complex(0,1)*l4*TH1x1*TH1x2*TH2x1*TH2x2 - 8*complex(0,1)*l5*TH1x1*TH1x2*TH2x1*TH2x2 - 3*complex(0,1)*l7*TH1x2*TH2x1**2*TH2x2 - complex(0,1)*l3*TH1x1**2*TH2x2**2 - complex(0,1)*l4*TH1x1**2*TH2x2**2 - 2*complex(0,1)*l5*TH1x1**2*TH2x2**2 - 3*complex(0,1)*l7*TH1x1*TH2x1*TH2x2**2 - 6*complex(0,1)*l2*TH2x1**2*TH2x2**2 + 3*l6*TH1x1*TH1x2**2*TH3x1 + 2*l7*TH1x2*TH2x1*TH2x2*TH3x1 + l7*TH1x1*TH2x2**2*TH3x1 - complex(0,1)*l3*TH1x2**2*TH3x1**2 - complex(0,1)*l4*TH1x2**2*TH3x1**2 + 2*complex(0,1)*l5*TH1x2**2*TH3x1**2 - complex(0,1)*l7*TH1x2*TH2x2*TH3x1**2 - 2*complex(0,1)*l2*TH2x2**2*TH3x1**2 + 3*l6*TH1x1**2*TH1x2*TH3x2 + l7*TH1x2*TH2x1**2*TH3x2 + 2*l7*TH1x1*TH2x1*TH2x2*TH3x2 - 4*complex(0,1)*l3*TH1x1*TH1x2*TH3x1*TH3x2 - 4*complex(0,1)*l4*TH1x1*TH1x2*TH3x1*TH3x2 + 8*complex(0,1)*l5*TH1x1*TH1x2*TH3x1*TH3x2 - 2*complex(0,1)*l7*TH1x2*TH2x1*TH3x1*TH3x2 - 2*complex(0,1)*l7*TH1x1*TH2x2*TH3x1*TH3x2 - 8*complex(0,1)*l2*TH2x1*TH2x2*TH3x1*TH3x2 + 3*l7*TH1x2*TH3x1**2*TH3x2 - complex(0,1)*l3*TH1x1**2*TH3x2**2 - complex(0,1)*l4*TH1x1**2*TH3x2**2 + 2*complex(0,1)*l5*TH1x1**2*TH3x2**2 - complex(0,1)*l7*TH1x1*TH2x1*TH3x2**2 - 2*complex(0,1)*l2*TH2x1**2*TH3x2**2 + 3*l7*TH1x1*TH3x1*TH3x2**2 - 6*complex(0,1)*l2*TH3x1**2*TH3x2**2 - 3*complex(0,1)*TH1x1*TH1x2**2*TH2x1*complexconjugate(l6) - 3*complex(0,1)*TH1x1**2*TH1x2*TH2x2*complexconjugate(l6) - 3*TH1x1*TH1x2**2*TH3x1*complexconjugate(l6) - 3*TH1x1**2*TH1x2*TH3x2*complexconjugate(l6) - 3*complex(0,1)*TH1x2*TH2x1**2*TH2x2*complexconjugate(l7) - 3*complex(0,1)*TH1x1*TH2x1*TH2x2**2*complexconjugate(l7) - 2*TH1x2*TH2x1*TH2x2*TH3x1*complexconjugate(l7) - TH1x1*TH2x2**2*TH3x1*complexconjugate(l7) - complex(0,1)*TH1x2*TH2x2*TH3x1**2*complexconjugate(l7) - TH1x2*TH2x1**2*TH3x2*complexconjugate(l7) - 2*TH1x1*TH2x1*TH2x2*TH3x2*complexconjugate(l7) - 2*complex(0,1)*TH1x2*TH2x1*TH3x1*TH3x2*complexconjugate(l7) - 2*complex(0,1)*TH1x1*TH2x2*TH3x1*TH3x2*complexconjugate(l7) - 3*TH1x2*TH3x1**2*TH3x2*complexconjugate(l7) - complex(0,1)*TH1x1*TH2x1*TH3x2**2*complexconjugate(l7) - 3*TH1x1*TH3x1*TH3x2**2*complexconjugate(l7)',
                  order = {'QED':2})

GC_221 = Coupling(name = 'GC_221',
                  value = '-6*complex(0,1)*l1*TH1x1*TH1x2**3 - (3*complex(0,1)*l6*TH1x2**3*TH2x1)/2. - (9*complex(0,1)*l6*TH1x1*TH1x2**2*TH2x2)/2. - 3*complex(0,1)*l3*TH1x2**2*TH2x1*TH2x2 - 3*complex(0,1)*l4*TH1x2**2*TH2x1*TH2x2 - 6*complex(0,1)*l5*TH1x2**2*TH2x1*TH2x2 - 3*complex(0,1)*l3*TH1x1*TH1x2*TH2x2**2 - 3*complex(0,1)*l4*TH1x1*TH1x2*TH2x2**2 - 6*complex(0,1)*l5*TH1x1*TH1x2*TH2x2**2 - (9*complex(0,1)*l7*TH1x2*TH2x1*TH2x2**2)/2. - (3*complex(0,1)*l7*TH1x1*TH2x2**3)/2. - 6*complex(0,1)*l2*TH2x1*TH2x2**3 + (3*l6*TH1x2**3*TH3x1)/2. + (3*l7*TH1x2*TH2x2**2*TH3x1)/2. + (9*l6*TH1x1*TH1x2**2*TH3x2)/2. + 3*l7*TH1x2*TH2x1*TH2x2*TH3x2 + (3*l7*TH1x1*TH2x2**2*TH3x2)/2. - 3*complex(0,1)*l3*TH1x2**2*TH3x1*TH3x2 - 3*complex(0,1)*l4*TH1x2**2*TH3x1*TH3x2 + 6*complex(0,1)*l5*TH1x2**2*TH3x1*TH3x2 - 3*complex(0,1)*l7*TH1x2*TH2x2*TH3x1*TH3x2 - 6*complex(0,1)*l2*TH2x2**2*TH3x1*TH3x2 - 3*complex(0,1)*l3*TH1x1*TH1x2*TH3x2**2 - 3*complex(0,1)*l4*TH1x1*TH1x2*TH3x2**2 + 6*complex(0,1)*l5*TH1x1*TH1x2*TH3x2**2 - (3*complex(0,1)*l7*TH1x2*TH2x1*TH3x2**2)/2. - (3*complex(0,1)*l7*TH1x1*TH2x2*TH3x2**2)/2. - 6*complex(0,1)*l2*TH2x1*TH2x2*TH3x2**2 + (9*l7*TH1x2*TH3x1*TH3x2**2)/2. + (3*l7*TH1x1*TH3x2**3)/2. - 6*complex(0,1)*l2*TH3x1*TH3x2**3 - (3*complex(0,1)*TH1x2**3*TH2x1*complexconjugate(l6))/2. - (9*complex(0,1)*TH1x1*TH1x2**2*TH2x2*complexconjugate(l6))/2. - (3*TH1x2**3*TH3x1*complexconjugate(l6))/2. - (9*TH1x1*TH1x2**2*TH3x2*complexconjugate(l6))/2. - (9*complex(0,1)*TH1x2*TH2x1*TH2x2**2*complexconjugate(l7))/2. - (3*complex(0,1)*TH1x1*TH2x2**3*complexconjugate(l7))/2. - (3*TH1x2*TH2x2**2*TH3x1*complexconjugate(l7))/2. - 3*TH1x2*TH2x1*TH2x2*TH3x2*complexconjugate(l7) - (3*TH1x1*TH2x2**2*TH3x2*complexconjugate(l7))/2. - 3*complex(0,1)*TH1x2*TH2x2*TH3x1*TH3x2*complexconjugate(l7) - (3*complex(0,1)*TH1x2*TH2x1*TH3x2**2*complexconjugate(l7))/2. - (3*complex(0,1)*TH1x1*TH2x2*TH3x2**2*complexconjugate(l7))/2. - (9*TH1x2*TH3x1*TH3x2**2*complexconjugate(l7))/2. - (3*TH1x1*TH3x2**3*complexconjugate(l7))/2.',
                  order = {'QED':2})

GC_222 = Coupling(name = 'GC_222',
                  value = '-6*complex(0,1)*l1*TH1x2**4 - 6*complex(0,1)*l6*TH1x2**3*TH2x2 - 6*complex(0,1)*l3*TH1x2**2*TH2x2**2 - 6*complex(0,1)*l4*TH1x2**2*TH2x2**2 - 12*complex(0,1)*l5*TH1x2**2*TH2x2**2 - 6*complex(0,1)*l7*TH1x2*TH2x2**3 - 6*complex(0,1)*l2*TH2x2**4 + 6*l6*TH1x2**3*TH3x2 + 6*l7*TH1x2*TH2x2**2*TH3x2 - 6*complex(0,1)*l3*TH1x2**2*TH3x2**2 - 6*complex(0,1)*l4*TH1x2**2*TH3x2**2 + 12*complex(0,1)*l5*TH1x2**2*TH3x2**2 - 6*complex(0,1)*l7*TH1x2*TH2x2*TH3x2**2 - 12*complex(0,1)*l2*TH2x2**2*TH3x2**2 + 6*l7*TH1x2*TH3x2**3 - 6*complex(0,1)*l2*TH3x2**4 - 6*complex(0,1)*TH1x2**3*TH2x2*complexconjugate(l6) - 6*TH1x2**3*TH3x2*complexconjugate(l6) - 6*complex(0,1)*TH1x2*TH2x2**3*complexconjugate(l7) - 6*TH1x2*TH2x2**2*TH3x2*complexconjugate(l7) - 6*complex(0,1)*TH1x2*TH2x2*TH3x2**2*complexconjugate(l7) - 6*TH1x2*TH3x2**3*complexconjugate(l7)',
                  order = {'QED':2})

GC_223 = Coupling(name = 'GC_223',
                  value = '-(complex(0,1)*l3*TH1x1*TH1x3) - (complex(0,1)*l7*TH1x3*TH2x1)/2. - (complex(0,1)*l7*TH1x1*TH2x3)/2. - 2*complex(0,1)*l2*TH2x1*TH2x3 + (l7*TH1x3*TH3x1)/2. + (l7*TH1x1*TH3x3)/2. - 2*complex(0,1)*l2*TH3x1*TH3x3 - (complex(0,1)*TH1x3*TH2x1*complexconjugate(l7))/2. - (complex(0,1)*TH1x1*TH2x3*complexconjugate(l7))/2. - (TH1x3*TH3x1*complexconjugate(l7))/2. - (TH1x1*TH3x3*complexconjugate(l7))/2.',
                  order = {'QED':2})

GC_224 = Coupling(name = 'GC_224',
                  value = '-(complex(0,1)*l3*TH1x2*TH1x3) - (complex(0,1)*l7*TH1x3*TH2x2)/2. - (complex(0,1)*l7*TH1x2*TH2x3)/2. - 2*complex(0,1)*l2*TH2x2*TH2x3 + (l7*TH1x3*TH3x2)/2. + (l7*TH1x2*TH3x3)/2. - 2*complex(0,1)*l2*TH3x2*TH3x3 - (complex(0,1)*TH1x3*TH2x2*complexconjugate(l7))/2. - (complex(0,1)*TH1x2*TH2x3*complexconjugate(l7))/2. - (TH1x3*TH3x2*complexconjugate(l7))/2. - (TH1x2*TH3x3*complexconjugate(l7))/2.',
                  order = {'QED':2})

GC_225 = Coupling(name = 'GC_225',
                  value = '-(complex(0,1)*l3*TH1x3**2) - complex(0,1)*l7*TH1x3*TH2x3 - 2*complex(0,1)*l2*TH2x3**2 + l7*TH1x3*TH3x3 - 2*complex(0,1)*l2*TH3x3**2 - complex(0,1)*TH1x3*TH2x3*complexconjugate(l7) - TH1x3*TH3x3*complexconjugate(l7)',
                  order = {'QED':2})

GC_226 = Coupling(name = 'GC_226',
                  value = '-6*complex(0,1)*l1*TH1x1**3*TH1x3 - (9*complex(0,1)*l6*TH1x1**2*TH1x3*TH2x1)/2. - 3*complex(0,1)*l3*TH1x1*TH1x3*TH2x1**2 - 3*complex(0,1)*l4*TH1x1*TH1x3*TH2x1**2 - 6*complex(0,1)*l5*TH1x1*TH1x3*TH2x1**2 - (3*complex(0,1)*l7*TH1x3*TH2x1**3)/2. - (3*complex(0,1)*l6*TH1x1**3*TH2x3)/2. - 3*complex(0,1)*l3*TH1x1**2*TH2x1*TH2x3 - 3*complex(0,1)*l4*TH1x1**2*TH2x1*TH2x3 - 6*complex(0,1)*l5*TH1x1**2*TH2x1*TH2x3 - (9*complex(0,1)*l7*TH1x1*TH2x1**2*TH2x3)/2. - 6*complex(0,1)*l2*TH2x1**3*TH2x3 + (9*l6*TH1x1**2*TH1x3*TH3x1)/2. + (3*l7*TH1x3*TH2x1**2*TH3x1)/2. + 3*l7*TH1x1*TH2x1*TH2x3*TH3x1 - 3*complex(0,1)*l3*TH1x1*TH1x3*TH3x1**2 - 3*complex(0,1)*l4*TH1x1*TH1x3*TH3x1**2 + 6*complex(0,1)*l5*TH1x1*TH1x3*TH3x1**2 - (3*complex(0,1)*l7*TH1x3*TH2x1*TH3x1**2)/2. - (3*complex(0,1)*l7*TH1x1*TH2x3*TH3x1**2)/2. - 6*complex(0,1)*l2*TH2x1*TH2x3*TH3x1**2 + (3*l7*TH1x3*TH3x1**3)/2. + (3*l6*TH1x1**3*TH3x3)/2. + (3*l7*TH1x1*TH2x1**2*TH3x3)/2. - 3*complex(0,1)*l3*TH1x1**2*TH3x1*TH3x3 - 3*complex(0,1)*l4*TH1x1**2*TH3x1*TH3x3 + 6*complex(0,1)*l5*TH1x1**2*TH3x1*TH3x3 - 3*complex(0,1)*l7*TH1x1*TH2x1*TH3x1*TH3x3 - 6*complex(0,1)*l2*TH2x1**2*TH3x1*TH3x3 + (9*l7*TH1x1*TH3x1**2*TH3x3)/2. - 6*complex(0,1)*l2*TH3x1**3*TH3x3 - (9*complex(0,1)*TH1x1**2*TH1x3*TH2x1*complexconjugate(l6))/2. - (3*complex(0,1)*TH1x1**3*TH2x3*complexconjugate(l6))/2. - (9*TH1x1**2*TH1x3*TH3x1*complexconjugate(l6))/2. - (3*TH1x1**3*TH3x3*complexconjugate(l6))/2. - (3*complex(0,1)*TH1x3*TH2x1**3*complexconjugate(l7))/2. - (9*complex(0,1)*TH1x1*TH2x1**2*TH2x3*complexconjugate(l7))/2. - (3*TH1x3*TH2x1**2*TH3x1*complexconjugate(l7))/2. - 3*TH1x1*TH2x1*TH2x3*TH3x1*complexconjugate(l7) - (3*complex(0,1)*TH1x3*TH2x1*TH3x1**2*complexconjugate(l7))/2. - (3*complex(0,1)*TH1x1*TH2x3*TH3x1**2*complexconjugate(l7))/2. - (3*TH1x3*TH3x1**3*complexconjugate(l7))/2. - (3*TH1x1*TH2x1**2*TH3x3*complexconjugate(l7))/2. - 3*complex(0,1)*TH1x1*TH2x1*TH3x1*TH3x3*complexconjugate(l7) - (9*TH1x1*TH3x1**2*TH3x3*complexconjugate(l7))/2.',
                  order = {'QED':2})

GC_227 = Coupling(name = 'GC_227',
                  value = '-6*complex(0,1)*l1*TH1x1**2*TH1x2*TH1x3 - 3*complex(0,1)*l6*TH1x1*TH1x2*TH1x3*TH2x1 - complex(0,1)*l3*TH1x2*TH1x3*TH2x1**2 - complex(0,1)*l4*TH1x2*TH1x3*TH2x1**2 - 2*complex(0,1)*l5*TH1x2*TH1x3*TH2x1**2 - (3*complex(0,1)*l6*TH1x1**2*TH1x3*TH2x2)/2. - 2*complex(0,1)*l3*TH1x1*TH1x3*TH2x1*TH2x2 - 2*complex(0,1)*l4*TH1x1*TH1x3*TH2x1*TH2x2 - 4*complex(0,1)*l5*TH1x1*TH1x3*TH2x1*TH2x2 - (3*complex(0,1)*l7*TH1x3*TH2x1**2*TH2x2)/2. - (3*complex(0,1)*l6*TH1x1**2*TH1x2*TH2x3)/2. - 2*complex(0,1)*l3*TH1x1*TH1x2*TH2x1*TH2x3 - 2*complex(0,1)*l4*TH1x1*TH1x2*TH2x1*TH2x3 - 4*complex(0,1)*l5*TH1x1*TH1x2*TH2x1*TH2x3 - (3*complex(0,1)*l7*TH1x2*TH2x1**2*TH2x3)/2. - complex(0,1)*l3*TH1x1**2*TH2x2*TH2x3 - complex(0,1)*l4*TH1x1**2*TH2x2*TH2x3 - 2*complex(0,1)*l5*TH1x1**2*TH2x2*TH2x3 - 3*complex(0,1)*l7*TH1x1*TH2x1*TH2x2*TH2x3 - 6*complex(0,1)*l2*TH2x1**2*TH2x2*TH2x3 + 3*l6*TH1x1*TH1x2*TH1x3*TH3x1 + l7*TH1x3*TH2x1*TH2x2*TH3x1 + l7*TH1x2*TH2x1*TH2x3*TH3x1 + l7*TH1x1*TH2x2*TH2x3*TH3x1 - complex(0,1)*l3*TH1x2*TH1x3*TH3x1**2 - complex(0,1)*l4*TH1x2*TH1x3*TH3x1**2 + 2*complex(0,1)*l5*TH1x2*TH1x3*TH3x1**2 - (complex(0,1)*l7*TH1x3*TH2x2*TH3x1**2)/2. - (complex(0,1)*l7*TH1x2*TH2x3*TH3x1**2)/2. - 2*complex(0,1)*l2*TH2x2*TH2x3*TH3x1**2 + (3*l6*TH1x1**2*TH1x3*TH3x2)/2. + (l7*TH1x3*TH2x1**2*TH3x2)/2. + l7*TH1x1*TH2x1*TH2x3*TH3x2 - 2*complex(0,1)*l3*TH1x1*TH1x3*TH3x1*TH3x2 - 2*complex(0,1)*l4*TH1x1*TH1x3*TH3x1*TH3x2 + 4*complex(0,1)*l5*TH1x1*TH1x3*TH3x1*TH3x2 - complex(0,1)*l7*TH1x3*TH2x1*TH3x1*TH3x2 - complex(0,1)*l7*TH1x1*TH2x3*TH3x1*TH3x2 - 4*complex(0,1)*l2*TH2x1*TH2x3*TH3x1*TH3x2 + (3*l7*TH1x3*TH3x1**2*TH3x2)/2. + (3*l6*TH1x1**2*TH1x2*TH3x3)/2. + (l7*TH1x2*TH2x1**2*TH3x3)/2. + l7*TH1x1*TH2x1*TH2x2*TH3x3 - 2*complex(0,1)*l3*TH1x1*TH1x2*TH3x1*TH3x3 - 2*complex(0,1)*l4*TH1x1*TH1x2*TH3x1*TH3x3 + 4*complex(0,1)*l5*TH1x1*TH1x2*TH3x1*TH3x3 - complex(0,1)*l7*TH1x2*TH2x1*TH3x1*TH3x3 - complex(0,1)*l7*TH1x1*TH2x2*TH3x1*TH3x3 - 4*complex(0,1)*l2*TH2x1*TH2x2*TH3x1*TH3x3 + (3*l7*TH1x2*TH3x1**2*TH3x3)/2. - complex(0,1)*l3*TH1x1**2*TH3x2*TH3x3 - complex(0,1)*l4*TH1x1**2*TH3x2*TH3x3 + 2*complex(0,1)*l5*TH1x1**2*TH3x2*TH3x3 - complex(0,1)*l7*TH1x1*TH2x1*TH3x2*TH3x3 - 2*complex(0,1)*l2*TH2x1**2*TH3x2*TH3x3 + 3*l7*TH1x1*TH3x1*TH3x2*TH3x3 - 6*complex(0,1)*l2*TH3x1**2*TH3x2*TH3x3 - 3*complex(0,1)*TH1x1*TH1x2*TH1x3*TH2x1*complexconjugate(l6) - (3*complex(0,1)*TH1x1**2*TH1x3*TH2x2*complexconjugate(l6))/2. - (3*complex(0,1)*TH1x1**2*TH1x2*TH2x3*complexconjugate(l6))/2. - 3*TH1x1*TH1x2*TH1x3*TH3x1*complexconjugate(l6) - (3*TH1x1**2*TH1x3*TH3x2*complexconjugate(l6))/2. - (3*TH1x1**2*TH1x2*TH3x3*complexconjugate(l6))/2. - (3*complex(0,1)*TH1x3*TH2x1**2*TH2x2*complexconjugate(l7))/2. - (3*complex(0,1)*TH1x2*TH2x1**2*TH2x3*complexconjugate(l7))/2. - 3*complex(0,1)*TH1x1*TH2x1*TH2x2*TH2x3*complexconjugate(l7) - TH1x3*TH2x1*TH2x2*TH3x1*complexconjugate(l7) - TH1x2*TH2x1*TH2x3*TH3x1*complexconjugate(l7) - TH1x1*TH2x2*TH2x3*TH3x1*complexconjugate(l7) - (complex(0,1)*TH1x3*TH2x2*TH3x1**2*complexconjugate(l7))/2. - (complex(0,1)*TH1x2*TH2x3*TH3x1**2*complexconjugate(l7))/2. - (TH1x3*TH2x1**2*TH3x2*complexconjugate(l7))/2. - TH1x1*TH2x1*TH2x3*TH3x2*complexconjugate(l7) - complex(0,1)*TH1x3*TH2x1*TH3x1*TH3x2*complexconjugate(l7) - complex(0,1)*TH1x1*TH2x3*TH3x1*TH3x2*complexconjugate(l7) - (3*TH1x3*TH3x1**2*TH3x2*complexconjugate(l7))/2. - (TH1x2*TH2x1**2*TH3x3*complexconjugate(l7))/2. - TH1x1*TH2x1*TH2x2*TH3x3*complexconjugate(l7) - complex(0,1)*TH1x2*TH2x1*TH3x1*TH3x3*complexconjugate(l7) - complex(0,1)*TH1x1*TH2x2*TH3x1*TH3x3*complexconjugate(l7) - (3*TH1x2*TH3x1**2*TH3x3*complexconjugate(l7))/2. - complex(0,1)*TH1x1*TH2x1*TH3x2*TH3x3*complexconjugate(l7) - 3*TH1x1*TH3x1*TH3x2*TH3x3*complexconjugate(l7)',
                  order = {'QED':2})

GC_228 = Coupling(name = 'GC_228',
                  value = '-6*complex(0,1)*l1*TH1x1*TH1x2**2*TH1x3 - (3*complex(0,1)*l6*TH1x2**2*TH1x3*TH2x1)/2. - 3*complex(0,1)*l6*TH1x1*TH1x2*TH1x3*TH2x2 - 2*complex(0,1)*l3*TH1x2*TH1x3*TH2x1*TH2x2 - 2*complex(0,1)*l4*TH1x2*TH1x3*TH2x1*TH2x2 - 4*complex(0,1)*l5*TH1x2*TH1x3*TH2x1*TH2x2 - complex(0,1)*l3*TH1x1*TH1x3*TH2x2**2 - complex(0,1)*l4*TH1x1*TH1x3*TH2x2**2 - 2*complex(0,1)*l5*TH1x1*TH1x3*TH2x2**2 - (3*complex(0,1)*l7*TH1x3*TH2x1*TH2x2**2)/2. - (3*complex(0,1)*l6*TH1x1*TH1x2**2*TH2x3)/2. - complex(0,1)*l3*TH1x2**2*TH2x1*TH2x3 - complex(0,1)*l4*TH1x2**2*TH2x1*TH2x3 - 2*complex(0,1)*l5*TH1x2**2*TH2x1*TH2x3 - 2*complex(0,1)*l3*TH1x1*TH1x2*TH2x2*TH2x3 - 2*complex(0,1)*l4*TH1x1*TH1x2*TH2x2*TH2x3 - 4*complex(0,1)*l5*TH1x1*TH1x2*TH2x2*TH2x3 - 3*complex(0,1)*l7*TH1x2*TH2x1*TH2x2*TH2x3 - (3*complex(0,1)*l7*TH1x1*TH2x2**2*TH2x3)/2. - 6*complex(0,1)*l2*TH2x1*TH2x2**2*TH2x3 + (3*l6*TH1x2**2*TH1x3*TH3x1)/2. + (l7*TH1x3*TH2x2**2*TH3x1)/2. + l7*TH1x2*TH2x2*TH2x3*TH3x1 + 3*l6*TH1x1*TH1x2*TH1x3*TH3x2 + l7*TH1x3*TH2x1*TH2x2*TH3x2 + l7*TH1x2*TH2x1*TH2x3*TH3x2 + l7*TH1x1*TH2x2*TH2x3*TH3x2 - 2*complex(0,1)*l3*TH1x2*TH1x3*TH3x1*TH3x2 - 2*complex(0,1)*l4*TH1x2*TH1x3*TH3x1*TH3x2 + 4*complex(0,1)*l5*TH1x2*TH1x3*TH3x1*TH3x2 - complex(0,1)*l7*TH1x3*TH2x2*TH3x1*TH3x2 - complex(0,1)*l7*TH1x2*TH2x3*TH3x1*TH3x2 - 4*complex(0,1)*l2*TH2x2*TH2x3*TH3x1*TH3x2 - complex(0,1)*l3*TH1x1*TH1x3*TH3x2**2 - complex(0,1)*l4*TH1x1*TH1x3*TH3x2**2 + 2*complex(0,1)*l5*TH1x1*TH1x3*TH3x2**2 - (complex(0,1)*l7*TH1x3*TH2x1*TH3x2**2)/2. - (complex(0,1)*l7*TH1x1*TH2x3*TH3x2**2)/2. - 2*complex(0,1)*l2*TH2x1*TH2x3*TH3x2**2 + (3*l7*TH1x3*TH3x1*TH3x2**2)/2. + (3*l6*TH1x1*TH1x2**2*TH3x3)/2. + l7*TH1x2*TH2x1*TH2x2*TH3x3 + (l7*TH1x1*TH2x2**2*TH3x3)/2. - complex(0,1)*l3*TH1x2**2*TH3x1*TH3x3 - complex(0,1)*l4*TH1x2**2*TH3x1*TH3x3 + 2*complex(0,1)*l5*TH1x2**2*TH3x1*TH3x3 - complex(0,1)*l7*TH1x2*TH2x2*TH3x1*TH3x3 - 2*complex(0,1)*l2*TH2x2**2*TH3x1*TH3x3 - 2*complex(0,1)*l3*TH1x1*TH1x2*TH3x2*TH3x3 - 2*complex(0,1)*l4*TH1x1*TH1x2*TH3x2*TH3x3 + 4*complex(0,1)*l5*TH1x1*TH1x2*TH3x2*TH3x3 - complex(0,1)*l7*TH1x2*TH2x1*TH3x2*TH3x3 - complex(0,1)*l7*TH1x1*TH2x2*TH3x2*TH3x3 - 4*complex(0,1)*l2*TH2x1*TH2x2*TH3x2*TH3x3 + 3*l7*TH1x2*TH3x1*TH3x2*TH3x3 + (3*l7*TH1x1*TH3x2**2*TH3x3)/2. - 6*complex(0,1)*l2*TH3x1*TH3x2**2*TH3x3 - (3*complex(0,1)*TH1x2**2*TH1x3*TH2x1*complexconjugate(l6))/2. - 3*complex(0,1)*TH1x1*TH1x2*TH1x3*TH2x2*complexconjugate(l6) - (3*complex(0,1)*TH1x1*TH1x2**2*TH2x3*complexconjugate(l6))/2. - (3*TH1x2**2*TH1x3*TH3x1*complexconjugate(l6))/2. - 3*TH1x1*TH1x2*TH1x3*TH3x2*complexconjugate(l6) - (3*TH1x1*TH1x2**2*TH3x3*complexconjugate(l6))/2. - (3*complex(0,1)*TH1x3*TH2x1*TH2x2**2*complexconjugate(l7))/2. - 3*complex(0,1)*TH1x2*TH2x1*TH2x2*TH2x3*complexconjugate(l7) - (3*complex(0,1)*TH1x1*TH2x2**2*TH2x3*complexconjugate(l7))/2. - (TH1x3*TH2x2**2*TH3x1*complexconjugate(l7))/2. - TH1x2*TH2x2*TH2x3*TH3x1*complexconjugate(l7) - TH1x3*TH2x1*TH2x2*TH3x2*complexconjugate(l7) - TH1x2*TH2x1*TH2x3*TH3x2*complexconjugate(l7) - TH1x1*TH2x2*TH2x3*TH3x2*complexconjugate(l7) - complex(0,1)*TH1x3*TH2x2*TH3x1*TH3x2*complexconjugate(l7) - complex(0,1)*TH1x2*TH2x3*TH3x1*TH3x2*complexconjugate(l7) - (complex(0,1)*TH1x3*TH2x1*TH3x2**2*complexconjugate(l7))/2. - (complex(0,1)*TH1x1*TH2x3*TH3x2**2*complexconjugate(l7))/2. - (3*TH1x3*TH3x1*TH3x2**2*complexconjugate(l7))/2. - TH1x2*TH2x1*TH2x2*TH3x3*complexconjugate(l7) - (TH1x1*TH2x2**2*TH3x3*complexconjugate(l7))/2. - complex(0,1)*TH1x2*TH2x2*TH3x1*TH3x3*complexconjugate(l7) - complex(0,1)*TH1x2*TH2x1*TH3x2*TH3x3*complexconjugate(l7) - complex(0,1)*TH1x1*TH2x2*TH3x2*TH3x3*complexconjugate(l7) - 3*TH1x2*TH3x1*TH3x2*TH3x3*complexconjugate(l7) - (3*TH1x1*TH3x2**2*TH3x3*complexconjugate(l7))/2.',
                  order = {'QED':2})

GC_229 = Coupling(name = 'GC_229',
                  value = '-6*complex(0,1)*l1*TH1x2**3*TH1x3 - (9*complex(0,1)*l6*TH1x2**2*TH1x3*TH2x2)/2. - 3*complex(0,1)*l3*TH1x2*TH1x3*TH2x2**2 - 3*complex(0,1)*l4*TH1x2*TH1x3*TH2x2**2 - 6*complex(0,1)*l5*TH1x2*TH1x3*TH2x2**2 - (3*complex(0,1)*l7*TH1x3*TH2x2**3)/2. - (3*complex(0,1)*l6*TH1x2**3*TH2x3)/2. - 3*complex(0,1)*l3*TH1x2**2*TH2x2*TH2x3 - 3*complex(0,1)*l4*TH1x2**2*TH2x2*TH2x3 - 6*complex(0,1)*l5*TH1x2**2*TH2x2*TH2x3 - (9*complex(0,1)*l7*TH1x2*TH2x2**2*TH2x3)/2. - 6*complex(0,1)*l2*TH2x2**3*TH2x3 + (9*l6*TH1x2**2*TH1x3*TH3x2)/2. + (3*l7*TH1x3*TH2x2**2*TH3x2)/2. + 3*l7*TH1x2*TH2x2*TH2x3*TH3x2 - 3*complex(0,1)*l3*TH1x2*TH1x3*TH3x2**2 - 3*complex(0,1)*l4*TH1x2*TH1x3*TH3x2**2 + 6*complex(0,1)*l5*TH1x2*TH1x3*TH3x2**2 - (3*complex(0,1)*l7*TH1x3*TH2x2*TH3x2**2)/2. - (3*complex(0,1)*l7*TH1x2*TH2x3*TH3x2**2)/2. - 6*complex(0,1)*l2*TH2x2*TH2x3*TH3x2**2 + (3*l7*TH1x3*TH3x2**3)/2. + (3*l6*TH1x2**3*TH3x3)/2. + (3*l7*TH1x2*TH2x2**2*TH3x3)/2. - 3*complex(0,1)*l3*TH1x2**2*TH3x2*TH3x3 - 3*complex(0,1)*l4*TH1x2**2*TH3x2*TH3x3 + 6*complex(0,1)*l5*TH1x2**2*TH3x2*TH3x3 - 3*complex(0,1)*l7*TH1x2*TH2x2*TH3x2*TH3x3 - 6*complex(0,1)*l2*TH2x2**2*TH3x2*TH3x3 + (9*l7*TH1x2*TH3x2**2*TH3x3)/2. - 6*complex(0,1)*l2*TH3x2**3*TH3x3 - (9*complex(0,1)*TH1x2**2*TH1x3*TH2x2*complexconjugate(l6))/2. - (3*complex(0,1)*TH1x2**3*TH2x3*complexconjugate(l6))/2. - (9*TH1x2**2*TH1x3*TH3x2*complexconjugate(l6))/2. - (3*TH1x2**3*TH3x3*complexconjugate(l6))/2. - (3*complex(0,1)*TH1x3*TH2x2**3*complexconjugate(l7))/2. - (9*complex(0,1)*TH1x2*TH2x2**2*TH2x3*complexconjugate(l7))/2. - (3*TH1x3*TH2x2**2*TH3x2*complexconjugate(l7))/2. - 3*TH1x2*TH2x2*TH2x3*TH3x2*complexconjugate(l7) - (3*complex(0,1)*TH1x3*TH2x2*TH3x2**2*complexconjugate(l7))/2. - (3*complex(0,1)*TH1x2*TH2x3*TH3x2**2*complexconjugate(l7))/2. - (3*TH1x3*TH3x2**3*complexconjugate(l7))/2. - (3*TH1x2*TH2x2**2*TH3x3*complexconjugate(l7))/2. - 3*complex(0,1)*TH1x2*TH2x2*TH3x2*TH3x3*complexconjugate(l7) - (9*TH1x2*TH3x2**2*TH3x3*complexconjugate(l7))/2.',
                  order = {'QED':2})

GC_230 = Coupling(name = 'GC_230',
                  value = '-6*complex(0,1)*l1*TH1x1**2*TH1x3**2 - 3*complex(0,1)*l6*TH1x1*TH1x3**2*TH2x1 - complex(0,1)*l3*TH1x3**2*TH2x1**2 - complex(0,1)*l4*TH1x3**2*TH2x1**2 - 2*complex(0,1)*l5*TH1x3**2*TH2x1**2 - 3*complex(0,1)*l6*TH1x1**2*TH1x3*TH2x3 - 4*complex(0,1)*l3*TH1x1*TH1x3*TH2x1*TH2x3 - 4*complex(0,1)*l4*TH1x1*TH1x3*TH2x1*TH2x3 - 8*complex(0,1)*l5*TH1x1*TH1x3*TH2x1*TH2x3 - 3*complex(0,1)*l7*TH1x3*TH2x1**2*TH2x3 - complex(0,1)*l3*TH1x1**2*TH2x3**2 - complex(0,1)*l4*TH1x1**2*TH2x3**2 - 2*complex(0,1)*l5*TH1x1**2*TH2x3**2 - 3*complex(0,1)*l7*TH1x1*TH2x1*TH2x3**2 - 6*complex(0,1)*l2*TH2x1**2*TH2x3**2 + 3*l6*TH1x1*TH1x3**2*TH3x1 + 2*l7*TH1x3*TH2x1*TH2x3*TH3x1 + l7*TH1x1*TH2x3**2*TH3x1 - complex(0,1)*l3*TH1x3**2*TH3x1**2 - complex(0,1)*l4*TH1x3**2*TH3x1**2 + 2*complex(0,1)*l5*TH1x3**2*TH3x1**2 - complex(0,1)*l7*TH1x3*TH2x3*TH3x1**2 - 2*complex(0,1)*l2*TH2x3**2*TH3x1**2 + 3*l6*TH1x1**2*TH1x3*TH3x3 + l7*TH1x3*TH2x1**2*TH3x3 + 2*l7*TH1x1*TH2x1*TH2x3*TH3x3 - 4*complex(0,1)*l3*TH1x1*TH1x3*TH3x1*TH3x3 - 4*complex(0,1)*l4*TH1x1*TH1x3*TH3x1*TH3x3 + 8*complex(0,1)*l5*TH1x1*TH1x3*TH3x1*TH3x3 - 2*complex(0,1)*l7*TH1x3*TH2x1*TH3x1*TH3x3 - 2*complex(0,1)*l7*TH1x1*TH2x3*TH3x1*TH3x3 - 8*complex(0,1)*l2*TH2x1*TH2x3*TH3x1*TH3x3 + 3*l7*TH1x3*TH3x1**2*TH3x3 - complex(0,1)*l3*TH1x1**2*TH3x3**2 - complex(0,1)*l4*TH1x1**2*TH3x3**2 + 2*complex(0,1)*l5*TH1x1**2*TH3x3**2 - complex(0,1)*l7*TH1x1*TH2x1*TH3x3**2 - 2*complex(0,1)*l2*TH2x1**2*TH3x3**2 + 3*l7*TH1x1*TH3x1*TH3x3**2 - 6*complex(0,1)*l2*TH3x1**2*TH3x3**2 - 3*complex(0,1)*TH1x1*TH1x3**2*TH2x1*complexconjugate(l6) - 3*complex(0,1)*TH1x1**2*TH1x3*TH2x3*complexconjugate(l6) - 3*TH1x1*TH1x3**2*TH3x1*complexconjugate(l6) - 3*TH1x1**2*TH1x3*TH3x3*complexconjugate(l6) - 3*complex(0,1)*TH1x3*TH2x1**2*TH2x3*complexconjugate(l7) - 3*complex(0,1)*TH1x1*TH2x1*TH2x3**2*complexconjugate(l7) - 2*TH1x3*TH2x1*TH2x3*TH3x1*complexconjugate(l7) - TH1x1*TH2x3**2*TH3x1*complexconjugate(l7) - complex(0,1)*TH1x3*TH2x3*TH3x1**2*complexconjugate(l7) - TH1x3*TH2x1**2*TH3x3*complexconjugate(l7) - 2*TH1x1*TH2x1*TH2x3*TH3x3*complexconjugate(l7) - 2*complex(0,1)*TH1x3*TH2x1*TH3x1*TH3x3*complexconjugate(l7) - 2*complex(0,1)*TH1x1*TH2x3*TH3x1*TH3x3*complexconjugate(l7) - 3*TH1x3*TH3x1**2*TH3x3*complexconjugate(l7) - complex(0,1)*TH1x1*TH2x1*TH3x3**2*complexconjugate(l7) - 3*TH1x1*TH3x1*TH3x3**2*complexconjugate(l7)',
                  order = {'QED':2})

GC_231 = Coupling(name = 'GC_231',
                  value = '-6*complex(0,1)*l1*TH1x1*TH1x2*TH1x3**2 - (3*complex(0,1)*l6*TH1x2*TH1x3**2*TH2x1)/2. - (3*complex(0,1)*l6*TH1x1*TH1x3**2*TH2x2)/2. - complex(0,1)*l3*TH1x3**2*TH2x1*TH2x2 - complex(0,1)*l4*TH1x3**2*TH2x1*TH2x2 - 2*complex(0,1)*l5*TH1x3**2*TH2x1*TH2x2 - 3*complex(0,1)*l6*TH1x1*TH1x2*TH1x3*TH2x3 - 2*complex(0,1)*l3*TH1x2*TH1x3*TH2x1*TH2x3 - 2*complex(0,1)*l4*TH1x2*TH1x3*TH2x1*TH2x3 - 4*complex(0,1)*l5*TH1x2*TH1x3*TH2x1*TH2x3 - 2*complex(0,1)*l3*TH1x1*TH1x3*TH2x2*TH2x3 - 2*complex(0,1)*l4*TH1x1*TH1x3*TH2x2*TH2x3 - 4*complex(0,1)*l5*TH1x1*TH1x3*TH2x2*TH2x3 - 3*complex(0,1)*l7*TH1x3*TH2x1*TH2x2*TH2x3 - complex(0,1)*l3*TH1x1*TH1x2*TH2x3**2 - complex(0,1)*l4*TH1x1*TH1x2*TH2x3**2 - 2*complex(0,1)*l5*TH1x1*TH1x2*TH2x3**2 - (3*complex(0,1)*l7*TH1x2*TH2x1*TH2x3**2)/2. - (3*complex(0,1)*l7*TH1x1*TH2x2*TH2x3**2)/2. - 6*complex(0,1)*l2*TH2x1*TH2x2*TH2x3**2 + (3*l6*TH1x2*TH1x3**2*TH3x1)/2. + l7*TH1x3*TH2x2*TH2x3*TH3x1 + (l7*TH1x2*TH2x3**2*TH3x1)/2. + (3*l6*TH1x1*TH1x3**2*TH3x2)/2. + l7*TH1x3*TH2x1*TH2x3*TH3x2 + (l7*TH1x1*TH2x3**2*TH3x2)/2. - complex(0,1)*l3*TH1x3**2*TH3x1*TH3x2 - complex(0,1)*l4*TH1x3**2*TH3x1*TH3x2 + 2*complex(0,1)*l5*TH1x3**2*TH3x1*TH3x2 - complex(0,1)*l7*TH1x3*TH2x3*TH3x1*TH3x2 - 2*complex(0,1)*l2*TH2x3**2*TH3x1*TH3x2 + 3*l6*TH1x1*TH1x2*TH1x3*TH3x3 + l7*TH1x3*TH2x1*TH2x2*TH3x3 + l7*TH1x2*TH2x1*TH2x3*TH3x3 + l7*TH1x1*TH2x2*TH2x3*TH3x3 - 2*complex(0,1)*l3*TH1x2*TH1x3*TH3x1*TH3x3 - 2*complex(0,1)*l4*TH1x2*TH1x3*TH3x1*TH3x3 + 4*complex(0,1)*l5*TH1x2*TH1x3*TH3x1*TH3x3 - complex(0,1)*l7*TH1x3*TH2x2*TH3x1*TH3x3 - complex(0,1)*l7*TH1x2*TH2x3*TH3x1*TH3x3 - 4*complex(0,1)*l2*TH2x2*TH2x3*TH3x1*TH3x3 - 2*complex(0,1)*l3*TH1x1*TH1x3*TH3x2*TH3x3 - 2*complex(0,1)*l4*TH1x1*TH1x3*TH3x2*TH3x3 + 4*complex(0,1)*l5*TH1x1*TH1x3*TH3x2*TH3x3 - complex(0,1)*l7*TH1x3*TH2x1*TH3x2*TH3x3 - complex(0,1)*l7*TH1x1*TH2x3*TH3x2*TH3x3 - 4*complex(0,1)*l2*TH2x1*TH2x3*TH3x2*TH3x3 + 3*l7*TH1x3*TH3x1*TH3x2*TH3x3 - complex(0,1)*l3*TH1x1*TH1x2*TH3x3**2 - complex(0,1)*l4*TH1x1*TH1x2*TH3x3**2 + 2*complex(0,1)*l5*TH1x1*TH1x2*TH3x3**2 - (complex(0,1)*l7*TH1x2*TH2x1*TH3x3**2)/2. - (complex(0,1)*l7*TH1x1*TH2x2*TH3x3**2)/2. - 2*complex(0,1)*l2*TH2x1*TH2x2*TH3x3**2 + (3*l7*TH1x2*TH3x1*TH3x3**2)/2. + (3*l7*TH1x1*TH3x2*TH3x3**2)/2. - 6*complex(0,1)*l2*TH3x1*TH3x2*TH3x3**2 - (3*complex(0,1)*TH1x2*TH1x3**2*TH2x1*complexconjugate(l6))/2. - (3*complex(0,1)*TH1x1*TH1x3**2*TH2x2*complexconjugate(l6))/2. - 3*complex(0,1)*TH1x1*TH1x2*TH1x3*TH2x3*complexconjugate(l6) - (3*TH1x2*TH1x3**2*TH3x1*complexconjugate(l6))/2. - (3*TH1x1*TH1x3**2*TH3x2*complexconjugate(l6))/2. - 3*TH1x1*TH1x2*TH1x3*TH3x3*complexconjugate(l6) - 3*complex(0,1)*TH1x3*TH2x1*TH2x2*TH2x3*complexconjugate(l7) - (3*complex(0,1)*TH1x2*TH2x1*TH2x3**2*complexconjugate(l7))/2. - (3*complex(0,1)*TH1x1*TH2x2*TH2x3**2*complexconjugate(l7))/2. - TH1x3*TH2x2*TH2x3*TH3x1*complexconjugate(l7) - (TH1x2*TH2x3**2*TH3x1*complexconjugate(l7))/2. - TH1x3*TH2x1*TH2x3*TH3x2*complexconjugate(l7) - (TH1x1*TH2x3**2*TH3x2*complexconjugate(l7))/2. - complex(0,1)*TH1x3*TH2x3*TH3x1*TH3x2*complexconjugate(l7) - TH1x3*TH2x1*TH2x2*TH3x3*complexconjugate(l7) - TH1x2*TH2x1*TH2x3*TH3x3*complexconjugate(l7) - TH1x1*TH2x2*TH2x3*TH3x3*complexconjugate(l7) - complex(0,1)*TH1x3*TH2x2*TH3x1*TH3x3*complexconjugate(l7) - complex(0,1)*TH1x2*TH2x3*TH3x1*TH3x3*complexconjugate(l7) - complex(0,1)*TH1x3*TH2x1*TH3x2*TH3x3*complexconjugate(l7) - complex(0,1)*TH1x1*TH2x3*TH3x2*TH3x3*complexconjugate(l7) - 3*TH1x3*TH3x1*TH3x2*TH3x3*complexconjugate(l7) - (complex(0,1)*TH1x2*TH2x1*TH3x3**2*complexconjugate(l7))/2. - (complex(0,1)*TH1x1*TH2x2*TH3x3**2*complexconjugate(l7))/2. - (3*TH1x2*TH3x1*TH3x3**2*complexconjugate(l7))/2. - (3*TH1x1*TH3x2*TH3x3**2*complexconjugate(l7))/2.',
                  order = {'QED':2})

GC_232 = Coupling(name = 'GC_232',
                  value = '-6*complex(0,1)*l1*TH1x2**2*TH1x3**2 - 3*complex(0,1)*l6*TH1x2*TH1x3**2*TH2x2 - complex(0,1)*l3*TH1x3**2*TH2x2**2 - complex(0,1)*l4*TH1x3**2*TH2x2**2 - 2*complex(0,1)*l5*TH1x3**2*TH2x2**2 - 3*complex(0,1)*l6*TH1x2**2*TH1x3*TH2x3 - 4*complex(0,1)*l3*TH1x2*TH1x3*TH2x2*TH2x3 - 4*complex(0,1)*l4*TH1x2*TH1x3*TH2x2*TH2x3 - 8*complex(0,1)*l5*TH1x2*TH1x3*TH2x2*TH2x3 - 3*complex(0,1)*l7*TH1x3*TH2x2**2*TH2x3 - complex(0,1)*l3*TH1x2**2*TH2x3**2 - complex(0,1)*l4*TH1x2**2*TH2x3**2 - 2*complex(0,1)*l5*TH1x2**2*TH2x3**2 - 3*complex(0,1)*l7*TH1x2*TH2x2*TH2x3**2 - 6*complex(0,1)*l2*TH2x2**2*TH2x3**2 + 3*l6*TH1x2*TH1x3**2*TH3x2 + 2*l7*TH1x3*TH2x2*TH2x3*TH3x2 + l7*TH1x2*TH2x3**2*TH3x2 - complex(0,1)*l3*TH1x3**2*TH3x2**2 - complex(0,1)*l4*TH1x3**2*TH3x2**2 + 2*complex(0,1)*l5*TH1x3**2*TH3x2**2 - complex(0,1)*l7*TH1x3*TH2x3*TH3x2**2 - 2*complex(0,1)*l2*TH2x3**2*TH3x2**2 + 3*l6*TH1x2**2*TH1x3*TH3x3 + l7*TH1x3*TH2x2**2*TH3x3 + 2*l7*TH1x2*TH2x2*TH2x3*TH3x3 - 4*complex(0,1)*l3*TH1x2*TH1x3*TH3x2*TH3x3 - 4*complex(0,1)*l4*TH1x2*TH1x3*TH3x2*TH3x3 + 8*complex(0,1)*l5*TH1x2*TH1x3*TH3x2*TH3x3 - 2*complex(0,1)*l7*TH1x3*TH2x2*TH3x2*TH3x3 - 2*complex(0,1)*l7*TH1x2*TH2x3*TH3x2*TH3x3 - 8*complex(0,1)*l2*TH2x2*TH2x3*TH3x2*TH3x3 + 3*l7*TH1x3*TH3x2**2*TH3x3 - complex(0,1)*l3*TH1x2**2*TH3x3**2 - complex(0,1)*l4*TH1x2**2*TH3x3**2 + 2*complex(0,1)*l5*TH1x2**2*TH3x3**2 - complex(0,1)*l7*TH1x2*TH2x2*TH3x3**2 - 2*complex(0,1)*l2*TH2x2**2*TH3x3**2 + 3*l7*TH1x2*TH3x2*TH3x3**2 - 6*complex(0,1)*l2*TH3x2**2*TH3x3**2 - 3*complex(0,1)*TH1x2*TH1x3**2*TH2x2*complexconjugate(l6) - 3*complex(0,1)*TH1x2**2*TH1x3*TH2x3*complexconjugate(l6) - 3*TH1x2*TH1x3**2*TH3x2*complexconjugate(l6) - 3*TH1x2**2*TH1x3*TH3x3*complexconjugate(l6) - 3*complex(0,1)*TH1x3*TH2x2**2*TH2x3*complexconjugate(l7) - 3*complex(0,1)*TH1x2*TH2x2*TH2x3**2*complexconjugate(l7) - 2*TH1x3*TH2x2*TH2x3*TH3x2*complexconjugate(l7) - TH1x2*TH2x3**2*TH3x2*complexconjugate(l7) - complex(0,1)*TH1x3*TH2x3*TH3x2**2*complexconjugate(l7) - TH1x3*TH2x2**2*TH3x3*complexconjugate(l7) - 2*TH1x2*TH2x2*TH2x3*TH3x3*complexconjugate(l7) - 2*complex(0,1)*TH1x3*TH2x2*TH3x2*TH3x3*complexconjugate(l7) - 2*complex(0,1)*TH1x2*TH2x3*TH3x2*TH3x3*complexconjugate(l7) - 3*TH1x3*TH3x2**2*TH3x3*complexconjugate(l7) - complex(0,1)*TH1x2*TH2x2*TH3x3**2*complexconjugate(l7) - 3*TH1x2*TH3x2*TH3x3**2*complexconjugate(l7)',
                  order = {'QED':2})

GC_233 = Coupling(name = 'GC_233',
                  value = '-6*complex(0,1)*l1*TH1x1*TH1x3**3 - (3*complex(0,1)*l6*TH1x3**3*TH2x1)/2. - (9*complex(0,1)*l6*TH1x1*TH1x3**2*TH2x3)/2. - 3*complex(0,1)*l3*TH1x3**2*TH2x1*TH2x3 - 3*complex(0,1)*l4*TH1x3**2*TH2x1*TH2x3 - 6*complex(0,1)*l5*TH1x3**2*TH2x1*TH2x3 - 3*complex(0,1)*l3*TH1x1*TH1x3*TH2x3**2 - 3*complex(0,1)*l4*TH1x1*TH1x3*TH2x3**2 - 6*complex(0,1)*l5*TH1x1*TH1x3*TH2x3**2 - (9*complex(0,1)*l7*TH1x3*TH2x1*TH2x3**2)/2. - (3*complex(0,1)*l7*TH1x1*TH2x3**3)/2. - 6*complex(0,1)*l2*TH2x1*TH2x3**3 + (3*l6*TH1x3**3*TH3x1)/2. + (3*l7*TH1x3*TH2x3**2*TH3x1)/2. + (9*l6*TH1x1*TH1x3**2*TH3x3)/2. + 3*l7*TH1x3*TH2x1*TH2x3*TH3x3 + (3*l7*TH1x1*TH2x3**2*TH3x3)/2. - 3*complex(0,1)*l3*TH1x3**2*TH3x1*TH3x3 - 3*complex(0,1)*l4*TH1x3**2*TH3x1*TH3x3 + 6*complex(0,1)*l5*TH1x3**2*TH3x1*TH3x3 - 3*complex(0,1)*l7*TH1x3*TH2x3*TH3x1*TH3x3 - 6*complex(0,1)*l2*TH2x3**2*TH3x1*TH3x3 - 3*complex(0,1)*l3*TH1x1*TH1x3*TH3x3**2 - 3*complex(0,1)*l4*TH1x1*TH1x3*TH3x3**2 + 6*complex(0,1)*l5*TH1x1*TH1x3*TH3x3**2 - (3*complex(0,1)*l7*TH1x3*TH2x1*TH3x3**2)/2. - (3*complex(0,1)*l7*TH1x1*TH2x3*TH3x3**2)/2. - 6*complex(0,1)*l2*TH2x1*TH2x3*TH3x3**2 + (9*l7*TH1x3*TH3x1*TH3x3**2)/2. + (3*l7*TH1x1*TH3x3**3)/2. - 6*complex(0,1)*l2*TH3x1*TH3x3**3 - (3*complex(0,1)*TH1x3**3*TH2x1*complexconjugate(l6))/2. - (9*complex(0,1)*TH1x1*TH1x3**2*TH2x3*complexconjugate(l6))/2. - (3*TH1x3**3*TH3x1*complexconjugate(l6))/2. - (9*TH1x1*TH1x3**2*TH3x3*complexconjugate(l6))/2. - (9*complex(0,1)*TH1x3*TH2x1*TH2x3**2*complexconjugate(l7))/2. - (3*complex(0,1)*TH1x1*TH2x3**3*complexconjugate(l7))/2. - (3*TH1x3*TH2x3**2*TH3x1*complexconjugate(l7))/2. - 3*TH1x3*TH2x1*TH2x3*TH3x3*complexconjugate(l7) - (3*TH1x1*TH2x3**2*TH3x3*complexconjugate(l7))/2. - 3*complex(0,1)*TH1x3*TH2x3*TH3x1*TH3x3*complexconjugate(l7) - (3*complex(0,1)*TH1x3*TH2x1*TH3x3**2*complexconjugate(l7))/2. - (3*complex(0,1)*TH1x1*TH2x3*TH3x3**2*complexconjugate(l7))/2. - (9*TH1x3*TH3x1*TH3x3**2*complexconjugate(l7))/2. - (3*TH1x1*TH3x3**3*complexconjugate(l7))/2.',
                  order = {'QED':2})

GC_234 = Coupling(name = 'GC_234',
                  value = '-6*complex(0,1)*l1*TH1x2*TH1x3**3 - (3*complex(0,1)*l6*TH1x3**3*TH2x2)/2. - (9*complex(0,1)*l6*TH1x2*TH1x3**2*TH2x3)/2. - 3*complex(0,1)*l3*TH1x3**2*TH2x2*TH2x3 - 3*complex(0,1)*l4*TH1x3**2*TH2x2*TH2x3 - 6*complex(0,1)*l5*TH1x3**2*TH2x2*TH2x3 - 3*complex(0,1)*l3*TH1x2*TH1x3*TH2x3**2 - 3*complex(0,1)*l4*TH1x2*TH1x3*TH2x3**2 - 6*complex(0,1)*l5*TH1x2*TH1x3*TH2x3**2 - (9*complex(0,1)*l7*TH1x3*TH2x2*TH2x3**2)/2. - (3*complex(0,1)*l7*TH1x2*TH2x3**3)/2. - 6*complex(0,1)*l2*TH2x2*TH2x3**3 + (3*l6*TH1x3**3*TH3x2)/2. + (3*l7*TH1x3*TH2x3**2*TH3x2)/2. + (9*l6*TH1x2*TH1x3**2*TH3x3)/2. + 3*l7*TH1x3*TH2x2*TH2x3*TH3x3 + (3*l7*TH1x2*TH2x3**2*TH3x3)/2. - 3*complex(0,1)*l3*TH1x3**2*TH3x2*TH3x3 - 3*complex(0,1)*l4*TH1x3**2*TH3x2*TH3x3 + 6*complex(0,1)*l5*TH1x3**2*TH3x2*TH3x3 - 3*complex(0,1)*l7*TH1x3*TH2x3*TH3x2*TH3x3 - 6*complex(0,1)*l2*TH2x3**2*TH3x2*TH3x3 - 3*complex(0,1)*l3*TH1x2*TH1x3*TH3x3**2 - 3*complex(0,1)*l4*TH1x2*TH1x3*TH3x3**2 + 6*complex(0,1)*l5*TH1x2*TH1x3*TH3x3**2 - (3*complex(0,1)*l7*TH1x3*TH2x2*TH3x3**2)/2. - (3*complex(0,1)*l7*TH1x2*TH2x3*TH3x3**2)/2. - 6*complex(0,1)*l2*TH2x2*TH2x3*TH3x3**2 + (9*l7*TH1x3*TH3x2*TH3x3**2)/2. + (3*l7*TH1x2*TH3x3**3)/2. - 6*complex(0,1)*l2*TH3x2*TH3x3**3 - (3*complex(0,1)*TH1x3**3*TH2x2*complexconjugate(l6))/2. - (9*complex(0,1)*TH1x2*TH1x3**2*TH2x3*complexconjugate(l6))/2. - (3*TH1x3**3*TH3x2*complexconjugate(l6))/2. - (9*TH1x2*TH1x3**2*TH3x3*complexconjugate(l6))/2. - (9*complex(0,1)*TH1x3*TH2x2*TH2x3**2*complexconjugate(l7))/2. - (3*complex(0,1)*TH1x2*TH2x3**3*complexconjugate(l7))/2. - (3*TH1x3*TH2x3**2*TH3x2*complexconjugate(l7))/2. - 3*TH1x3*TH2x2*TH2x3*TH3x3*complexconjugate(l7) - (3*TH1x2*TH2x3**2*TH3x3*complexconjugate(l7))/2. - 3*complex(0,1)*TH1x3*TH2x3*TH3x2*TH3x3*complexconjugate(l7) - (3*complex(0,1)*TH1x3*TH2x2*TH3x3**2*complexconjugate(l7))/2. - (3*complex(0,1)*TH1x2*TH2x3*TH3x3**2*complexconjugate(l7))/2. - (9*TH1x3*TH3x2*TH3x3**2*complexconjugate(l7))/2. - (3*TH1x2*TH3x3**3*complexconjugate(l7))/2.',
                  order = {'QED':2})

GC_235 = Coupling(name = 'GC_235',
                  value = '-6*complex(0,1)*l1*TH1x3**4 - 6*complex(0,1)*l6*TH1x3**3*TH2x3 - 6*complex(0,1)*l3*TH1x3**2*TH2x3**2 - 6*complex(0,1)*l4*TH1x3**2*TH2x3**2 - 12*complex(0,1)*l5*TH1x3**2*TH2x3**2 - 6*complex(0,1)*l7*TH1x3*TH2x3**3 - 6*complex(0,1)*l2*TH2x3**4 + 6*l6*TH1x3**3*TH3x3 + 6*l7*TH1x3*TH2x3**2*TH3x3 - 6*complex(0,1)*l3*TH1x3**2*TH3x3**2 - 6*complex(0,1)*l4*TH1x3**2*TH3x3**2 + 12*complex(0,1)*l5*TH1x3**2*TH3x3**2 - 6*complex(0,1)*l7*TH1x3*TH2x3*TH3x3**2 - 12*complex(0,1)*l2*TH2x3**2*TH3x3**2 + 6*l7*TH1x3*TH3x3**3 - 6*complex(0,1)*l2*TH3x3**4 - 6*complex(0,1)*TH1x3**3*TH2x3*complexconjugate(l6) - 6*TH1x3**3*TH3x3*complexconjugate(l6) - 6*complex(0,1)*TH1x3*TH2x3**3*complexconjugate(l7) - 6*TH1x3*TH2x3**2*TH3x3*complexconjugate(l7) - 6*complex(0,1)*TH1x3*TH2x3*TH3x3**2*complexconjugate(l7) - 6*TH1x3*TH3x3**3*complexconjugate(l7)',
                  order = {'QED':2})

GC_236 = Coupling(name = 'GC_236',
                  value = '-(complex(0,1)*l3*TH1x1*v) - (complex(0,1)*l7*TH2x1*v)/2. + (l7*TH3x1*v)/2. - (complex(0,1)*TH2x1*v*complexconjugate(l7))/2. - (TH3x1*v*complexconjugate(l7))/2.',
                  order = {'QED':1})

GC_237 = Coupling(name = 'GC_237',
                  value = '-6*complex(0,1)*l1*TH1x1**3*v - (9*complex(0,1)*l6*TH1x1**2*TH2x1*v)/2. - 3*complex(0,1)*l3*TH1x1*TH2x1**2*v - 3*complex(0,1)*l4*TH1x1*TH2x1**2*v - 6*complex(0,1)*l5*TH1x1*TH2x1**2*v - (3*complex(0,1)*l7*TH2x1**3*v)/2. + (9*l6*TH1x1**2*TH3x1*v)/2. + (3*l7*TH2x1**2*TH3x1*v)/2. - 3*complex(0,1)*l3*TH1x1*TH3x1**2*v - 3*complex(0,1)*l4*TH1x1*TH3x1**2*v + 6*complex(0,1)*l5*TH1x1*TH3x1**2*v - (3*complex(0,1)*l7*TH2x1*TH3x1**2*v)/2. + (3*l7*TH3x1**3*v)/2. - (9*complex(0,1)*TH1x1**2*TH2x1*v*complexconjugate(l6))/2. - (9*TH1x1**2*TH3x1*v*complexconjugate(l6))/2. - (3*complex(0,1)*TH2x1**3*v*complexconjugate(l7))/2. - (3*TH2x1**2*TH3x1*v*complexconjugate(l7))/2. - (3*complex(0,1)*TH2x1*TH3x1**2*v*complexconjugate(l7))/2. - (3*TH3x1**3*v*complexconjugate(l7))/2.',
                  order = {'QED':1})

GC_238 = Coupling(name = 'GC_238',
                  value = '-(complex(0,1)*l3*TH1x2*v) - (complex(0,1)*l7*TH2x2*v)/2. + (l7*TH3x2*v)/2. - (complex(0,1)*TH2x2*v*complexconjugate(l7))/2. - (TH3x2*v*complexconjugate(l7))/2.',
                  order = {'QED':1})

GC_239 = Coupling(name = 'GC_239',
                  value = '-6*complex(0,1)*l1*TH1x1**2*TH1x2*v - 3*complex(0,1)*l6*TH1x1*TH1x2*TH2x1*v - complex(0,1)*l3*TH1x2*TH2x1**2*v - complex(0,1)*l4*TH1x2*TH2x1**2*v - 2*complex(0,1)*l5*TH1x2*TH2x1**2*v - (3*complex(0,1)*l6*TH1x1**2*TH2x2*v)/2. - 2*complex(0,1)*l3*TH1x1*TH2x1*TH2x2*v - 2*complex(0,1)*l4*TH1x1*TH2x1*TH2x2*v - 4*complex(0,1)*l5*TH1x1*TH2x1*TH2x2*v - (3*complex(0,1)*l7*TH2x1**2*TH2x2*v)/2. + 3*l6*TH1x1*TH1x2*TH3x1*v + l7*TH2x1*TH2x2*TH3x1*v - complex(0,1)*l3*TH1x2*TH3x1**2*v - complex(0,1)*l4*TH1x2*TH3x1**2*v + 2*complex(0,1)*l5*TH1x2*TH3x1**2*v - (complex(0,1)*l7*TH2x2*TH3x1**2*v)/2. + (3*l6*TH1x1**2*TH3x2*v)/2. + (l7*TH2x1**2*TH3x2*v)/2. - 2*complex(0,1)*l3*TH1x1*TH3x1*TH3x2*v - 2*complex(0,1)*l4*TH1x1*TH3x1*TH3x2*v + 4*complex(0,1)*l5*TH1x1*TH3x1*TH3x2*v - complex(0,1)*l7*TH2x1*TH3x1*TH3x2*v + (3*l7*TH3x1**2*TH3x2*v)/2. - 3*complex(0,1)*TH1x1*TH1x2*TH2x1*v*complexconjugate(l6) - (3*complex(0,1)*TH1x1**2*TH2x2*v*complexconjugate(l6))/2. - 3*TH1x1*TH1x2*TH3x1*v*complexconjugate(l6) - (3*TH1x1**2*TH3x2*v*complexconjugate(l6))/2. - (3*complex(0,1)*TH2x1**2*TH2x2*v*complexconjugate(l7))/2. - TH2x1*TH2x2*TH3x1*v*complexconjugate(l7) - (complex(0,1)*TH2x2*TH3x1**2*v*complexconjugate(l7))/2. - (TH2x1**2*TH3x2*v*complexconjugate(l7))/2. - complex(0,1)*TH2x1*TH3x1*TH3x2*v*complexconjugate(l7) - (3*TH3x1**2*TH3x2*v*complexconjugate(l7))/2.',
                  order = {'QED':1})

GC_240 = Coupling(name = 'GC_240',
                  value = '-6*complex(0,1)*l1*TH1x1*TH1x2**2*v - (3*complex(0,1)*l6*TH1x2**2*TH2x1*v)/2. - 3*complex(0,1)*l6*TH1x1*TH1x2*TH2x2*v - 2*complex(0,1)*l3*TH1x2*TH2x1*TH2x2*v - 2*complex(0,1)*l4*TH1x2*TH2x1*TH2x2*v - 4*complex(0,1)*l5*TH1x2*TH2x1*TH2x2*v - complex(0,1)*l3*TH1x1*TH2x2**2*v - complex(0,1)*l4*TH1x1*TH2x2**2*v - 2*complex(0,1)*l5*TH1x1*TH2x2**2*v - (3*complex(0,1)*l7*TH2x1*TH2x2**2*v)/2. + (3*l6*TH1x2**2*TH3x1*v)/2. + (l7*TH2x2**2*TH3x1*v)/2. + 3*l6*TH1x1*TH1x2*TH3x2*v + l7*TH2x1*TH2x2*TH3x2*v - 2*complex(0,1)*l3*TH1x2*TH3x1*TH3x2*v - 2*complex(0,1)*l4*TH1x2*TH3x1*TH3x2*v + 4*complex(0,1)*l5*TH1x2*TH3x1*TH3x2*v - complex(0,1)*l7*TH2x2*TH3x1*TH3x2*v - complex(0,1)*l3*TH1x1*TH3x2**2*v - complex(0,1)*l4*TH1x1*TH3x2**2*v + 2*complex(0,1)*l5*TH1x1*TH3x2**2*v - (complex(0,1)*l7*TH2x1*TH3x2**2*v)/2. + (3*l7*TH3x1*TH3x2**2*v)/2. - (3*complex(0,1)*TH1x2**2*TH2x1*v*complexconjugate(l6))/2. - 3*complex(0,1)*TH1x1*TH1x2*TH2x2*v*complexconjugate(l6) - (3*TH1x2**2*TH3x1*v*complexconjugate(l6))/2. - 3*TH1x1*TH1x2*TH3x2*v*complexconjugate(l6) - (3*complex(0,1)*TH2x1*TH2x2**2*v*complexconjugate(l7))/2. - (TH2x2**2*TH3x1*v*complexconjugate(l7))/2. - TH2x1*TH2x2*TH3x2*v*complexconjugate(l7) - complex(0,1)*TH2x2*TH3x1*TH3x2*v*complexconjugate(l7) - (complex(0,1)*TH2x1*TH3x2**2*v*complexconjugate(l7))/2. - (3*TH3x1*TH3x2**2*v*complexconjugate(l7))/2.',
                  order = {'QED':1})

GC_241 = Coupling(name = 'GC_241',
                  value = '-6*complex(0,1)*l1*TH1x2**3*v - (9*complex(0,1)*l6*TH1x2**2*TH2x2*v)/2. - 3*complex(0,1)*l3*TH1x2*TH2x2**2*v - 3*complex(0,1)*l4*TH1x2*TH2x2**2*v - 6*complex(0,1)*l5*TH1x2*TH2x2**2*v - (3*complex(0,1)*l7*TH2x2**3*v)/2. + (9*l6*TH1x2**2*TH3x2*v)/2. + (3*l7*TH2x2**2*TH3x2*v)/2. - 3*complex(0,1)*l3*TH1x2*TH3x2**2*v - 3*complex(0,1)*l4*TH1x2*TH3x2**2*v + 6*complex(0,1)*l5*TH1x2*TH3x2**2*v - (3*complex(0,1)*l7*TH2x2*TH3x2**2*v)/2. + (3*l7*TH3x2**3*v)/2. - (9*complex(0,1)*TH1x2**2*TH2x2*v*complexconjugate(l6))/2. - (9*TH1x2**2*TH3x2*v*complexconjugate(l6))/2. - (3*complex(0,1)*TH2x2**3*v*complexconjugate(l7))/2. - (3*TH2x2**2*TH3x2*v*complexconjugate(l7))/2. - (3*complex(0,1)*TH2x2*TH3x2**2*v*complexconjugate(l7))/2. - (3*TH3x2**3*v*complexconjugate(l7))/2.',
                  order = {'QED':1})

GC_242 = Coupling(name = 'GC_242',
                  value = '-(complex(0,1)*l3*TH1x3*v) - (complex(0,1)*l7*TH2x3*v)/2. + (l7*TH3x3*v)/2. - (complex(0,1)*TH2x3*v*complexconjugate(l7))/2. - (TH3x3*v*complexconjugate(l7))/2.',
                  order = {'QED':1})

GC_243 = Coupling(name = 'GC_243',
                  value = '-6*complex(0,1)*l1*TH1x1**2*TH1x3*v - 3*complex(0,1)*l6*TH1x1*TH1x3*TH2x1*v - complex(0,1)*l3*TH1x3*TH2x1**2*v - complex(0,1)*l4*TH1x3*TH2x1**2*v - 2*complex(0,1)*l5*TH1x3*TH2x1**2*v - (3*complex(0,1)*l6*TH1x1**2*TH2x3*v)/2. - 2*complex(0,1)*l3*TH1x1*TH2x1*TH2x3*v - 2*complex(0,1)*l4*TH1x1*TH2x1*TH2x3*v - 4*complex(0,1)*l5*TH1x1*TH2x1*TH2x3*v - (3*complex(0,1)*l7*TH2x1**2*TH2x3*v)/2. + 3*l6*TH1x1*TH1x3*TH3x1*v + l7*TH2x1*TH2x3*TH3x1*v - complex(0,1)*l3*TH1x3*TH3x1**2*v - complex(0,1)*l4*TH1x3*TH3x1**2*v + 2*complex(0,1)*l5*TH1x3*TH3x1**2*v - (complex(0,1)*l7*TH2x3*TH3x1**2*v)/2. + (3*l6*TH1x1**2*TH3x3*v)/2. + (l7*TH2x1**2*TH3x3*v)/2. - 2*complex(0,1)*l3*TH1x1*TH3x1*TH3x3*v - 2*complex(0,1)*l4*TH1x1*TH3x1*TH3x3*v + 4*complex(0,1)*l5*TH1x1*TH3x1*TH3x3*v - complex(0,1)*l7*TH2x1*TH3x1*TH3x3*v + (3*l7*TH3x1**2*TH3x3*v)/2. - 3*complex(0,1)*TH1x1*TH1x3*TH2x1*v*complexconjugate(l6) - (3*complex(0,1)*TH1x1**2*TH2x3*v*complexconjugate(l6))/2. - 3*TH1x1*TH1x3*TH3x1*v*complexconjugate(l6) - (3*TH1x1**2*TH3x3*v*complexconjugate(l6))/2. - (3*complex(0,1)*TH2x1**2*TH2x3*v*complexconjugate(l7))/2. - TH2x1*TH2x3*TH3x1*v*complexconjugate(l7) - (complex(0,1)*TH2x3*TH3x1**2*v*complexconjugate(l7))/2. - (TH2x1**2*TH3x3*v*complexconjugate(l7))/2. - complex(0,1)*TH2x1*TH3x1*TH3x3*v*complexconjugate(l7) - (3*TH3x1**2*TH3x3*v*complexconjugate(l7))/2.',
                  order = {'QED':1})

GC_244 = Coupling(name = 'GC_244',
                  value = '-6*complex(0,1)*l1*TH1x1*TH1x2*TH1x3*v - (3*complex(0,1)*l6*TH1x2*TH1x3*TH2x1*v)/2. - (3*complex(0,1)*l6*TH1x1*TH1x3*TH2x2*v)/2. - complex(0,1)*l3*TH1x3*TH2x1*TH2x2*v - complex(0,1)*l4*TH1x3*TH2x1*TH2x2*v - 2*complex(0,1)*l5*TH1x3*TH2x1*TH2x2*v - (3*complex(0,1)*l6*TH1x1*TH1x2*TH2x3*v)/2. - complex(0,1)*l3*TH1x2*TH2x1*TH2x3*v - complex(0,1)*l4*TH1x2*TH2x1*TH2x3*v - 2*complex(0,1)*l5*TH1x2*TH2x1*TH2x3*v - complex(0,1)*l3*TH1x1*TH2x2*TH2x3*v - complex(0,1)*l4*TH1x1*TH2x2*TH2x3*v - 2*complex(0,1)*l5*TH1x1*TH2x2*TH2x3*v - (3*complex(0,1)*l7*TH2x1*TH2x2*TH2x3*v)/2. + (3*l6*TH1x2*TH1x3*TH3x1*v)/2. + (l7*TH2x2*TH2x3*TH3x1*v)/2. + (3*l6*TH1x1*TH1x3*TH3x2*v)/2. + (l7*TH2x1*TH2x3*TH3x2*v)/2. - complex(0,1)*l3*TH1x3*TH3x1*TH3x2*v - complex(0,1)*l4*TH1x3*TH3x1*TH3x2*v + 2*complex(0,1)*l5*TH1x3*TH3x1*TH3x2*v - (complex(0,1)*l7*TH2x3*TH3x1*TH3x2*v)/2. + (3*l6*TH1x1*TH1x2*TH3x3*v)/2. + (l7*TH2x1*TH2x2*TH3x3*v)/2. - complex(0,1)*l3*TH1x2*TH3x1*TH3x3*v - complex(0,1)*l4*TH1x2*TH3x1*TH3x3*v + 2*complex(0,1)*l5*TH1x2*TH3x1*TH3x3*v - (complex(0,1)*l7*TH2x2*TH3x1*TH3x3*v)/2. - complex(0,1)*l3*TH1x1*TH3x2*TH3x3*v - complex(0,1)*l4*TH1x1*TH3x2*TH3x3*v + 2*complex(0,1)*l5*TH1x1*TH3x2*TH3x3*v - (complex(0,1)*l7*TH2x1*TH3x2*TH3x3*v)/2. + (3*l7*TH3x1*TH3x2*TH3x3*v)/2. - (3*complex(0,1)*TH1x2*TH1x3*TH2x1*v*complexconjugate(l6))/2. - (3*complex(0,1)*TH1x1*TH1x3*TH2x2*v*complexconjugate(l6))/2. - (3*complex(0,1)*TH1x1*TH1x2*TH2x3*v*complexconjugate(l6))/2. - (3*TH1x2*TH1x3*TH3x1*v*complexconjugate(l6))/2. - (3*TH1x1*TH1x3*TH3x2*v*complexconjugate(l6))/2. - (3*TH1x1*TH1x2*TH3x3*v*complexconjugate(l6))/2. - (3*complex(0,1)*TH2x1*TH2x2*TH2x3*v*complexconjugate(l7))/2. - (TH2x2*TH2x3*TH3x1*v*complexconjugate(l7))/2. - (TH2x1*TH2x3*TH3x2*v*complexconjugate(l7))/2. - (complex(0,1)*TH2x3*TH3x1*TH3x2*v*complexconjugate(l7))/2. - (TH2x1*TH2x2*TH3x3*v*complexconjugate(l7))/2. - (complex(0,1)*TH2x2*TH3x1*TH3x3*v*complexconjugate(l7))/2. - (complex(0,1)*TH2x1*TH3x2*TH3x3*v*complexconjugate(l7))/2. - (3*TH3x1*TH3x2*TH3x3*v*complexconjugate(l7))/2.',
                  order = {'QED':1})

GC_245 = Coupling(name = 'GC_245',
                  value = '-6*complex(0,1)*l1*TH1x2**2*TH1x3*v - 3*complex(0,1)*l6*TH1x2*TH1x3*TH2x2*v - complex(0,1)*l3*TH1x3*TH2x2**2*v - complex(0,1)*l4*TH1x3*TH2x2**2*v - 2*complex(0,1)*l5*TH1x3*TH2x2**2*v - (3*complex(0,1)*l6*TH1x2**2*TH2x3*v)/2. - 2*complex(0,1)*l3*TH1x2*TH2x2*TH2x3*v - 2*complex(0,1)*l4*TH1x2*TH2x2*TH2x3*v - 4*complex(0,1)*l5*TH1x2*TH2x2*TH2x3*v - (3*complex(0,1)*l7*TH2x2**2*TH2x3*v)/2. + 3*l6*TH1x2*TH1x3*TH3x2*v + l7*TH2x2*TH2x3*TH3x2*v - complex(0,1)*l3*TH1x3*TH3x2**2*v - complex(0,1)*l4*TH1x3*TH3x2**2*v + 2*complex(0,1)*l5*TH1x3*TH3x2**2*v - (complex(0,1)*l7*TH2x3*TH3x2**2*v)/2. + (3*l6*TH1x2**2*TH3x3*v)/2. + (l7*TH2x2**2*TH3x3*v)/2. - 2*complex(0,1)*l3*TH1x2*TH3x2*TH3x3*v - 2*complex(0,1)*l4*TH1x2*TH3x2*TH3x3*v + 4*complex(0,1)*l5*TH1x2*TH3x2*TH3x3*v - complex(0,1)*l7*TH2x2*TH3x2*TH3x3*v + (3*l7*TH3x2**2*TH3x3*v)/2. - 3*complex(0,1)*TH1x2*TH1x3*TH2x2*v*complexconjugate(l6) - (3*complex(0,1)*TH1x2**2*TH2x3*v*complexconjugate(l6))/2. - 3*TH1x2*TH1x3*TH3x2*v*complexconjugate(l6) - (3*TH1x2**2*TH3x3*v*complexconjugate(l6))/2. - (3*complex(0,1)*TH2x2**2*TH2x3*v*complexconjugate(l7))/2. - TH2x2*TH2x3*TH3x2*v*complexconjugate(l7) - (complex(0,1)*TH2x3*TH3x2**2*v*complexconjugate(l7))/2. - (TH2x2**2*TH3x3*v*complexconjugate(l7))/2. - complex(0,1)*TH2x2*TH3x2*TH3x3*v*complexconjugate(l7) - (3*TH3x2**2*TH3x3*v*complexconjugate(l7))/2.',
                  order = {'QED':1})

GC_246 = Coupling(name = 'GC_246',
                  value = '-6*complex(0,1)*l1*TH1x1*TH1x3**2*v - (3*complex(0,1)*l6*TH1x3**2*TH2x1*v)/2. - 3*complex(0,1)*l6*TH1x1*TH1x3*TH2x3*v - 2*complex(0,1)*l3*TH1x3*TH2x1*TH2x3*v - 2*complex(0,1)*l4*TH1x3*TH2x1*TH2x3*v - 4*complex(0,1)*l5*TH1x3*TH2x1*TH2x3*v - complex(0,1)*l3*TH1x1*TH2x3**2*v - complex(0,1)*l4*TH1x1*TH2x3**2*v - 2*complex(0,1)*l5*TH1x1*TH2x3**2*v - (3*complex(0,1)*l7*TH2x1*TH2x3**2*v)/2. + (3*l6*TH1x3**2*TH3x1*v)/2. + (l7*TH2x3**2*TH3x1*v)/2. + 3*l6*TH1x1*TH1x3*TH3x3*v + l7*TH2x1*TH2x3*TH3x3*v - 2*complex(0,1)*l3*TH1x3*TH3x1*TH3x3*v - 2*complex(0,1)*l4*TH1x3*TH3x1*TH3x3*v + 4*complex(0,1)*l5*TH1x3*TH3x1*TH3x3*v - complex(0,1)*l7*TH2x3*TH3x1*TH3x3*v - complex(0,1)*l3*TH1x1*TH3x3**2*v - complex(0,1)*l4*TH1x1*TH3x3**2*v + 2*complex(0,1)*l5*TH1x1*TH3x3**2*v - (complex(0,1)*l7*TH2x1*TH3x3**2*v)/2. + (3*l7*TH3x1*TH3x3**2*v)/2. - (3*complex(0,1)*TH1x3**2*TH2x1*v*complexconjugate(l6))/2. - 3*complex(0,1)*TH1x1*TH1x3*TH2x3*v*complexconjugate(l6) - (3*TH1x3**2*TH3x1*v*complexconjugate(l6))/2. - 3*TH1x1*TH1x3*TH3x3*v*complexconjugate(l6) - (3*complex(0,1)*TH2x1*TH2x3**2*v*complexconjugate(l7))/2. - (TH2x3**2*TH3x1*v*complexconjugate(l7))/2. - TH2x1*TH2x3*TH3x3*v*complexconjugate(l7) - complex(0,1)*TH2x3*TH3x1*TH3x3*v*complexconjugate(l7) - (complex(0,1)*TH2x1*TH3x3**2*v*complexconjugate(l7))/2. - (3*TH3x1*TH3x3**2*v*complexconjugate(l7))/2.',
                  order = {'QED':1})

GC_247 = Coupling(name = 'GC_247',
                  value = '-6*complex(0,1)*l1*TH1x2*TH1x3**2*v - (3*complex(0,1)*l6*TH1x3**2*TH2x2*v)/2. - 3*complex(0,1)*l6*TH1x2*TH1x3*TH2x3*v - 2*complex(0,1)*l3*TH1x3*TH2x2*TH2x3*v - 2*complex(0,1)*l4*TH1x3*TH2x2*TH2x3*v - 4*complex(0,1)*l5*TH1x3*TH2x2*TH2x3*v - complex(0,1)*l3*TH1x2*TH2x3**2*v - complex(0,1)*l4*TH1x2*TH2x3**2*v - 2*complex(0,1)*l5*TH1x2*TH2x3**2*v - (3*complex(0,1)*l7*TH2x2*TH2x3**2*v)/2. + (3*l6*TH1x3**2*TH3x2*v)/2. + (l7*TH2x3**2*TH3x2*v)/2. + 3*l6*TH1x2*TH1x3*TH3x3*v + l7*TH2x2*TH2x3*TH3x3*v - 2*complex(0,1)*l3*TH1x3*TH3x2*TH3x3*v - 2*complex(0,1)*l4*TH1x3*TH3x2*TH3x3*v + 4*complex(0,1)*l5*TH1x3*TH3x2*TH3x3*v - complex(0,1)*l7*TH2x3*TH3x2*TH3x3*v - complex(0,1)*l3*TH1x2*TH3x3**2*v - complex(0,1)*l4*TH1x2*TH3x3**2*v + 2*complex(0,1)*l5*TH1x2*TH3x3**2*v - (complex(0,1)*l7*TH2x2*TH3x3**2*v)/2. + (3*l7*TH3x2*TH3x3**2*v)/2. - (3*complex(0,1)*TH1x3**2*TH2x2*v*complexconjugate(l6))/2. - 3*complex(0,1)*TH1x2*TH1x3*TH2x3*v*complexconjugate(l6) - (3*TH1x3**2*TH3x2*v*complexconjugate(l6))/2. - 3*TH1x2*TH1x3*TH3x3*v*complexconjugate(l6) - (3*complex(0,1)*TH2x2*TH2x3**2*v*complexconjugate(l7))/2. - (TH2x3**2*TH3x2*v*complexconjugate(l7))/2. - TH2x2*TH2x3*TH3x3*v*complexconjugate(l7) - complex(0,1)*TH2x3*TH3x2*TH3x3*v*complexconjugate(l7) - (complex(0,1)*TH2x2*TH3x3**2*v*complexconjugate(l7))/2. - (3*TH3x2*TH3x3**2*v*complexconjugate(l7))/2.',
                  order = {'QED':1})

GC_248 = Coupling(name = 'GC_248',
                  value = '-6*complex(0,1)*l1*TH1x3**3*v - (9*complex(0,1)*l6*TH1x3**2*TH2x3*v)/2. - 3*complex(0,1)*l3*TH1x3*TH2x3**2*v - 3*complex(0,1)*l4*TH1x3*TH2x3**2*v - 6*complex(0,1)*l5*TH1x3*TH2x3**2*v - (3*complex(0,1)*l7*TH2x3**3*v)/2. + (9*l6*TH1x3**2*TH3x3*v)/2. + (3*l7*TH2x3**2*TH3x3*v)/2. - 3*complex(0,1)*l3*TH1x3*TH3x3**2*v - 3*complex(0,1)*l4*TH1x3*TH3x3**2*v + 6*complex(0,1)*l5*TH1x3*TH3x3**2*v - (3*complex(0,1)*l7*TH2x3*TH3x3**2*v)/2. + (3*l7*TH3x3**3*v)/2. - (9*complex(0,1)*TH1x3**2*TH2x3*v*complexconjugate(l6))/2. - (9*TH1x3**2*TH3x3*v*complexconjugate(l6))/2. - (3*complex(0,1)*TH2x3**3*v*complexconjugate(l7))/2. - (3*TH2x3**2*TH3x3*v*complexconjugate(l7))/2. - (3*complex(0,1)*TH2x3*TH3x3**2*v*complexconjugate(l7))/2. - (3*TH3x3**3*v*complexconjugate(l7))/2.',
                  order = {'QED':1})

