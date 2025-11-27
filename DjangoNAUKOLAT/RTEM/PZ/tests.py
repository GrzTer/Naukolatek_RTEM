from django.test import TestCase, RequestFactory
from django.urls import reverse
from unittest.mock import patch
from .views import predict
import numpy as np


class TestPredictView(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    @patch("PZ.views.apps")
    def test_predict_view(self, mock_apps):
        # Mock the model's predict method
        mock_model = mock_apps.get_app_config.return_value.model
        mock_model.predict.return_value = np.array([[0.5]])

        # Create a request and get the response
        request = self.factory.get(reverse("predict"))
        response = predict(request)

        # Check that the response is successful
        self.assertEqual(response.status_code, 200)
