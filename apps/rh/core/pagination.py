"""
==========================================================
SGCP - Système de Gestion de Carrière du Personnel

Fichier : core/pagination.py

Description :
    Pagination commune du SGCP.

Auteur : SGCP
Version : 1.0
==========================================================
"""

from rest_framework.pagination import PageNumberPagination


class SGCPPagination(PageNumberPagination):
    """
    Pagination standard du SGCP.
    """

    page_size = 30

    page_size_query_param = "page_size"

    max_page_size = 1000