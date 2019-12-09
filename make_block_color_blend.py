# NX 12.0.2.9
# Journal created by sapresco on Wed Nov 20 12:51:22 2019 W. Europe Standard Time
#
import math
import NXOpen
import NXOpen.Features
import NXOpen.GeometricUtilities
def main() : 

    theSession  = NXOpen.Session.GetSession()
    workPart = theSession.Parts.Work
    displayPart = theSession.Parts.Display
    # ----------------------------------------------
    #   Menu: Insert->Design Feature->Block...
    # ----------------------------------------------
    markId1 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    blockFeatureBuilder1 = workPart.Features.CreateBlockFeatureBuilder(NXOpen.Features.Feature.Null)
    
    blockFeatureBuilder1.BooleanOption.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    targetBodies1 = [NXOpen.Body.Null] * 1 
    targetBodies1[0] = NXOpen.Body.Null
    blockFeatureBuilder1.BooleanOption.SetTargetBodies(targetBodies1)
    
    blockFeatureBuilder1.BooleanOption.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    targetBodies2 = [NXOpen.Body.Null] * 1 
    targetBodies2[0] = NXOpen.Body.Null
    blockFeatureBuilder1.BooleanOption.SetTargetBodies(targetBodies2)
    
    theSession.SetUndoMarkName(markId1, "Block Dialog")
    
    coordinates1 = NXOpen.Point3d(0.0, 0.0, 0.0)
    point1 = workPart.Points.CreatePoint(coordinates1)
    
    unit1 = workPart.UnitCollection.FindObject("MilliMeter")
    expression1 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    markId2 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Block")
    
    theSession.DeleteUndoMark(markId2, None)
    
    markId3 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Block")
    
    blockFeatureBuilder1.Type = NXOpen.Features.BlockFeatureBuilder.Types.OriginAndEdgeLengths
    
    blockFeatureBuilder1.OriginPoint = point1
    
    originPoint1 = NXOpen.Point3d(0.0, 0.0, 0.0)
    blockFeatureBuilder1.SetOriginAndLengths(originPoint1, "150", "100", "50")
    
    blockFeatureBuilder1.SetBooleanOperationAndTarget(NXOpen.Features.Feature.BooleanType.Create, NXOpen.Body.Null)
    
    feature1 = blockFeatureBuilder1.CommitFeature()
    
    theSession.DeleteUndoMark(markId3, None)
    
    theSession.SetUndoMarkName(markId1, "Block")
    
    blockFeatureBuilder1.Destroy()
    
    workPart.Expressions.Delete(expression1)
    
    # ----------------------------------------------
    #   Menu: Insert->Detail Feature->Edge Blend...
    # ----------------------------------------------
    markId4 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    edgeBlendBuilder1 = workPart.Features.CreateEdgeBlendBuilder(NXOpen.Features.Feature.Null)
    
    expression2 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression3 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    blendLimitsData1 = edgeBlendBuilder1.LimitsListData
    
    origin1 = NXOpen.Point3d(0.0, 0.0, 0.0)
    normal1 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    plane1 = workPart.Planes.CreatePlane(origin1, normal1, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    facePlaneSelectionBuilder1 = workPart.FacePlaneSelectionBuilderData.Create()
    
    expression4 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression5 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    theSession.SetUndoMarkName(markId4, "Edge Blend Dialog")
    
    scCollector1 = workPart.ScCollectors.CreateCollector()
    
    seedEdges1 = [NXOpen.Edge.Null] * 1 
    block1 = feature1
    edge1 = block1.FindObject("EDGE * 1 * 2 {(150,0,50)(75,0,50)(0,0,50) BLOCK(1)}")
    seedEdges1[0] = edge1
    edgeMultipleSeedTangentRule1 = workPart.ScRuleFactory.CreateRuleEdgeMultipleSeedTangent(seedEdges1, 0.5, True)
    
    rules1 = [None] * 1 
    rules1[0] = edgeMultipleSeedTangentRule1
    scCollector1.ReplaceRules(rules1, False)
    
    seedEdges2 = [NXOpen.Edge.Null] * 2 
    seedEdges2[0] = edge1
    edge2 = block1.FindObject("EDGE * 1 * 6 {(150,100,50)(150,50,50)(150,0,50) BLOCK(1)}")
    seedEdges2[1] = edge2
    edgeMultipleSeedTangentRule2 = workPart.ScRuleFactory.CreateRuleEdgeMultipleSeedTangent(seedEdges2, 0.5, True)
    
    rules2 = [None] * 1 
    rules2[0] = edgeMultipleSeedTangentRule2
    scCollector1.ReplaceRules(rules2, False)
    
    seedEdges3 = [NXOpen.Edge.Null] * 3 
    seedEdges3[0] = edge1
    seedEdges3[1] = edge2
    edge3 = block1.FindObject("EDGE * 1 * 4 {(0,100,50)(75,100,50)(150,100,50) BLOCK(1)}")
    seedEdges3[2] = edge3
    edgeMultipleSeedTangentRule3 = workPart.ScRuleFactory.CreateRuleEdgeMultipleSeedTangent(seedEdges3, 0.5, True)
    
    rules3 = [None] * 1 
    rules3[0] = edgeMultipleSeedTangentRule3
    scCollector1.ReplaceRules(rules3, False)
    
    seedEdges4 = [NXOpen.Edge.Null] * 4 
    seedEdges4[0] = edge1
    seedEdges4[1] = edge2
    seedEdges4[2] = edge3
    edge4 = block1.FindObject("EDGE * 1 * 3 {(0,0,50)(0,50,50)(0,100,50) BLOCK(1)}")
    seedEdges4[3] = edge4
    edgeMultipleSeedTangentRule4 = workPart.ScRuleFactory.CreateRuleEdgeMultipleSeedTangent(seedEdges4, 0.5, True)
    
    rules4 = [None] * 1 
    rules4[0] = edgeMultipleSeedTangentRule4
    scCollector1.ReplaceRules(rules4, False)
    
    markId5 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Edge Blend")
    
    theSession.DeleteUndoMark(markId5, None)
    
    markId6 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Edge Blend")
    
    edgeBlendBuilder1.Tolerance = 0.01
    
    edgeBlendBuilder1.AllInstancesOption = False
    
    edgeBlendBuilder1.RemoveSelfIntersection = True
    
    edgeBlendBuilder1.PatchComplexGeometryAreas = True
    
    edgeBlendBuilder1.LimitFailingAreas = True
    
    edgeBlendBuilder1.ConvexConcaveY = False
    
    edgeBlendBuilder1.RollOverSmoothEdge = True
    
    edgeBlendBuilder1.RollOntoEdge = True
    
    edgeBlendBuilder1.MoveSharpEdge = True
    
    edgeBlendBuilder1.TrimmingOption = False
    
    edgeBlendBuilder1.OverlapOption = NXOpen.Features.EdgeBlendBuilder.Overlap.AnyConvexityRollOver
    
    edgeBlendBuilder1.BlendOrder = NXOpen.Features.EdgeBlendBuilder.OrderOfBlending.ConvexFirst
    
    edgeBlendBuilder1.SetbackOption = NXOpen.Features.EdgeBlendBuilder.Setback.SeparateFromCorner
    
    edgeBlendBuilder1.BlendFaceContinuity = NXOpen.Features.EdgeBlendBuilder.FaceContinuity.Tangent
    
    csIndex1 = edgeBlendBuilder1.AddChainset(scCollector1, "5")
    
    feature2 = edgeBlendBuilder1.CommitFeature()
    
    theSession.DeleteUndoMark(markId6, None)
    
    theSession.SetUndoMarkName(markId4, "Edge Blend")
    
    workPart.FacePlaneSelectionBuilderData.Destroy(facePlaneSelectionBuilder1)
    
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression5)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression4)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    edgeBlendBuilder1.Destroy()
    
    workPart.Expressions.Delete(expression2)
    
    workPart.Expressions.Delete(expression3)
    
    # ----------------------------------------------
    #   Menu: Edit->Object Display...
    # ----------------------------------------------
    markId7 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    theSession.SetUndoMarkName(markId7, "Class Selection Dialog")
    
    markId8 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Class Selection")
    
    theSession.DeleteUndoMark(markId8, None)
    
    markId9 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Class Selection")
    
    theSession.DeleteUndoMark(markId9, None)
    
    theSession.SetUndoMarkName(markId7, "Class Selection")
    
    theSession.DeleteUndoMark(markId7, None)
    
    # ----------------------------------------------
    #   Dialog Begin Edit Object Display
    # ----------------------------------------------
    # ----------------------------------------------
    #   Dialog Begin Color
    # ----------------------------------------------
    markId10 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Edit Object Display")
    
    displayModification1 = theSession.DisplayManager.NewDisplayModification()
    
    displayModification1.ApplyToAllFaces = True
    
    displayModification1.ApplyToOwningParts = False
    
    displayModification1.NewColor = 11
    
    objects1 = [NXOpen.DisplayableObject.Null] * 1 
    edgeBlend1 = feature2
    face1 = edgeBlend1.FindObject("FACE 3 {(75,1.4644660940673,48.5355339059327) BLOCK(1)}")
    objects1[0] = face1
    displayModification1.Apply(objects1)
    
    nErrs1 = theSession.UpdateManager.DoUpdate(markId10)
    
    displayModification1.Dispose()
    # ----------------------------------------------
    #   Menu: Tools->Journal->Stop Recording
    # ----------------------------------------------
    
if __name__ == '__main__':
    main()
