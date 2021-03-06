from pyplasm import *
from scipy import *
import os,sys
""" import modules from larcc/lib """
sys.path.insert(0, '/home/j-hard/Programmazione/python/lib/lar-cc/lib/py/')

from architectural import *
from lar2psm import *
from simplexn import *
from larcc import *
from largrid import *
from mapper import *
from boolean import *
from sysml import *



DRAW = COMP([VIEW,STRUCT,MKPOLS])

bagno = assemblyDiagramInit([3,2,2])([[.3,3,.3],[3,.3],[.3,2.7]])
V,CV = bagno
hpcb= SKEL_1(STRUCT(MKPOLS(bagno)))
hpcb = cellNumbering (bagno,hpcb)(range(len(CV)),CYAN,1)
VIEW(hpcb)

toMerge = 7
cell = MKPOL([bagno[0],[[v+1 for v in  bagno[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))

diagram = assemblyDiagramInit([3,1,3])([[.4,.5,2],[.3],[1,1.2,.5]])
bagno = diagram2cell(diagram,bagno,toMerge)
hpcb= SKEL_1(STRUCT(MKPOLS(bagno)))
hpcb = cellNumbering (bagno,hpcb)(range(len(bagno[1])),CYAN,1)
VIEW(hpcb)

toRemove = [5,15]
bagno = bagno[0], [cell for k,cell in enumerate(bagno[1]) if not (k in toRemove)]
DRAW(bagno)
hpcb = SKEL_1(STRUCT(MKPOLS(bagno)))
hpcb = cellNumbering (bagno,hpcb)(range(len(bagno[1])),CYAN,1)
VIEW(hpcb)

bagno=STRUCT(MKPOLS(bagno)) 


soggiorno= assemblyDiagramInit([3,3,2])([[.3,7,.3],[.3,12,.3],[.3,2.7]])
V,CV = soggiorno
s= SKEL_1(STRUCT(MKPOLS(soggiorno)))
s = cellNumbering (soggiorno,s)(range(len(CV)),CYAN,1)
VIEW(s)

toMerge = 7
cell = MKPOL([soggiorno[0],[[v+1 for v in  soggiorno[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))

diagram = assemblyDiagramInit([8,1,3])([[1.5,1,1.5,.2,1,.2,1,.6],[.3],[1,1.2,.5]])
soggiorno = diagram2cell(diagram,soggiorno,toMerge)
hpcs= SKEL_1(STRUCT(MKPOLS(soggiorno)))
hpcs = cellNumbering (soggiorno,hpcs)(range(len(soggiorno[1])),CYAN,1)

VIEW(hpcs)

toMerge = 10
cell = MKPOL([soggiorno[0],[[v+1 for v in  soggiorno[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))

diagram = assemblyDiagramInit([3,1,2])([[6.5,1,.5],[.3],[2.2,.5]])
soggiorno = diagram2cell(diagram,soggiorno,toMerge)
hpcs= SKEL_1(STRUCT(MKPOLS(soggiorno)))
hpcs = cellNumbering (soggiorno,hpcs)(range(len(soggiorno[1])),CYAN,1)
VIEW(hpcs)

toRemove = [8,20,28,29,35,42]
soggiorno= soggiorno[0], [cell for k,cell in enumerate(soggiorno[1]) if not (k in toRemove)]
DRAW(soggiorno)
hpcs = SKEL_1(STRUCT(MKPOLS(soggiorno)))
hpcs = cellNumbering (soggiorno,hpcs)(range(len(soggiorno[1])),CYAN,1)
VIEW(hpcs)

soggiorno=STRUCT(MKPOLS(soggiorno))

camera= assemblyDiagramInit([2,2,2])([[3.9,.1],[3.9,.1],[.3,2.7]])
V,CV = camera
hpcc= SKEL_1(STRUCT(MKPOLS(camera)))
hpcc = cellNumbering (camera,hpcc)(range(len(CV)),CYAN,1)
VIEW(hpcc)

toMerge = 5
cell = MKPOL([camera[0],[[v+1 for v in  camera[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))

diagram = assemblyDiagramInit([1,3,2])([[.1],[1.5,1,1.5],[2.2,.5]])
camera = diagram2cell(diagram,camera,toMerge)
hpcc= SKEL_1(STRUCT(MKPOLS(camera)))
hpcc = cellNumbering (camera,hpcc)(range(len(camera[1])),CYAN,1)
VIEW(hpcc)

toRemove = [1,9]
camera = camera[0],[cell for k,cell in enumerate(camera[1]) if not (k in toRemove)]
DRAW(camera)
hpcc = SKEL_1(STRUCT(MKPOLS(camera)))
hpcc = cellNumbering (camera,hpcc)(range(len(camera[1])),CYAN,1)

camera=STRUCT(MKPOLS(camera))



scale= assemblyDiagramInit([2,2,2])([[3.9,.1],[2,.1],[.3,2.7]])
V,CV = scale
sc= SKEL_1(STRUCT(MKPOLS(scale)))
sc = cellNumbering (scale,sc)(range(len(CV)),CYAN,1)
VIEW(sc)


toMerge = 5
cell = MKPOL([scale[0],[[v+1 for v in  scale[1][toMerge]]],None])
#VIEW(STRUCT([hpcsc,cell]))

diagram = assemblyDiagramInit([1,3,2])([[.1],[.5,1,.5],[2.2,.5]])
scale = diagram2cell(diagram,scale,toMerge)
hpcsc= SKEL_1(STRUCT(MKPOLS(scale)))
hpcsc = cellNumbering (scale,hpcsc)(range(len(scale[1])),CYAN,1)
VIEW(STRUCT([hpcsc,cell]))
VIEW(hpcsc)

toRemove = [1,9]
scale = scale[0],[cell for k,cell in enumerate(scale[1]) if not (k in toRemove)]

scale=STRUCT(MKPOLS(scale))

flat=STRUCT([T([1,2])([.3,4.3])(scale),T([1,2])([.3,.3])(camera),T([1,2])([4,12.3])(bagno),soggiorno])
VIEW(flat)


