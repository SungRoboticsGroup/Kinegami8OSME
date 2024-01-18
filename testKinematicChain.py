# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 17:32:19 2023

@author: Daniel Feshbach
"""
from KinematicChain import *
r = 1
numSides = 6

# chain whose root is a waypoint at the global origin
chain = KinematicChain(StartFingertip(numSides, r, Pose=SE3(), length=0.5)) 

chain.show(block=True, showJointSurface=False, showLinkSurface=False, showSpheres=True)

prismaticIndex = chain.append(PrismaticJoint(numSides, r, neutralLength=3, numLayers=6, 
                        coneAngle=np.pi/4, Pose= SE3.Trans([5,5,0]) ) )

chain.show(block=True, showJointSurface=False, showLinkSurface=False, showSpheres=True)

revoluteIndex = chain.append(RevoluteJoint(numSides, r, np.pi, 
                                           SE3.Ry(np.pi/4)))

chain.show(block=True, showJointSurface=False, showLinkSurface=False, showSpheres=True)

chain.append(EndFingertip(numSides, r, Pose=SE3.Ry(np.pi/2), length=0.5))

chain.show(block=True, showJointSurface=False, showLinkSurface=False, showSpheres=True)

chain.show(block=True, showLinkPath=False, showJointPoses=False, showLinkPoses=False)

"""
KC.translateJointAlongAxis(prismaticIndex, -5)
KC.translateJointAlongAxis(revoluteIndex, -5)
KC.rotateJointAboutAxis(revoluteIndex, -np.pi/4)

KC.show(block=False)

pattern = KC.TubularPatternPattern(numSides)
pattern.show(show=True, block=False)


minPrismaticState, maxPrismaticState = chain.Joints[prismaticIndex].stateRange()
KC.setJointState(prismaticIndex, maxPrismaticState)

KC.setJointState(revoluteIndex, -np.pi/2)
KC.show(block=True)
"""