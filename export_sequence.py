import c4d
import os
import subprocess
from c4d import gui
# Welcome to the world of Python


def recurse_hierarchy(op, matrices):
    
    if len(op.GetChildren()) > 0:
        print '--- parent ---'
        print op.GetName()
        print len(op.GetChildren())
        print '---------------'
        children = op.GetChildren()
        for child in children:
            recurse_hierarchy(child, matrices)
    else:
        print '--- poly ---'
        print op.GetName()
        #print str(op.GetMl())
        matrices.append(str(op.GetMl()))
        print '---------------'

# Main function
def main():
    doc = c4d.documents.GetActiveDocument()
    obj = doc.GetActiveObject()


    
    
    
    

    # retrieve fps
    docFps = 30
    
    # Get Animation Length
    fromTime = 60
    toTime = 61
    animLength = toTime - fromTime + 1


    frames = []
    for x in range(0,animLength):
        moveTime = c4d.BaseTime(fromTime,docFps) + c4d.BaseTime(x,docFps)
        doc.SetTime(moveTime)
        c4d.EventAdd(c4d.EVENT_FORCEREDRAW)
        c4d.DrawViews(c4d.DRAWFLAGS_FORCEFULLREDRAW)

        # progress bar
        c4d.StatusSetText("Exporting " + str(x) + " of " + str(animLength))
        c4d.StatusSetBar(100.0*x/animLength)

        frame_matrices = []
        recurse_hierarchy(obj.GetCache(), frame_matrices)
        frames.append(frame_matrices)

    

    string_matrices = []
    for matrices in frames:
        string_matrices.append('\n'.join(matrices))


    filePath = c4d.storage.SaveDialog()
    txt_file = open(filePath,'w')
    txt_file.write('\n---\n'.join(string_matrices))
    txt_file.close()
    c4d.StatusClear()
    
# Execute main()
if __name__=='__main__':
    main()