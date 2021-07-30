import ast
import json

from msfapp.models import ClosePairs
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import ClosePairsSerializer


class ClosePairsListApiView(APIView):

  def get(self, request, *args, **kwargs):

    #list all the closepair items
    closepairs = ClosePairs.objects.all()
    serializer = ClosePairsSerializer(closepairs, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)

  def post(self, request, *args, **kwargs):
    points = list(ast.literal_eval(request.data.get('points')))
    def square(x):
      return x*x
    
    def getDist(a,b):
      return square(a[0]-b[0]) + square(a[1]-b[1])
    
    #Initiate smallest distance and pair giving that
    best=[getDist(points[0], points[1]), (points[0], points[1])]

    def pairchecker(a,b):
      c = getDist(a,b)
      if c < best[0]:
        best[0]=c
        best[1]=a,b
      
    # merges two sorted lists based on the y coordinate
    def mergeLists(lisA, lisB):
      i=0
      j=0
      while i < len(lisA) or j < len(lisB):
        if j >= len(lisB) or (i < len(lisA) and lisA[i][1] <= lisB[j][1]):
          yield lisA[i]
          i +=1
        else:
          yield lisB[j]
          j += 1


    #Recursively get closest pair
    def recurs(points):
      #Terminate if only one element/point left in the list
      if len(points)<2:
        return points
      
      split = len(points)//2
      splitx = points[split][0]
      points = list(mergeLists(recurs(points[:split]), recurs(points[split:])))

      E = [point for point in points if abs(point[0]-splitx) < best[0]]

      for i in range(len(E)):
        for j in range(1,8):
          if i+j < len(E):
            pairchecker(E[i], E[i+j])
      return points

    points.sort()
    recurs(points)

    print(json.dumps(best[1]))
    data = {
        'submitted_points': request.data.get('points'), 
        'closest_pair': json.dumps(best[1]), 
      
    }
    serializer = ClosePairsSerializer(data=data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
