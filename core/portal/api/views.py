import math

from rest_framework import authentication, permissions
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from user.models import Profile

from ..top_headlines import get_top_headlines_country


class HeadLinesListAPIView(APIView):
    """
    View to list all top head lines.

    * Requires token authentication.
    * Only authorize are able to access this view.
    """
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]

    def get(self, request, *args, **kwargs):
        """
        Return a list of all users.
        """
        try:
            page = self.request.GET.get('page')
            user = self.request.user
            users = Profile.objects.get(user=user)
            country_tag = users.country_tag
            source_tag = users.source_tag
            keyword_tag = users.keyword_tag
            news_list, total_result = get_top_headlines_country(country_tag, source_tag, keyword_tag, request, page)
            page = '1' if page is None else page
            page = int(page)
            total_article = total_result
            total_page = math.ceil(total_article / 10)
            if total_page == page:
                next_page = 0
            else:
                if total_result == 0:
                    next_page = 0
                else:
                    next_page = page + 1

            data = {
                'news': news_list,
                'current_page': page,
                'next_page': next_page,
                'previous_page': page - 1
            }
            return Response(data, status.HTTP_200_OK)
        except:
            page = 1
            news_list = []
            data = {
                'news': news_list,
                'current_page': page,
                'next_page': 1,
                'previous_page': 0
            }
            return Response(data, status.HTTP_429_TOO_MANY_REQUESTS)
