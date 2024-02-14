from datetime import datetime
from django.views import View
from django.http import JsonResponse


class InitialView(View):
    def get(self, request, *args, **kwargs):
        return JsonResponse(
            {
                "hello": "world",
                "checked_at": datetime.now().strftime("%Y-%m-%d_%H:%M:%S"),
            }
        )
