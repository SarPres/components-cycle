'Journal to walk through the assembly structure
' will run on assemblies or piece parts
' will step through all "components of 1st level" of the displayed part and make them displayed part

Option Strict Off

Imports System
Imports NXOpen
Imports NXOpen.UF
Imports NXOpen.Assemblies
Imports System.IO
Imports NXOpenUI
Imports System.Windows.Forms

Module NXJournal

    Public theSession As Session = Session.GetSession()
    Public ufs As UFSession = UFSession.GetUFSession()
    Public lw As ListingWindow = theSession.ListingWindow

    Sub Main()
        Dim workPart As Part = theSession.Parts.Work
        Dim dispPart As Part = theSession.Parts.Display
        'lw.Open
        Try
            Dim c As ComponentAssembly = dispPart.ComponentAssembly
            'to process the work part rather than the display part,
            ' comment the previous line and uncomment the following line
            'Dim c As ComponentAssembly = workPart.ComponentAssembly
            If Not IsNothing(c.RootComponent) Then
                '*** insert code to process 'root component' (assembly file)
                'lw.WriteLine("Assembly: " & c.RootComponent.DisplayName)
                'lw.WriteLine(" + Active Arrangement: " & c.ActiveArrangement.Name)
                '*** end of code to process root component
                'lw.WriteLine("")
                'lw.WriteLine("comps")
                'lw.WriteLine("")
                Dim comps() As component = c.RootComponent.getchildren()
                Dim part2 As Part = CType(theSession.Parts.FindObject(c.RootComponent.DisplayName), Part)
                For i As Integer = 0 To (comps.Length - 1)
                    'lw.writeline( comps(i).name )
                    '-----------------------------------------------------------
                    Dim component1 As Assemblies.Component = comps(i)
                    Dim components1(0) As Assemblies.Component
                    components1(0) = component1
                    Dim errorList1 As ErrorList
                    errorList1 = component1.DisplayComponentsExact(components1)
                    errorList1.Clear()
                    Dim part1 As Part = CType(theSession.Parts.FindObject(comps(i).displayname), Part)
                    part1.Preferences.Modeling.CutViewUpdateDelayed = True
                    Dim partLoadStatus1 As PartLoadStatus
                    Dim status1 As PartCollection.SdpsStatus
                    status1 = theSession.Parts.SetDisplay(part1, True, False, partLoadStatus1)
                    workPart = theSession.Parts.Work
                    dispPart = theSession.Parts.Display
                    partLoadStatus1.Dispose()
                    'MessageBox.Show(comps(i).displayname)
                    'SARAH EDITS START
                    If comps(i).displayname = "Frame" Or comps(i).displayname = "Nut" Then
                        Dim displayModification1 As NXOpen.DisplayModification = Nothing
                        displayModification1 = theSession.DisplayManager.NewDisplayModification()

                        displayModification1.ApplyToAllFaces = True

                        displayModification1.ApplyToOwningParts = False

                        displayModification1.NewColor = 36

                        Dim objects1(0) As NXOpen.DisplayableObject
                        'Dim component1 As NXOpen.Assemblies.Component = CType(workPart.ComponentAssembly.RootComponent.FindObject("COMPONENT model2 1"), NXOpen.Assemblies.Component)

                        objects1(0) = component1
                        displayModification1.Apply(objects1)

                        Dim nErrs1 As Integer = Nothing
                        'nErrs1 = theSession.UpdateManager.DoUpdate(markId4)

                        displayModification1.Dispose()
                    End If
                    'SARAH EDITS END
                    '------------------------------------------------------------
                    'Dim part2 As Part = CType(theSession.Parts.FindObject(c.RootComponent.DisplayName), Part)
                    workPart.Preferences.Modeling.CutViewUpdateDelayed = True
                    Dim partLoadStatus2 As PartLoadStatus
                    Dim status2 As PartCollection.SdpsStatus
                    status2 = theSession.Parts.SetDisplay(part2, True, False, partLoadStatus2)
                    workPart = theSession.Parts.Work
                    dispPart = theSession.Parts.Display
                    partLoadStatus2.Dispose()
                    '------------------------------------------------------------
                Next
                workPart.Preferences.Modeling.CutViewUpdateDelayed = True
                Dim partLoadStatus6 As PartLoadStatus
                Dim status6 As PartCollection.SdpsStatus
                status6 = theSession.Parts.SetDisplay(part2, True, False, partLoadStatus6)
                workPart = theSession.Parts.Work
                dispPart = theSession.Parts.Display
                Dim nullAssemblies_Component As Assemblies.Component = Nothing
                dispPart.Preferences.Modeling.CutViewUpdateDelayed = True
                Dim partLoadStatus7 As PartLoadStatus
                theSession.Parts.SetWorkComponent(nullAssemblies_Component, PartCollection.RefsetOption.Current, PartCollection.WorkComponentOption.Visible, partLoadStatus7)
                workPart = theSession.Parts.Work
                partLoadStatus7.Dispose()
                MessageBox.Show(c.RootComponent.DisplayName)
            Else
                '*** insert code to process piece part
                lw.WriteLine("Part has no components")
            End If
        Catch e As Exception
            theSession.ListingWindow.WriteLine("Failed: " & e.ToString)
        End Try
        'lw.Close

    End Sub

    '**********************************************************
    Public Function GetUnloadOption(ByVal dummy As String) As Integer
        Return Session.LibraryUnloadOption.Immediately
    End Function
    '**********************************************************

End Module