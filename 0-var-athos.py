class Var:
  def __init__(self, name, modules = [], variables = {}):
    self.name = name
    self.modules = modules
    self.variables = variables

variants = [ Var('g1D', ['gcc', 'openmpi/2.0.2'],
                {'CC' :'gcc',
		 'CXX' : 'g++',
		 'MPICC' : 'mpicc -L/opt/openmpi-2.0.2/lib/x86_64-linux-gnu',
		 'MPICXX' : 'mpicxx -L/opt/openmpi-2.0.2/lib/x86_64-linux-gnu',
		 'FC' : 'gfortran',
		 'FCLIB' : '-lgfortran',
		 'ZOLTAN' : 'no'}),
             Var('g2D', ['gcc', 'openmpi/2.0.1'],
                {'CC' :'gcc',
		 'CXX' : 'g++',
		 'MPICC' : 'mpicc -L/opt/openmpi/2.0.1-athos/lib/x86_64-linux-gnu',
		 'MPICXX' : 'mpicxx -L/opt/openmpi/2.0.1-athos/lib/x86_64-linux-gnu',
		 'FC' : 'gfortran',
		 'FCLIB' : '-lgfortran',
		 'ZOLTAN' : 'no'}),
             Var('g3D', ['gcc', 'openmpi/1.10.4'],
                {'CC' :'gcc',
		 'CXX' : 'g++',
		 'MPICC' : 'mpicc -L/opt/openmpi/1.10.4-athos/lib/x86_64-linux-gnu',
		 'MPICXX' : 'mpicxx -L/opt/openmpi/1.10.4-athos/lib/x86_64-linux-gnu',
		 'FC' : 'gfortran',
		 'FCLIB' : '-lgfortran',
		 'ZOLTAN' : 'no'}),
             Var('g4D', ['gcc', 'impi/2016.4.072'],
                {'CC' :'gcc',
		 'CXX' : 'g++',
		 'MPICC' : 'mpicc -L/opt/intel/2016.4.072/impi/5.1.3.258/lib64',
		 'MPICXX' : 'mpicxx -L/opt/intel/2016.4.072/impi/5.1.3.258/lib64',
		 'FC' : 'gfortran',
		 'FCLIB' : '-lgfortran',
		 'ZOLTAN' : 'no'}),
             Var('g5D', ['gcc', 'impi/2016.0.047'],
                {'CC' :'gcc',
		 'CXX' : 'g++',
		 'MPICC' : 'mpicc -L/opt/intel/2016.0.047/impi/5.1.1.109/lib64',
		 'MPICXX' : 'mpicxx -L/opt/intel/2016.0.047/impi/5.1.1.109/lib64',
		 'FC' : 'gfortran',
		 'FCLIB' : '-lgfortran',
		 'ZOLTAN' : 'no'}),
             Var('g6D', ['gcc', 'impi/2015.1.133'],
                {'CC' :'gcc',
		 'CXX' : 'g++',
		 'MPICC' : 'mpicc -L/opt/intel/2015.1.133/impi/5.0.2.044/lib64',
		 'MPICXX' : 'mpicxx -L/opt/intel/2015.1.133/impi/5.0.2.044/lib64',
		 'FC' : 'gfortran',
		 'FCLIB' : '-lgfortran',
		 'ZOLTAN' : 'no'}),
             Var('g7D', ['gcc', 'impi/2013.1.046'],
                {'CC' :'gcc',
		 'CXX' : 'g++',
		 'MPICC' : 'mpicc -L/opt/intel/2013.1.046/impi/4.1.3.048/lib64',
		 'MPICXX' : 'mpicxx -L/opt/intel/2013.1.046/impi/4.1.3.048/lib64',
		 'FC' : 'gfortran',
		 'FCLIB' : '-lgfortran',
		 'ZOLTAN' : 'no'})
            ]