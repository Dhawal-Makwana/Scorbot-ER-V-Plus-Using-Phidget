from functions import control



def by_angles():
  
  angles = list(map(int, input(
	"Enter the angles for Base, Shoulder, Elbow, wrist Link(Space-Separated): ").strip().split()))[:4]
  print('Angles Entered are', angles) 
  
  #Base Angle
  if angles[0] > 0:
    control(146552, 1, .055 * angles[0]) 
  else:
    control(146552, -1, -0.055 * angles[0])
  
  #Shoulder Angle
  if angles[1] > 0:
    control(146627, 1, .055 * angles[1]) 
  else:
    control(146627, -1, -0.055 * angles[1])

  #Elbow Angle
  if angles[2] > 0:
    control(146520, 1, .04 * angles[2]) 
  else:
    control(146520, -1, -0.04 * angles[2])
  # wrist angle  
  if angles[3] > 0:
    control(146680, 1, .055 * angles[3]) 
  else:
    control(146680, -1, -.055 * angles[3])
    
def draw():
    control(146552, -0.5, 2.5) 
    control(146680, -0.5, 2.5)
    control(146552, 0.5, 2.5)
    control(146680, 0.5, 2.5)

  
  
  
  
  
  
 
  
  
    
     
      
        
  
 
