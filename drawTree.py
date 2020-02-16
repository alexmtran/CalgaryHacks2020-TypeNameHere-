from SimpleGraphics import *
stepDown = 15
xPos = 400
yPos = 50
xPos1 = 400
xPos2 = 400
preqs = {
    'CPSC 461': {
        'CPSC 355': {
            'CPSC 331': {
                'MATH 271': {},
                'CPSC 233': {
                    'CPSC 231': {
                    }
                }
            }
        }
    }
}

def preqTree(preqs, xPos, yPos):
    setFont("Garamond", "18", "bold")
 
    for key, item in preqs.items():
        if isinstance(item, dict):
            if len(item) > 1:
                text(xPos, yPos, key)
                xPos1 -= 100
                xPos2 += 100
                line(xPos, yPos+stepDown, xPos1, yPos+stepDown*2)
                line(xPos, yPos+stepDown, xPos2, yPos+stepDown*2)
                

                preqTree(preqs[key], xPos, yPos + 3*stepDown)
                
            else:
                line(xPos, yPos+stepDown, xPos, yPos + 2*stepDown)
                text(xPos, yPos, key + ' ' + str(len(item)))
                preqTree(preqs[key], xPos, yPos + 3*stepDown)

        else:
            continue

preqTree(preqs, xPos, yPos)