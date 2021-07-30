import json
from random import uniform

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from msfapp.api.serializers import ClosePairsSerializer
from msfapp.models import ClosePairs


class ClosePairTestCase(APITestCase):
    
  def test_close_pair_result(self):
    data={"points": "(0,0),(7,6),(2,20),(12,5),(16,16),(5,8),(19,7),(14,22),(8,9),(7,29),(10,11),(1,13)"}
    
    response = self.client.post("/closestpoints/api/", data)
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    self.assertEqual(response.data['closest_pair'], '[[7, 6], [5, 8]]')
