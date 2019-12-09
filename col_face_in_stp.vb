' NX 12.0.2.9
' Journal created by sapresco on Fri Nov  1 13:47:44 2019 W. Europe Standard Time
'
Imports System
Imports NXOpen

Module NXJournal
    Sub Main(ByVal args() As String)

        Dim theSession As NXOpen.Session = NXOpen.Session.GetSession()
        ' ----------------------------------------------
        '   Menu: File->Open...
        ' ----------------------------------------------
        Dim basePart1 As NXOpen.BasePart = Nothing
        Dim partLoadStatus1 As NXOpen.PartLoadStatus = Nothing
        basePart1 = theSession.Parts.OpenActiveDisplay("C:\CAD19\Panel concept 2019-10-24.STEP", NXOpen.DisplayPartOption.AllowAdditional, partLoadStatus1)

        Dim workPart As NXOpen.Part = theSession.Parts.Work

        Dim displayPart As NXOpen.Part = theSession.Parts.Display

        partLoadStatus1.Dispose()
        theSession.ApplicationSwitchImmediate("UG_APP_MODELING")

        ' ----------------------------------------------
        '   Menu: Tools->Repeat Command->4 Stop Journal Recording
        ' ----------------------------------------------
        ' ----------------------------------------------
        '   Menu: Tools->Journal->Stop Recording
        ' ----------------------------------------------
        ' ----------------------------------------------
        '   Menu: Edit->Object Display...
        ' ----------------------------------------------
        Dim markId1 As NXOpen.Session.UndoMarkId = Nothing
        markId1 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")

        theSession.SetUndoMarkName(markId1, "Class Selection Dialog")

        ' ----------------------------------------------
        '   Dialog Begin Select by Type
        ' ----------------------------------------------
        Dim markId2 As NXOpen.Session.UndoMarkId = Nothing
        markId2 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Class Selection")

        theSession.DeleteUndoMark(markId2, Nothing)

        Dim markId3 As NXOpen.Session.UndoMarkId = Nothing
        markId3 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Class Selection")

        theSession.DeleteUndoMark(markId3, Nothing)

        theSession.SetUndoMarkName(markId1, "Class Selection")

        theSession.DeleteUndoMark(markId1, Nothing)

        ' ----------------------------------------------
        '   Dialog Begin Edit Object Display
        ' ----------------------------------------------
        ' ----------------------------------------------
        '   Dialog Begin Color
        ' ----------------------------------------------
        Dim markId4 As NXOpen.Session.UndoMarkId = Nothing
        markId4 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Edit Object Display")

        Dim displayModification1 As NXOpen.DisplayModification = Nothing
        displayModification1 = theSession.DisplayManager.NewDisplayModification()

        displayModification1.ApplyToAllFaces = True

        displayModification1.ApplyToOwningParts = False

        displayModification1.NewColor = 100

        displayModification1.NewWidth = NXOpen.DisplayableObject.ObjectWidth.One

        Dim objects1(0) As NXOpen.DisplayableObject
        Dim objects2(0) As NXOpen.DisplayableObject

        Dim brep1 As NXOpen.Features.Brep = CType(workPart.Features.FindObject("UNPARAMETERIZED_FEATURE(1)"), NXOpen.Features.Brep)

        Dim face1 As NXOpen.Face = CType(brep1.FindObject("FACE 2 {(35,5,-10) UNPARAMETERIZED_FEATURE(1)}"), NXOpen.Face)
        Dim face2 As NXOpen.Face = CType(brep1.FindObject("FACE 9 {(35,5,-10) UNPARAMETERIZED_FEATURE(1)}"), NXOpen.Face)


        objects1(0) = face1
        objects2(0) = face2

        displayModification1.Apply(objects1)
        displayModification1.Apply(objects2)


        Dim nErrs1 As Integer = Nothing
        nErrs1 = theSession.UpdateManager.DoUpdate(markId4)

        displayModification1.Dispose()
    End Sub
End Module
