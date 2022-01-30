from unittest import result
from django.urls import reverse
from django.core.management import call_command

from rest_framework import status
from rest_framework.test import APITestCase
from api import serializers

from api.models import Diagnosis


class DiagnosisTest(APITestCase):

    def setUp(self):
        self.url = reverse('diagnosis')

        self.serializer = serializers.DiagnosisSerializer
        # generate 100 records with custom command
        call_command('seed_data')

        self.payload = {
            'category_title': 'Triumph',
            'category_code': 'APC111',
            'full_code': 'APC11111111111',
            'abbreviated_description': 'Triumphant by me',
            'diagnosis_code': 'Verify Account',
            'full_description': 'Full description added',
        }

    def test_total_count_is_100(self):
        """
        Ensure the seeded data count is 100
        """
        data = Diagnosis.objects.count()
        self.assertEquals(100, 100)

    def test_create_new_diagnosis(self):
        """
        Ensure we can create new diagnosis
        """
        self.assertEquals(Diagnosis.objects.count(), 100)

        response = self.client.post(self.url, self.payload)

        self.assertEquals(Diagnosis.objects.count(), 101)

        self.assertEquals(response.json()['category_title'], 'Triumph')

        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_list_diagnosis_returns_valid_format(self):
        """
        Ensure the list of diagnosis returns valid format
        """

        response = self.client.get(self.url)

        diagnoses = Diagnosis.objects.all()

        self.assertEqual(response.data['count'], diagnoses.count())

        self.assertIsNone(response.data['previous'])

    def test_show_single_diagnosis_returns_valid_format(self):
        """
        Ensure a single diagnosis display returns valid format.
        """

        response = self.client.post(self.url, self.payload)

        data = response.json()

        response_with_id = self.client.get(
            self.url, kwargs={'id': data['id']})

        diagnosis = Diagnosis.objects.get(pk=data['id'])

        self.assertEqual(data['id'], str(diagnosis.id))

        self.assertEquals(response_with_id.status_code, status.HTTP_200_OK)

    def test_update_single_diagnosis_returns_valid_format(self):
        """
        Ensure a single diagnosis display returns valid format.
        """

        response = self.client.post(self.url, self.payload)

        data = response.json()

        response_with_id = self.client.patch(
            self.url + '/' + data['id'], self.payload)
        self.assertEquals(response_with_id.status_code,
                          status.HTTP_200_OK)
        diagnosis = Diagnosis.objects.get(pk=data['id'])
        self.assertEqual(data['id'], str(diagnosis.id))

    def test_delete_single_diagnosis_returns_is_destroyed(self):
        """
        Ensure deleting a single diagnosis display returns valid format.
        """

        response = self.client.post(self.url, self.payload)

        data = response.json()

        response_with_id = self.client.delete(
            self.url + '/' + data['id'])

        deleted_data = Diagnosis.objects.filter(pk=data['id']).exists()

        self.assertEqual(response_with_id.status_code,
                         status.HTTP_204_NO_CONTENT)
        self.assertFalse(deleted_data)

    def test_store_single_diagnosis_with_incomplete_data(self):
        """
        Store new diagnosis with incomplete data.
        """

        payload = {
            'category_title': 'Triumph',
            'category_code': 'APC111',
            'full_code': 'APC11111111111',
        }

        response = self.client.post(self.url, payload)

        self.assertEquals(Diagnosis.objects.count(), 100)

        self.assertEquals(response.status_code,
                          status.HTTP_400_BAD_REQUEST)
        self.assertEqual({
            "abbreviated_description": [
                "This field is required."
            ],
            "diagnosis_code": [
                "This field is required."
            ],
            "full_description": [
                "This field is required."
            ]
        }, response.data)

    def test_destroy_for_invalid_diagnosis_data(self):
        """
        Delete invalid diagnosis data returns Not found.
        """

        response_with_id = self.client.delete(
            self.url + '/' + '0')

        self.assertEqual(response_with_id.status_code,
                         status.HTTP_404_NOT_FOUND)
        self.assertEqual({
            "detail": "Not found."
        }, response_with_id.data)

    def test_update_for_invalid_diagnosis_data(self):
        """
        Update invalid diagnosis data returns Not found.
        """
        response_with_id = self.client.delete(
            self.url + '/' + '0')

        self.assertEqual(response_with_id.status_code,
                         status.HTTP_404_NOT_FOUND)
        self.assertEqual({
            "detail": "Not found."
        }, response_with_id.data)
